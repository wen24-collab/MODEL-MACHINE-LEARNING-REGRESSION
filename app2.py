from flask import Flask, render_template, request
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.preprocessing import StandardScaler
import joblib
import pandas as pd
import numpy as np

model = joblib.load("pipeline_model_finis.pkl")



#application interface

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    
    brand = request.form["brand"]
    processor_brand = request.form["processor_brand"]
    processor_name = request.form["processor_name"]
    ram = (request.form["ram_gb"])
    ram_type = request.form["ram_type"]
    #data value
    processor_gnrtn = "10th"
    ssd = "521"
    hdd = "0"
    os = "Windows"
    os_bit = "64-bit"
    gpu = "0"
    weight = "Casual"
    warranty = "1 Year"
    Touchscreen = "no"
    msoffice = "no"
    rating = "4"
    nor = "0"
    norv= "0"
    
    data_model = pd.DataFrame([{
        "brand": brand,
        "processor_brand": processor_brand,
        "processor_name": processor_name,
        "processor_gnrtn": processor_gnrtn,
        "ram_gb": ram,
        "ram_type": ram_type,
        "ssd" : ssd,
        "hdd" : hdd,
        "os" : os,  
        "os_bit" : os_bit,
        "graphic_card_gb" : gpu,
        "weight" : weight,
        "warranty" : warranty,
        "Touchscreen" : Touchscreen,
        "msoffice" : msoffice,
        "rating" : rating,
        "Number of Ratings" : nor,
        "Number of Reviews" : norv
        
        
    }])
    

    #GABUNGKAN MODDEL 
    
    predic_model = model.predict(data_model)[0]
    harga = int(predic_model)
    harga_final = f"Rp{harga:,.0f}".replace(",", ".")

    
    return render_template("index.html", predic_model=harga_final)

if __name__ == "__main__":
    app.run(debug=True)
    