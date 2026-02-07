from flask import Flask, request, jsonify, send_file, send_from_directory
from PIL import Image
import random
from datetime import datetime
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

history = []

# -------- AI PREDICTION (SIMULATED CNN) --------
def predict_defect(image_path):
    defects = ["Normal", "Scratch Defect", "Crack Defect", "Contamination"]
    prediction = random.choice(defects)
    confidence = round(random.uniform(85, 99), 2)
    return prediction, confidence

# -------- API ROUTES --------
@app.route("/")
def home():
    return send_file("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["image"]
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    defect, confidence = predict_defect(path)

    result = {
        "filename": file.filename,
        "defect": defect,
        "confidence": confidence,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    history.append(result)

    return jsonify(result)

@app.route("/history")
def get_history():
    return jsonify(history)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
