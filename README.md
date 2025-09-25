---
title: FinalProBack
emoji: 📉
colorFrom: purple
colorTo: yellow
sdk: docker
pinned: false
license: unknown
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

<!--
TEAM MEMBERS-
GOURAV VED
PRABHASH KUMAR
SIDDHARTH GAUTAM
YASH KUMAR
DIVA LAKRA
JYOTI
-->
<h1 align="center">🌱 CropVision AI</h1>
<p align="center">
  <em>AI-powered Plant Disease Detection with Grok Cure Assistant</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Frontend-React-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Backend-Flask-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Model-TensorFlow-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Deployment-HuggingFace-yellow?style=for-the-badge"/>
</p>

<hr/>

<h2 id="overview">📌 Overview</h2>
<p>
<strong>CropVision AI</strong> is a full-stack project that detects diseases in crop leaves using a
TensorFlow Lite model. It integrates:
</p>

<ul>
  <li><strong>Frontend (React):</strong> User-friendly interface to upload leaf images and view results.</li>
  <li><strong>Backend (Flask):</strong> TensorFlow-powered API to predict plant diseases. Hosted on Hugging Face Spaces.</li>
  <li><strong>Grok Assistant:</strong> AI-powered cure assistant suggesting safe, practical, and organic-first treatments.</li>
</ul>

<hr/>

<h2 id="workflow">🔁 How It Works</h2>
<ol>
  <li>User uploads a plant leaf image via the React frontend.</li>
  <li>Image is sent to the Flask backend <code>/predict</code> endpoint.</li>
  <li>TensorFlow Lite model processes the image and returns prediction (disease + confidence).</li>
  <li>Frontend displays results and provides an option to ask <strong>Grok Assistant</strong> for cures.</li>
  <li>Assistant suggests treatment steps and preventive practices.</li>
</ol>

<hr/>

<h2 id="features">✨ Features</h2>
<ul>
  <li>🌿 Multi-class plant disease detection with deep learning.</li>
  <li>⚡ Lightweight TensorFlow Lite inference for fast predictions.</li>
  <li>💻 React frontend with modern UI.</li>
  <li>🤖 Grok AI integration for treatment and cure suggestions.</li>
  <li>☁ Backend deployed on Hugging Face Spaces.</li>
</ul>

<hr/>

<h2 id="quick-start">🚀 Quick Start</h2>

<h3>1. Clone Repository</h3>

<pre><code>git clone https://github.com/your-username/your-repo.git
cd your-repo
</code></pre>

<h3>2. Run Frontend (React)</h3>

<pre><code>cd frontend
npm install
npm start
</code></pre>

<p>Frontend will run at <code>http://localhost:3000</code>.</p>

<h4>.env Example</h4>

<pre><code>REACT_APP_API_URL=http://localhost:5000   # or Hugging Face backend URL
REACT_APP_GROK_ENABLED=true
</code></pre>

<h3>3. Run Backend (Flask)</h3>

<pre><code>cd backend
python -m venv venv
source venv/bin/activate    # Linux/macOS
# venv\Scripts\activate     # Windows
pip install -r requirements.txt
python app.py
</code></pre>

<p>Backend will run at <code>http://127.0.0.1:5000</code>.</p>

<hr/>

<h2 id="api">📡 API Endpoints</h2>

<h3>/predict</h3>
<p><strong>POST</strong> - Upload a leaf image to predict disease.</p>

<pre><code>curl -X POST "http://localhost:5000/predict" \
  -F "file=@/path/to/leaf.jpg"
</code></pre>

<p><strong>Response:</strong></p>
<pre><code>{
  "disease": "Late Blight",
  "confidence": 0.9432
}
</code></pre>

<h3>/grok</h3>
<p><strong>POST</strong> - Get cure/treatment suggestions from Grok Assistant.</p>

<pre><code>curl -X POST "http://localhost:5000/grok" \
  -H "Content-Type: application/json" \
  -d '{"disease":"Late Blight"}'
</code></pre>

<p><strong>Response:</strong></p>
<pre><code>{
  "assistant_text": "1) Remove infected leaves... 2) Apply copper fungicide... 3) Improve airflow..."
}
</code></pre>

<hr/>

<h2 id="repo-structure">📁 Repository Structure</h2>

<pre><code>.
├─ frontend/                 # React app
│  ├─ src/
│  └─ .env
├─ backend/                  # Flask server
│  ├─ app.py
│  ├─ requirements.txt
│  └─ models/plant_disease_model.tflite
├─ README.md
└─ LICENSE
</code></pre>

<hr/>

<h2 id="contributing">🤝 Contributing</h2>
<p>
Contributions, issues, and feature requests are welcome!<br/>
Feel free to fork the repo and submit pull requests.
</p>

<hr/>

<h2 id="license">📜 License</h2>
<p>
This project is licensed under the <strong>MIT License</strong>.  
See the <a href="LICENSE">LICENSE</a> file for details.
</p>

<hr/>

<h2 id="credits">🙏 Credits</h2>
<ul>
  <li>🧑‍🔬 Dataset: PlantVillage & other public crop disease datasets.</li>
  <li>🧠 Model Training: TensorFlow + TFLite.</li>
  <li>🤖 AI Cure Assistant: Grok API integration.</li>
  <li>☁ Hosting & Model Hub: Hugging Face Spaces.</li>
</ul>

# 25010 - SMART CROP ADVISORY SYSTEM FOR SMALL AND MARGINAL FARMERS

This README provides an overview of the project, including team details, relevant links, tasks completed, tech stack, key features, and steps to run the project locally.  

---

## Team Details  

**Team Name:** DebuggingTITANS  

**Team Leader:** [@CodeBreaker13](https://github.com/CodeBreaker13)  

**Team Members:**  
- MEMBER_1 – 2024UIC3535 – [@CodeBreaker13](https://github.com/CodeBreaker13)  
- MEMBER_2 – 2024UIC3504 – [@8920217247](https://github.com/8920217247)  
- MEMBER_3 – 2023UEC2622 – [@Sidd-harth011](https://github.com/Sidd-harth011)  
- MEMBER_4 – 2023UEC2516 – [@gjgj7676](https://github.com/gjgj7676)  
- MEMBER_5 – 2024UCM2343 – [@jyoti9406](https://github.com/jyoti9406)  
- MEMBER_6 – 2025UME7608 – [@divalakra](https://github.com/divalakra)  

---

## Project Links  

- **SIH Presentation:** [Final SIH Presentation](https://www.canva.com/design/DAGzmm53hDI/nrkxLKfvW8NQYk69Xo2fTw/edit?utm_content=DAGzmm53hDI&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)  
- **Video Demonstration:** [Watch Video](https://youtu.be/TrAbZGk9iTU?si=iELLg4-hyruI7-vx)  
- **Live Deployment:** [View Deployment](https://pdrm-pfront.vercel.app/)  
- **Source Code:** [GitHub Repository](GITHUB_REPO_LINK)  
- **Additional Resources:** [Other Relevant Links](ANY_OTHER_LINKS)  
