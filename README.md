# RagaMaya ML Service

<div align="center">
<img src="https://cdn.xann.my.id/ragamaya/59d42d65-43ee-4cc3-ba98-a1ae341d3a78.png" alt="Logo RagaMaya" width="200"/>
<h3>Temukan Makna, Hidupkan Budaya, Bersama RagaMaya</h3>

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Docker](https://img.shields.io/badge/Docker-latest-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)
[![Flask](https://img.shields.io/badge/Flask-latest-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)

</div>

## 📖 Tentang

RagaMaya ML Service adalah komponen penting dari platform RagaMaya yang menyediakan layanan machine learning untuk menganalisis dan mengklasifikasikan motif batik. Layanan ini dibangun menggunakan Python dan TensorFlow untuk memberikan kemampuan pengenalan pola batik yang akurat dan efisien.

🌐 **Bagian dari platform: [ragamaya.space](https://ragamaya.space)**

Service ini menggunakan model deep learning yang telah dilatih khusus untuk mengenali berbagai motif batik Indonesia, mendukung fitur utama platform RagaMaya dalam pelestarian dan edukasi tentang batik.

## 🚀 Fitur

- Klasifikasi Motif Batik
- Model Deep Learning Terlatih
- REST API Endpoint
- Docker Support
- Integrasi dengan RagaMaya Backend
- Jupyter Notebook untuk Training dan Evaluasi Model

## 🛠️ Teknologi yang Digunakan

- **Bahasa Pemrograman:** Python
- **Framework ML:** TensorFlow
- **Web Framework:** Flask
- **Notebook:** Jupyter Notebook
- **Kontainerisasi:** Docker
- **Model Format:** HDF5

## 🚀 Cara Memulai

1. Clone repositori
```bash
git clone https://github.com/RagaMaya/ragamaya-ml.git
```

2. Install dependensi
```bash
pip install -r requirements.txt
```

3. Jalankan aplikasi
```bash
python app.py
```

Atau menggunakan Docker:
```bash
docker build -t ragamaya-ml .
docker run -p 5000:5000 ragamaya-ml
```

## 📁 Struktur Proyek

```
.
├── app.py           # Aplikasi utama Flask
├── Dockerfile       # Konfigurasi Docker
├── requirements.txt # Dependensi Python
├── Batik.ipynb     # Notebook untuk training dan evaluasi model
└── models/         # Model ML
    └── batik_model.h5
```

## 📄 Lisensi

Proyek ini dilisensikan di bawah ketentuan lisensi yang disediakan dalam repositori.

## 👥 Kontributor

### Tim Pengembangan
- [Rama Diaz](https://github.com/ramadiaz) - Backend Developer
- [Fahry Firdaus](https://github.com/Fahry169) - Frontend Developer
- [Kevin Sipahutar](https://github.com/vinss-droid) - Machine Learning Engineer & Frontend Developer

---

<div align="center">
<p>© 2025 RagaMaya. Semua Hak Dilindungi.</p>
</div>
