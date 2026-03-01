## PREDIKSI HARGRA LEPTOP (BEGINER ML PROJECT) 💻

HAI SAYA DISINI MEMBANGUN MODEL MACHINE LEARNING REGRESSION UNTUK MEMPREDSIKSI HARGA LAPTOP

## DATA SET 📊

SAYA MENGAMABIL DATA SET DARI KAGLE UNTUK MELATIH MODEL REGRESSION SAYA, KURANG LEBIH MENNGGUNAKAN 800 DATA

Target(label)

- harga laptop

Fitur data yang saya gunakan:

-brand
- processor_brand
- processor_name
- processor_gnrtn
- ram_gb
- ram_type
- ssd
- hdd
- os
- os_bit
- graphic_card_gb
- weight
- warranty
- Touchscreen
- msoffice
- rating

## workflow 🛠️ (alur kerja)

1. DATA LOADING
memasukan data kedalam notebook

2. EXPLORATOTY DATA
pada tahap ini kita akan melihat apakah data meiliki:
    - missing value
    - data duplication
    - melihat description data

3. DETECTORE OUTLIERS
memastikan apakah data memiliki outliers yang siknifikat

4. PREPROCESSING 
proses ini kita melakukan
    - handling outliers menggunakan metode clapping
    - handling data duplication
    - split data
    - feacture enggine
    - scalling data

5. MODEL DEVELOPLMENT
kita sudah masuk ketahap melatih model dengan algortima yang kita bituhkan 
    - LGMBRegressor

6. MODEL EVALUATION
    - mean_absolut_error
    - mean_squared_error
    - r2_score

7. HASIL EVALUATION MODEL
    - MAE = 9618.96334788139
    - RMSE = 14482.174326786711
    - R2 SCORE =  0.833677761048091

8. MODEL DEPLOYMENT
    - menyimpan model menggunakan joblib
    - proses deplyo ke interface masih dalam pengerjaan


## CARA MENJALANKAN CODE ML 🧑‍💻

1. clone repsository ini (clon nama file model_finis.ipynb)
2. jalan kan di IDE anda
3. jalan model training (jika anda ingin melakukan traning model regresion)
4. untuk menjalan kan di wen interface masih dalam masa pengembangan
5. atau bisa masuk lewat ip ini :http://127.0.0.1:5000/predict

## HAL YANG SAYA PELAJARI DALAM MEMBANGUN MDOEL MACHINE LEARNING INI 📚

1. Memahai struktur data untuk melatih model ML 
2. Menangani outliers yanng dominan di dataset
3. Melakukan handling missing value dan data duplication
4. Menyelasaikan masalah antara model training dan testing model dengan data baru
5. Mennetukan algortima yang efektif untuk kondisi data set
6. melakukan deploy menggunakan flask

## PERENCANAAN YANG AKAN SAYA LAKUKAN KEDEPANNYA 📖

1. Saya akan menabahkan labih banyak data set agar akurasi menignkat
2. Menggunakan hiper parameter tuning
4. Mengoptimalkan hasil prediksi model karna model ku saat ini belum bisa memprediksi secara real time

## TENTANG SAYA 📝

SAYA ADALAH SORANG PELAJAR KELAS 12 DAN INI ADALAH PROJECT MACHINE LEARNING PERTAMA SAYA 



