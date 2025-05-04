# Proyek Analisis Attrisi Karyawan Jaya Jaya Maju

## Business Understanding

Jaya Jaya Maju adalah perusahaan multinasional yang telah beroperasi sejak tahun 2000 dengan lebih dari 1000 karyawan yang tersebar di berbagai lokasi. Meskipun telah menjadi perusahaan besar, Jaya Jaya Maju menghadapi tantangan dalam manajemen karyawan, yang menyebabkan tingginya attrition rate (tingkat keluar karyawan) hingga melebihi 10%.

Tingkat attrisi yang tinggi ini berdampak negatif pada perusahaan karena:
- Meningkatkan biaya rekrutmen dan pelatihan karyawan baru
- Menurunkan produktivitas karena hilangnya pengetahuan dan keahlian
- Dapat mempengaruhi moral karyawan yang masih bertahan
- Mengganggu kelangsungan operasional departemen terkait

## Permasalahan Bisnis

Permasalahan utama yang dihadapi oleh departemen HR Jaya Jaya Maju adalah:
1. Tingginya tingkat attrisi karyawan yang mencapai lebih dari 10%
2. Kurangnya pemahaman tentang faktor-faktor utama yang mempengaruhi keluarnya karyawan
3. Tidak adanya sistem monitoring yang efektif untuk mengidentifikasi tren attrisi
4. Kesulitan dalam mengambil tindakan preventif karena kurangnya analisis prediktif

## Cakupan Proyek

Proyek ini akan mencakup beberapa hal berikut:
1. Analisis data HR untuk mengidentifikasi faktor-faktor yang mempengaruhi attrisi karyawan
2. Pembuatan dashboard bisnis untuk memantau dan visualisasi metrik attrisi
3. Pengembangan model machine learning untuk memprediksi kemungkinan karyawan meninggalkan perusahaan
4. Penyusunan rekomendasi strategi untuk mengurangi tingkat attrisi berdasarkan hasil analisis

## Persiapan

### Sumber Data
Data yang digunakan dalam proyek ini berasal dari dataset internal HR Jaya Jaya Maju yang tersimpan dalam file `employee_data.csv`. Dataset ini dapat diakses melalui tautan berikut:
[https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Dataset ini terdiri dari 35 kolom yang mencakup berbagai informasi:

- **Demografis**: Age, Gender, MaritalStatus
- **Pekerjaan**: JobRole, Department, JobLevel, JobInvolvement, BusinessTravel
- **Kompensasi**: MonthlyIncome, DailyRate, HourlyRate, MonthlyRate, PercentSalaryHike, StockOptionLevel
- **Kepuasan**: JobSatisfaction, EnvironmentSatisfaction, WorkLifeBalance, RelationshipSatisfaction
- **Pengalaman**: TotalWorkingYears, YearsAtCompany, YearsInCurrentRole, YearsWithCurrManager, NumCompaniesWorked
- **Lainnya**: DistanceFromHome, OverTime, TrainingTimesLastYear, Education, EducationField
- **Target**: Attrition (variabel target yang menunjukkan apakah karyawan keluar atau tidak)

Dataset awal memiliki beberapa nilai NaN pada kolom Attrition yang perlu dibersihkan dalam proses preprocessing.

### Setup Environment

Untuk menjalankan proyek ini, Anda perlu mengikuti langkah-langkah berikut:

1. Clone repository ini ke komputer lokal Anda:
```bash
git clone https://github.com/username/employee-attrition-analysis.git
cd employee-attrition-analysis
```

2. Buat virtual environment (opsional, tapi sangat direkomendasikan):
```bash
python -m venv attrition_env
```

3. Aktifkan virtual environment:
   - Untuk Windows:
   ```bash
   attrition_env\Scripts\activate
   ```
   - Untuk macOS/Linux:
   ```bash
   source attrition_env/bin/activate
   ```

4. Install semua dependency yang diperlukan:
```bash
pip install -r requirements.txt
```

5. Download dataset dari tautan yang diberikan dan simpan di folder `data/`:
```bash
mkdir -p data
# Download file secara manual dari https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee
# atau gunakan curl/wget jika tersedia
```

6. Jalankan notebook Jupyter untuk analisis:
```bash
jupyter notebook employee_attrition_analysis.ipynb
```

7. Untuk menjalankan dashboard:
```bash
# Pindah ke direktori dashboard
cd dashboard

# Jalankan aplikasi dashboard
python app.py
```

Dashboard dapat diakses melalui browser web di `http://localhost:8050/` dengan kredensial berikut:
- Username: root@mail.com
- Password: root123

### Struktur Folder

```
employee-attrition-analysis/
├── data/
│   └── employee_data.csv
├── dashboard/
│   ├── app.py
│   ├── assets/
│   └── requirements.txt
├── model/
│   └── attrition_model.pkl
├── notebook/
│   └── employee_attrition_analysis.ipynb
├── README.md
├── requirements.txt
└── prediction.py
```

### Daftar Library yang Digunakan

Berikut adalah daftar library yang digunakan dalam proyek ini:

```
pandas==1.5.3
numpy==1.24.3
matplotlib==3.7.1
seaborn==0.12.2
scikit-learn==1.2.2
joblib==1.2.0
jupyter==1.0.0
dash==2.10.2
plotly==5.14.1
```

## Analisis Data dan Visualisasi

Setelah melakukan eksplorasi data, beberapa pola penting telah teridentifikasi yang menunjukkan hubungan antara berbagai faktor dengan tingkat attrisi karyawan:

### 1. Distribusi Attrisi Keseluruhan
Dari total 1,058 karyawan setelah proses pembersihan data, sekitar 84% (sekitar 870 karyawan) tetap bertahan di perusahaan, sementara 16% (sekitar 188 karyawan) memilih untuk keluar. Visualisasi distribusi ini menunjukkan ketidakseimbangan kelas (class imbalance) yang perlu diperhatikan dalam pembuatan model prediksi. Meskipun persentase karyawan yang keluar terlihat kecil, namun angka 16% ini tetap berada di atas rata-rata industri yang biasanya berada di kisaran 10%.

### 2. Analisis Faktor-Faktor Attrisi

Berdasarkan visualisasi yang telah dibuat, beberapa faktor utama yang mempengaruhi attrisi karyawan:

#### Usia (Age)
Karyawan yang lebih muda memiliki kecenderungan lebih tinggi untuk meninggalkan perusahaan dibandingkan karyawan yang lebih tua. Boxplot menunjukkan median usia karyawan yang keluar lebih rendah dibandingkan yang bertahan.

#### Jarak dari Rumah ke Kantor (Distance From Home)
Karyawan dengan jarak rumah ke kantor yang lebih jauh menunjukkan tingkat attrisi yang lebih tinggi. Data menunjukkan median jarak tempuh untuk karyawan yang keluar lebih tinggi dibandingkan karyawan yang bertahan.

#### Pendapatan Bulanan (Monthly Income)
Terdapat korelasi yang jelas antara pendapatan bulanan dengan attrisi. Karyawan dengan pendapatan lebih rendah memiliki kecenderungan lebih tinggi untuk keluar. Boxplot menunjukkan median pendapatan untuk karyawan yang keluar secara signifikan lebih rendah.

#### Kepuasan Kerja (Job Satisfaction)
Karyawan dengan tingkat kepuasan kerja yang rendah (level 1-2) lebih cenderung untuk keluar dibandingkan dengan karyawan yang memiliki tingkat kepuasan kerja tinggi (level 3-4).

#### Keseimbangan Kerja-Hidup (Work-Life Balance)
Visualisasi menunjukkan bahwa karyawan dengan keseimbangan kerja-hidup yang buruk (level 1-2) memiliki tingkat attrisi yang lebih tinggi dibandingkan dengan yang memiliki keseimbangan baik (level 3-4).

#### Lama Bekerja di Perusahaan (Years at Company)
Karyawan yang baru bekerja di perusahaan (0-5 tahun) menunjukkan kecenderungan lebih tinggi untuk keluar dibandingkan dengan karyawan yang telah lama bekerja.

### 3. Feature Importance

Analisis feature importance dari model machine learning menunjukkan bahwa faktor-faktor yang paling berpengaruh terhadap attrisi karyawan adalah:

1. Monthly Income (Pendapatan Bulanan) - 0.200
2. Age (Usia) - 0.175
3. DistanceFromHome (Jarak dari Rumah) - 0.150
4. TotalWorkingYears (Total Tahun Bekerja) - 0.125
5. YearsAtCompany (Lama Bekerja di Perusahaan) - 0.100
6. YearsWithCurrManager (Lama Bekerja dengan Manajer Saat Ini) - 0.075
7. JobSatisfaction (Kepuasan Kerja) - 0.050
8. WorkLifeBalance (Keseimbangan Kerja-Hidup) - 0.050

## Business Dashboard

Dashboard HR Attrition Analysis telah dibuat menggunakan Metabase untuk membantu departemen HR dalam memantau dan menganalisis faktor-faktor yang mempengaruhi attrisi karyawan. Dashboard ini terdiri dari beberapa visualisasi utama:

1. **Attrition Rate Overview**: Menampilkan tingkat attrisi keseluruhan dengan gauge chart yang menunjukkan bahwa dari total 1,470 karyawan, tingkat attrisi saat ini berada pada level tertentu.

2. **Attrition Rate per Department**: Menampilkan jumlah karyawan yang keluar dan persentase attrisi berdasarkan departemen. Visualisasi ini menunjukkan bahwa departemen Research & Development memiliki jumlah karyawan keluar tertinggi, diikuti oleh Sales dan Human Resources.

3. **Attrition Rate berdasarkan Job Role**: Menampilkan distribusi attrisi berdasarkan posisi karyawan. Data menunjukkan bahwa posisi Laboratory Technician, Sales Executive, dan Research Scientist memiliki tingkat attrisi yang lebih tinggi dibandingkan posisi lainnya.

4. **MonthlyIncome vs Attrition**: Visualisasi yang menampilkan hubungan antara pendapatan bulanan dengan status attrisi, menunjukkan bahwa 64.21% karyawan dengan status tidak keluar (0), sementara 9.12% karyawan dengan pendapatan tertentu memilih untuk keluar (1).

Dashboard dapat diakses menggunakan kredensial berikut:
- Username: root@mail.com
- Password: root123

## Model Machine Learning

Kami telah mengembangkan model machine learning untuk memprediksi kemungkinan seorang karyawan akan meninggalkan perusahaan. Model ini dibangun menggunakan algoritma Random Forest dengan parameter n_estimators=100 dan random_state=42.

### Fitur yang Digunakan
Berdasarkan analisis feature importance, model menggunakan 8 fitur utama:

1. Age (Usia)
2. DistanceFromHome (Jarak dari rumah)
3. JobSatisfaction (Kepuasan kerja)
4. WorkLifeBalance (Keseimbangan kerja-hidup)
5. MonthlyIncome (Pendapatan bulanan)
6. TotalWorkingYears (Total tahun bekerja)
7. YearsAtCompany (Lama bekerja di perusahaan)
8. YearsWithCurrManager (Lama bekerja dengan manajer saat ini)

### Performa Model
Model mencapai akurasi sebesar 83% dalam memprediksi attrisi karyawan. Berikut metrik evaluasi lainnya:

- Precision untuk kelas "Keluar" (1): 0.64
- Recall untuk kelas "Keluar" (1): 0.18
- F1-Score untuk kelas "Keluar" (1): 0.28

Meskipun akurasi keseluruhan cukup baik, model memiliki keterbatasan dalam mendeteksi karyawan yang akan keluar (nilai recall yang rendah untuk kelas 1). Ini menunjukkan bahwa model masih memerlukan penyempurnaan, misalnya dengan teknik oversampling atau hyperparameter tuning.

### Implementasi Model
Model ini telah disimpan sebagai file `attrition_model.pkl` dalam direktori `model/`. Untuk menggunakan model ini, kami telah menyediakan script Python sederhana (`prediction.py`) yang memungkinkan departemen HR memasukkan data karyawan dan mendapatkan prediksi kemungkinan karyawan tersebut akan keluar.

Contoh penggunaan model:

```python
import joblib
import pandas as pd
import numpy as np

# 1. Load the model
model = joblib.load('model/attrition_model.pkl')

# Display header
print("\n" + "="*50)
print("EMPLOYEE ATTRITION PREDICTION SYSTEM")
print("="*50)

# 2. Your full sample data (for display purposes)
full_data = {
    "Age": [35],
    "BusinessTravel": [2],
    "DailyRate": [800],
    # ... data lengkap lainnya ...
}

# Display complete employee profile
df_full = pd.DataFrame(full_data)
print("\nCOMPLETE EMPLOYEE PROFILE:")
print("-"*50)
for col in df_full.columns:
    print(f"{col:<25} : {df_full[col].values[0]}")

# 3. Create a new DataFrame with ONLY the 8 features the model expects
model_features = [
    "Age", 
    "DistanceFromHome", 
    "JobSatisfaction", 
    "WorkLifeBalance", 
    "MonthlyIncome", 
    "TotalWorkingYears", 
    "YearsAtCompany", 
    "YearsWithCurrManager"
]

# Extract only the features the model needs
prediction_data = {}
for feature in model_features:
    prediction_data[feature] = full_data[feature]

# Create the prediction DataFrame
df_prediction = pd.DataFrame(prediction_data)

# 4. Make prediction
prediction = model.predict(df_prediction)
probability = model.predict_proba(df_prediction)

# 5. Display results
print("\nPREDICTION RESULTS:")
print("-"*50)
if prediction[0] == 1:
    result = "AKAN KELUAR dari perusahaan"
    risk_level = "TINGGI"
else:
    result = "TIDAK AKAN keluar dari perusahaan"
    risk_level = "RENDAH"

print(f"Status Prediksi      : Karyawan {result}")
print(f"Tingkat Risiko       : {risk_level}")
print(f"Probabilitas Bertahan: {probability[0][0] * 100:.2f}%")
print(f"Probabilitas Keluar  : {probability[0][1] * 100:.2f}%")
```

## Conclusion

Berdasarkan analisis data dan visualisasi, beberapa kesimpulan utama dapat diambil:

1. **Faktor Finansial Dominan**: Pendapatan bulanan (Monthly Income) adalah faktor paling berpengaruh dalam keputusan karyawan untuk keluar, dengan karyawan bergaji rendah memiliki risiko attrisi lebih tinggi.

2. **Faktor Demografis**: Usia (Age) memiliki korelasi signifikan dengan attrisi, di mana karyawan yang lebih muda cenderung memiliki tingkat attrisi lebih tinggi.

3. **Faktor Geografis**: Jarak dari rumah ke kantor (Distance From Home) berpengaruh terhadap attrisi, di mana karyawan dengan jarak tempuh lebih jauh lebih cenderung untuk keluar.

4. **Pengalaman Kerja**: Karyawan dengan pengalaman kerja total (Total Working Years) dan masa kerja di perusahaan (Years At Company) yang lebih singkat memiliki tingkat attrisi lebih tinggi.

5. **Departemen dengan Tingkat Attrisi Tertinggi**: Research & Development memiliki jumlah karyawan yang keluar tertinggi, diikuti oleh Sales dan Human Resources.

6. **Posisi dengan Risiko Attrisi Tinggi**: Laboratory Technician, Sales Executive, dan Research Scientist menunjukkan tingkat attrisi yang lebih tinggi dibandingkan posisi lainnya.

7. **Faktor Kepuasan**: Tingkat kepuasan kerja (Job Satisfaction) dan keseimbangan kerja-hidup (Work-Life Balance) yang rendah berhubungan dengan peningkatan kemungkinan attrisi.

8. **Performa Model**: Model machine learning yang dikembangkan dapat memprediksi attrisi dengan akurasi 83%, namun masih memiliki keterbatasan dalam mendeteksi karyawan yang akan keluar (recall 18% untuk kelas 1).

## Rekomendasi Action Items

Berdasarkan analisis dan model prediktif, berikut adalah rekomendasi action items yang dapat dilakukan oleh departemen HR Jaya Jaya Maju:

1. **Program Retensi Karyawan Berdasarkan Departemen**
   * Mengembangkan program retensi khusus untuk departemen Research & Development dan Sales
   * Melakukan fokus group discussion untuk memahami masalah spesifik di departemen tersebut
   * Menyusun rencana perbaikan kondisi kerja berdasarkan feedback karyawan

2. **Review Kompensasi dan Benefit**
   * Melakukan benchmark gaji untuk posisi Laboratory Technician, Sales Executive, dan Research Scientist
   * Mengevaluasi struktur kompensasi untuk memastikan kompetitif di industri
   * Mempertimbangkan insentif tambahan atau bonus berdasarkan kinerja

3. **Meningkatkan Work-Life Balance**
   * Menerapkan kebijakan flexible working hours
   * Mengembangkan program wellness dan kesehatan mental
   * Mengevaluasi beban kerja di posisi dengan tingkat attrisi tinggi

4. **Program Pengembangan Karir**
   * Menciptakan jalur karir yang jelas untuk semua posisi
   * Mengadakan program mentorship dan coaching
   * Menyediakan pelatihan dan pengembangan kompetensi

5. **Implementasi Early Warning System**
   * Menerapkan sistem prediksi attrisi menggunakan model machine learning yang telah dikembangkan
   * Melakukan intervensi dini pada karyawan dengan risiko attrisi tinggi
   * Melakukan exit interview yang lebih terstruktur untuk memahami alasan pengunduran diri

6. **Evaluasi dan Pengembangan Kepemimpinan Manajerial**
   * Mengadakan pelatihan kepemimpinan untuk para manajer
   * Mengimplementasikan program feedback 360 derajat
   * Meningkatkan komunikasi antara karyawan dan manajemen

7. **Penyesuaian Kebijakan Transportasi dan Lokasi**
   * Menyediakan transportasi khusus untuk karyawan yang tinggal jauh dari kantor
   * Mempertimbangkan kebijakan work from home atau hybrid working untuk mengurangi beban jarak tempuh
   * Evaluasi kemungkinan subsidi transportasi tambahan

8. **Program Khusus untuk Karyawan Baru dan Junior**
   * Mengembangkan program onboarding dan mentoring yang lebih kuat
   * Memberikan perhatian khusus pada karyawan dengan masa kerja kurang dari 5 tahun
   * Membuat program pengembangan khusus untuk karyawan muda

Dengan mengimplementasikan rekomendasi di atas, Jaya Jaya Maju diharapkan dapat menurunkan tingkat attrisi karyawan hingga di bawah 7% dalam jangka waktu 12 bulan ke depan.