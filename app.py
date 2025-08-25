from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
from io import BytesIO

app = Flask(__name__)

model = load_model('models/batik_model.h5')

labels = {
    0: 'batik-bali', 1: 'batik-betawi', 2: 'batik-celup', 3: 'batik-cendrawasih',
    4: 'batik-ceplok', 5: 'batik-ciamis', 6: 'batik-garutan', 7: 'batik-gentongan',
    8: 'batik-kawung', 9: 'batik-keraton', 10: 'batik-lasem', 11: 'batik-megamendung',
    12: 'batik-parang', 13: 'batik-pekalongan', 14: 'batik-priangan', 15: 'batik-sekar',
    16: 'batik-sidoluhur', 17: 'batik-sidomukti', 18: 'batik-sogan', 19: 'batik-tambal'
}

def preprocess_image(file, target_size=(224, 224)):
    img = Image.open(BytesIO(file.read())).convert('RGB')
    img = img.resize(target_size)
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files['image']
    try:
        
        img_array = preprocess_image(file)
        predictions = model.predict(img_array)
        probabilities = predictions[0]

        top_indices = np.argsort(probabilities)[-3:][::-1]

        results = []
        for i in top_indices:
            if int(i) in labels:
                batik_id = labels[int(i)]
                confidence = float(probabilities[i])
                
                results.append({
                    "pattern": batik_id.replace("batik-", "").replace("-", " ").title(),
                    "code": batik_id,
                    "score": round(confidence * 100, 1),  
                    "match": "high" if confidence > 0.8 else "medium" if confidence > 0.5 else "low"
                })
        
        return jsonify({
            "success": True,
            "detected": results[0]["pattern"] if results else "Unknown",
            "alternatives": results
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=9013)