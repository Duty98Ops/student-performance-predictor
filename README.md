# Student Performance Predictor

Aplikasi prediksi performa akademik siswa berbasis machine learning dengan antarmuka Streamlit. Model memanfaatkan data demografi dan nilai ujian siswa untuk memprediksi kelulusan.

---

## 🚀 Key Features

* Input data siswa dengan label yang mudah dimengerti
* Validasi nilai ujian (0-100)
* Prediksi kelulusan dan probabilitas secara real-time
* Model Random Forest yang sudah terlatih dan siap pakai
* Preprocessing otomatis dengan pipeline terintegrasi
* Antarmuka user-friendly dan sesuai konteks Indonesia

---

## 🛠️ Technology Stack

* Python (pandas, scikit-learn, joblib)
* Streamlit (web UI)
* Machine Learning: Random Forest Classifier
* Serialization: joblib

---

## 🔧 Setup & Installation

Clone repo:

```bash
git clone https://github.com/Duty98Ops/student-performance-predictor.git
cd student-performance-predictor
```

Buat virtual environment dan aktifkan:

```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Jalankan aplikasi Streamlit:

```bash
streamlit run app.py
```

---

## ⚙️ Usage

Isi formulir input data siswa dengan nilai dan informasi yang valid. Tekan tombol **Prediksi** untuk mendapatkan hasil kelulusan beserta probabilitasnya.

---

## 📊 Dataset

Dataset yang digunakan adalah **Student Performance Dataset**, yang juga tersedia di Kaggle:
[https://www.kaggle.com/datasets/spscientist/students-performance-in-exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)

---

## 📈 Data & Model Details

**Fitur Input:**

* gender
* race/ethnicity (Kelompok Sosial)
* parental level of education
* lunch (Jenis Makan Siang)
* test preparation course (Pelatihan Persiapan Ujian)
* math score, reading score, writing score (nilai 0-100)

**Model:**

* Algoritma: Random Forest Classifier
* Akurasi: \~98% pada data uji
* Preprocessing: OneHotEncoder & ColumnTransformer

---

## ⚠️ Common Issues & Solutions

| Issue                                  | Cause                         | Solution                                   |
| -------------------------------------- | ----------------------------- | ------------------------------------------ |
| Error input nilai melebihi batas 0-100 | Input tidak divalidasi        | Masukkan nilai antara 0 dan 100            |
| Model error saat prediksi              | Input dataframe tidak lengkap | Pastikan semua kolom terisi                |
| Aplikasi tidak jalan                   | Dependensi belum terinstall   | Jalankan `pip install -r requirements.txt` |

---

## 🔗 Links

Hugging Face Repository: 
https://huggingface.co/spaces/Elvern/student-performance-predictor

