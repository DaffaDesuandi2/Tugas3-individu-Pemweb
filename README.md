# Product Review Analyzer with AI (Sentiment & Key Points)

Aplikasi analisis ulasan produk menggunakan **FastAPI** (Backend), **React + Vite** (Frontend), dan **PostgreSQL** sebagai database. Aplikasi ini menggunakan model AI dari **Hugging Face** untuk melakukan klasifikasi sentimen dan ekstraksi poin-poin penting secara otomatis.

## 🚀 Fitur Utama
* **Analisis Sentimen**: Mendeteksi apakah ulasan bernada POSITIVE atau NEGATIVE.
* **Ekstraksi Key Points**: Merangkum poin penting dari ulasan produk.
* **Penyimpanan Database**: Semua ulasan dan hasil analisis disimpan di PostgreSQL.
* **Tampilan Modern**: Interface responsif menggunakan React dan CSS.

## 📁 Struktur Folder
* `backend/`: Berisi API FastAPI, file database (`models.py`, `database.py`), dan logika AI.
* `frontend/`: Berisi dashboard React menggunakan Vite.

---

## 🛠️ Langkah Instalasi

### 1. Persiapan Database (PostgreSQL)
1. Buka **pgAdmin 4** atau terminal PostgreSQL.
2. Buat database baru bernama `product_review_db`.
3. Pastikan PostgreSQL berjalan di port `5432`.

### 2. Konfigurasi Backend
1. Masuk ke folder backend:
   ```bash
   cd backend
### 3. Install library yang dibutuhkan
python -m pip install fastapi uvicorn sqlalchemy psycopg2-binary requests python-dotenv httpx

### 4. Buat file .env di dalam folder backend dan masukkan API Key Hugging Face Anda
HUGGINGFACE_API_KEY=your_hf_token_here
### 5. Jalankan Frontend
cd frontend
npm run dev
