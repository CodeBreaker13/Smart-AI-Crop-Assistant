# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set HF cache inside container
ENV HF_HUB_CACHE=/app/hf_cache

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the port HF Spaces uses
EXPOSE 7860

# Run the Flask app
CMD ["python", "app.py"]
