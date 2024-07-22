import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.xception import preprocess_input
from flask import Flask, request, render_template

app = Flask(__name__)

model = load_model(r"C:\Users\adith\Desktop\COVID19_Dataset\covid19-radiography-database\COVID-19_Radiography_Dataset\xception.h5")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    try:
        file = request.files['image']
        if file:
            basepath = os.path.dirname(__file__)
            print('Current path:', basepath)
            filepath = os.path.join(basepath, 'static/uploads', file.filename)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            print('File path:', filepath)
            file.save(filepath)
            image = load_img(filepath, target_size=(299, 299))
            x = img_to_array(image)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)
            prediction = np.argmax(model.predict(x), axis=1)
            index = ['Covid-19', 'Lung Opacity', 'Normal', 'Viral Pneumonia']
            result = index[prediction[0]]
            text = "The person is diagnosed with: " + str(result)
            return render_template("index.html", result=text)
        else:
            return render_template("index.html", result="No file uploaded")
    except Exception as e:
        print("Error occurred:", e)
        return render_template("index.html", result="An error occurred during prediction")

if __name__ == "__main__":
    app.run(debug=True)
