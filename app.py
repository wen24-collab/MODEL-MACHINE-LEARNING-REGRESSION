from flask import Flask, render_template, request
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.preprocessing import StandardScaler
import joblib
import numpy as np
import pandas as pd


#application inteance


#LOAD PIPLINE

MODEL = joblib.load("piplane_model.pkl")

model = MODEL["model"]
scaler = MODEL["scaler"]
encode = MODEL["encoder"]


app = Flask(__name__)

@app.route("/") #disini kita membuat pintu masuk/ membuat url untuk app kita 
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"]) #disini nanti akan menjalankan code ketika menerima requesr "ptrdict" dari html
def predict():

    brand = request.form["brand"]
    processor = request.form["processor_brand"]
    processor_name = request.form["processor_name"]
    ram = request.form["ram_gb"]
    ram_type = request.form["ram_type"]
    sdd = request.form["ssd"]
    hdd = request.form["hdd"]
    os = request.form["os"]
    os_bit = request.form["os_bit"]
    gpu = request.form["graphic_card_gb"]
    weight = request.form["weight"]
    warranty = request.form["warranty"]
    Touchscreen = request.form["Touchscreen"]
    msoffice = request.form["msoffice"]
    rating = request.form["rating"]
    
     #karena hasil dari encode itu array jadi kita buat jadi data frame
    
    #scalling 
    
    
#ubah ke data fram karna model butuh data dengan data fram

    data = pd.DataFrame([{
        "Brand": brand,
        "processor": processor,
        "processor name": processor_name,
        "ram": ram,
        "ram_type": ram_type,
        "ssd": sdd,
        #default
        "hdd": hdd,
        "os": os,
        "os_bit": int(os_bit),
        "graphic_card_gb": float(gpu),
        "weight": float(weight),
        "warranty": float(warranty),
        "Touchscreen": Touchscreen,
        "msoffice": msoffice,
        "rating": float(rating)
}])

#kemudian kita buat model prdiction nya
    prediction_model = MODEL.predict(encode_final)
    
    #kita kembalikan lagi ke html agar nanti kita bisa lihat di borser
    return render_template("index.html", prediction_model=round(prediction_model[0], 2)) #artinya ini mangambil array dari variabel prediction_model nilai pertama dan membulatkan 2 angka setalah koma

if __name__ == '__main__':
    app.run(debug=True)

