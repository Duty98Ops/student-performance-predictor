import streamlit as st
import pandas as pd
import joblib

st.title("Prediksi Performa Akademik Siswa")

pipeline = joblib.load('model/pipeline.pkl')

race_map = {
    "Kelompok Sosial 1 (Kurang Mampu)": "group A",
    "Kelompok Sosial 2": "group B",
    "Kelompok Sosial 3 (Menengah)": "group C",
    "Kelompok Sosial 4": "group D",
    "Kelompok Sosial 5 (Mampu)": "group E"
}

lunch_map = {
    "Standar": "standard",
    "Gratis / Diskon": "free/reduced"
}

test_prep_map = {
    "Tidak Ikut Pelatihan": "none",
    "Sudah Ikut Pelatihan": "completed"
}

gender = st.selectbox("Jenis Kelamin", ['', 'female', 'male'])
race_label = st.selectbox("Kelompok Sosial (Race/Ethnicity)", [''] + list(race_map.keys()))
lunch_label = st.selectbox("Jenis Makan Siang (Lunch)", [''] + list(lunch_map.keys()))
test_prep_label = st.selectbox("Pelatihan Persiapan Ujian", [''] + list(test_prep_map.keys()))
parental_education = st.selectbox("Pendidikan Orang Tua", ['',
    "some high school", "high school", "some college", "associate's degree",
    "bachelor's degree", "master's degree"
])

# Gunakan float dengan step 0.1 supaya bisa input desimal
math_score = st.number_input("Nilai Matematika", min_value=0.0, max_value=100.0, step=0.1, format="%.1f", value=0.0)
reading_score = st.number_input("Nilai Membaca", min_value=0.0, max_value=100.0, step=0.1, format="%.1f", value=0.0)
writing_score = st.number_input("Nilai Menulis", min_value=0.0, max_value=100.0, step=0.1, format="%.1f", value=0.0)

if st.button("Prediksi"):
    # Cek input wajib, selain nilai numerik karena 0 itu valid
    if (gender == '' or race_label == '' or lunch_label == '' or test_prep_label == '' or parental_education == ''):
        st.error("Mohon isi semua input pilihan dengan benar!")
    else:
        # Kalau input nilai = 0, tetap valid, tidak perlu error
        race_ethnicity = race_map[race_label]
        lunch = lunch_map[lunch_label]
        test_prep = test_prep_map[test_prep_label]

        input_df = pd.DataFrame({
            'gender': [gender],
            'race/ethnicity': [race_ethnicity],
            'parental level of education': [parental_education],
            'lunch': [lunch],
            'test preparation course': [test_prep],
            'math score': [math_score],
            'reading score': [reading_score],
            'writing score': [writing_score]
        })

        try:
            pred = pipeline.predict(input_df)[0]
            proba = pipeline.predict_proba(input_df)[0][1]

            status = "Lulus" if pred == 1 else "Tidak Lulus"

            st.success(f"Prediksi: **{status}**")
            st.write(f"Probabilitas prediksi lulus: **{proba:.2f}**")
        except Exception as e:
            st.error(f"Terjadi kesalahan saat prediksi: {e}")
