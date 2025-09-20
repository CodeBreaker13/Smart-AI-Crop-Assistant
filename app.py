import os
import json
import numpy as np
import tensorflow as tf
from PIL import Image
from flask import Flask, request, jsonify
from flask_cors import CORS
import io
from huggingface_hub import hf_hub_download

# Set Hugging Face cache to a folder inside the container
os.environ['HF_HUB_CACHE'] = '/tmp/hf_cache'

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load model and class indices
working_dir = os.path.dirname(os.path.abspath(__file__))
#model_path = os.path.join(working_dir, "trained_model", "plant_disease_model.tflite")
model_path = hf_hub_download(
    repo_id="sidd-harth011/checkingPDRMod",  # ✅ your repo
    filename="plant_disease_model.tflite"
)

# Load the TFLite model
interpreter = tf.lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Load class indices
class_indices_path = os.path.join(working_dir, "class_indices.json")
with open(class_indices_path, 'r') as f:
    class_indices = json.load(f)

# -----------------------------
# Preprocessing function
# -----------------------------
def load_and_preprocess_image(image, target_size=(224, 224)):
    img = image.resize(target_size)
    img_array = np.array(img, dtype=np.float32)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array

# -----------------------------
# Function to clean label
# -----------------------------
def clean_label(label: str) -> str:
    if "___" in label:
        label = label.split("___")[-1]
    return label.replace("_", " ").title()

# -----------------------------
# Prediction function
# -----------------------------
def predict_image_class(image):
    preprocessed_img = load_and_preprocess_image(image)
    interpreter.set_tensor(input_details[0]['index'], preprocessed_img)
    interpreter.invoke()
    predictions = interpreter.get_tensor(output_details[0]['index'])
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    predicted_class_name = class_indices[str(predicted_class_index)]
    predicted_class_name = clean_label(predicted_class_name)
    
    # Get confidence score
    confidence = float(predictions[0][predicted_class_index])
    
    return predicted_class_name, confidence

# -----------------------------
# API endpoint for image classification
# -----------------------------
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if image is in the request
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
        
        # Get the image file
        image_file = request.files['image']
        
        # Check if filename is empty
        if image_file.filename == '':
            return jsonify({'error': 'No image selected'}), 400
        
        # Read and process the image
        image = Image.open(io.BytesIO(image_file.read()))
        
        # Make prediction
        predicted_class, confidence = predict_image_class(image)
        
        # Return prediction as JSON
        return jsonify({
            'prediction': predicted_class,
            'confidence': confidence,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'error'}), 500

# -----------------------------
# Health check endpoint
# -----------------------------
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'message': 'Plant Disease Classification API is running'})

# -----------------------------
# Run the Flask app
# -----------------------------
if __name__ == '__main__':
    # You can change the host and port as needed
    app.run(host='0.0.0.0', port=7860, debug=False)