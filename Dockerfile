# Menggunakan base image Python resmi dengan versi 3.9
FROM python:3.10

# Menetapkan direktori kerja dalam container
WORKDIR /app

# Menetapkan variabel lingkungan untuk port
ENV PORT 8080

# Menambahkan dependensi yang diperlukan untuk menggunakan wget
RUN apt-get update && apt-get install -y wget

# Mengunduh file
RUN wget -O MT.h5 https://storage.googleapis.com/tabi-translate/TextToText/MT.h5
RUN wget -O input_tokenizer.pkl https://storage.googleapis.com/tabi-translate/TextToText/input_tokenizer.pkl
RUN wget -O output_tokenizer.pkl https://storage.googleapis.com/tabi-translate/TextToText/output_tokenizer.pkl

# Menyalin semua file dari direktori lokal ke direktori kerja dalam container
COPY . .

# Menginstal semua dependensi yang ada di requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Membuka port yang akan digunakan oleh aplikasi
EXPOSE 8080

# Menjalankan aplikasi saat container dimulai
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
