# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju

## Business Understanding

Latar Belakang Bisnis

Jaya Jaya Maju adalah sebuah perusahaan multinasional yang didirikan pada tahun 2000 dan kini memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. Seiring dengan perkembangan yang pesat dan skala operasional yang semakin besar, perusahaan ini menghadapi tantangan signifikan dalam mengelola karyawan, salah satunya adalah tingginya tingkat attrition atau perputaran karyawan.

Attrition rate yang tinggi, yang mencapai lebih dari 10%, menunjukkan bahwa banyak karyawan yang meninggalkan perusahaan. Hal ini tentunya dapat menambah beban biaya perekrutan dan pelatihan karyawan baru, serta mengganggu kontinuitas operasional perusahaan. Untuk itu, manajemen perusahaan, khususnya departemen HR, ingin mengetahui lebih dalam faktor-faktor yang mempengaruhi keputusan karyawan untuk keluar dan mengurangi tingkat attrition agar dapat mempertahankan tenaga kerja yang lebih stabil dan berkompeten.

### Permasalahan Bisnis

Berikut adalah permasalahan bisnis yang ingin diselesaikan oleh perusahaan:

1. Tingginya Tingkat Attrition (Perputaran Karyawan):
Dengan tingkat attrition lebih dari 10%, perusahaan menghadapi biaya tinggi terkait proses perekrutan, pelatihan, serta kehilangan pengalaman dan pengetahuan yang dimiliki oleh karyawan yang keluar. Identifikasi faktor-faktor yang berhubungan dengan attrition diperlukan untuk merumuskan strategi retensi yang lebih efektif.

2. Identifikasi Faktor Penyebab Attrition:
Perusahaan membutuhkan pemahaman yang lebih mendalam mengenai faktor-faktor yang memengaruhi keputusan karyawan untuk keluar. Beberapa faktor yang bisa mempengaruhi attrition meliputi:

- Faktor Demografis: Usia, jenis kelamin, status pernikahan.
- Faktor Pekerjaan: Kepuasan kerja, keterlibatan dalam pekerjaan, gaji, tingkat pekerjaan, jam kerja, peluang promosi, dan keseimbangan kerja-hidup.
- Faktor Lingkungan Kerja: Kepuasan lingkungan, hubungan dengan manajer, dan tingkat beban kerja.

3. Peningkatan Retensi Karyawan:
Dengan mengetahui faktor-faktor yang mempengaruhi attrition, perusahaan diharapkan dapat mengambil langkah-langkah untuk meningkatkan retensi karyawan, seperti melakukan intervensi terhadap kondisi kerja yang tidak menguntungkan atau memberikan insentif bagi karyawan yang memiliki potensi tinggi untuk tetap berada di perusahaan.

4. Pembuatan Dashboard Bisnis:
Untuk memantau dan mengelola masalah-masalah ini secara lebih efisien, manajer HR menginginkan adanya dashboard bisnis yang dapat memberikan informasi real-time mengenai berbagai faktor yang memengaruhi attrition. Dashboard ini diharapkan dapat memberikan gambaran yang jelas dan komprehensif tentang kesehatan karyawan, tingkat kepuasan kerja, dan faktor-faktor risiko yang berpotensi meningkatkan attrition.

Dengan fokus pada analisis data karyawan yang tersedia, perusahaan akan dapat mengembangkan kebijakan yang lebih berbasis data dan strategi yang lebih terfokus untuk meningkatkan retensi karyawan dan mengurangi perputaran karyawan yang tinggi.

### Cakupan Proyek

Proyek ini akan berfokus pada analisis faktor-faktor yang memengaruhi tingkat attrition atau perputaran karyawan di perusahaan Jaya Jaya Maju. Berdasarkan analisis ini, tujuan akhir adalah untuk mengidentifikasi faktor-faktor utama yang berkontribusi terhadap keputusan karyawan untuk keluar, serta menyediakan solusi berbasis data untuk meningkatkan retensi karyawan. Berikut adalah cakupan proyek secara lebih rinci:

1. Eksplorasi dan Pembersihan Data

- Mengimpor dan melakukan pembersihan data untuk memastikan kualitas data yang baik.
- Menangani nilai yang hilang, outliers, dan data yang tidak konsisten.
- Mengonversi variabel kategorikal menjadi variabel numerik (misalnya, encoding) untuk analisis lebih lanjut.

2. Analisis Deskriptif

- Melakukan analisis statistik dasar untuk memahami distribusi data dan menemukan pola dasar.
- Mengidentifikasi tren dalam data seperti perbedaan attrition antara berbagai departemen, tingkat kepuasan kerja, umur karyawan, status pernikahan, dll.
- Menyajikan visualisasi data (misalnya, histogram, boxplot, pie chart) untuk menggambarkan distribusi dan hubungan antar fitur.

3. Analisis Faktor Penyebab Attrition

- Mengidentifikasi faktor-faktor yang signifikan yang mempengaruhi keputusan karyawan untuk keluar (attrition).
- Menggunakan teknik analisis korelasi untuk menemukan hubungan antara variabel karyawan dan status attrition.
- Membangun model prediksi untuk mengidentifikasi karyawan yang berisiko tinggi mengalami attrition.

4. Pembuatan Model Prediksi

- Menggunakan algoritma machine learning (adaboost) untuk membangun model yang dapat memprediksi kemungkinan karyawan akan mengalami attrition berdasarkan data demografis dan pekerjaan mereka.
- Melakukan evaluasi model menggunakan metrik seperti akurasi, precision, recall, dan F1-score untuk menentukan efektivitas model.

5. Pengembangan Business Dashboard

- Membuat dashboard interaktif menggunakan Looker studio untuk memantau faktor-faktor yang mempengaruhi attrition secara real-time.
- Menyajikan visualisasi yang mudah dipahami untuk manajer HR mengenai tingkat attrition, faktor-faktor risiko, distribusi gaji, kepuasan kerja, dan lainnya.
- Memfasilitasi pembuatan keputusan berbasis data untuk strategi retensi karyawan.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee

Setup environment:

Untuk menjalankan dashboard ini, Anda memerlukan lingkungan pengembangan Python dengan beberapa library yang sudah disiapkan. Berikut adalah langkah-langkah untuk menyiapkan environment:

1. **Clone Repository**

   Pertama, clone repository ini ke komputer lokal Anda.

   ```bash
   git clone https://github.com/zzazzz/Belajar-Penerapan-Data-Science.git
   cd Belajar-Penerapan-Data-Science

2. **Install Dependencies**

   Pastikan Anda telah menginstal semua dependensi yang dibutuhkan. Anda dapat menggunakan `requirements.txt` untuk menginstal semua library yang diperlukan.

   ```bash
   pip install -r requirements.txt
   ```

3. **Run Dashboard**

   Setelah menginstal dependensi, jalankan dashboard menggunakan Streamlit.

   ```bash
   streamlit run app.py
   ```

   atau terdapat pada https://lookerstudio.google.com/reporting/c476c471-6ebb-477a-97f4-a5e143a25414

## Business Dashboard

Dashboard ini berfokus pada analisis attrition karyawan dan faktor-faktor yang mempengaruhinya. Berikut adalah penjelasan singkat dari **18 pertanyaan** yang digunakan dalam dashboard ini:

1. Perbandingan Karyawan Aktif dan Keluar
Menampilkan jumlah karyawan yang masih aktif dan yang telah keluar untuk memahami tren **attrition** secara keseluruhan.

2. Karyawan yang Keluar Berdasarkan Gender
Mengidentifikasi perbedaan tingkat pengunduran diri antara karyawan pria dan wanita.

3. Attrition Berdasarkan Business Travel
Menunjukkan hubungan antara karyawan yang sering melakukan perjalanan bisnis dan tingkat **attrition** mereka.

4. Pengaruh Jarak Dari Rumah Terhadap Attrition
Menganalisis apakah jarak dari rumah mempengaruhi keputusan pengunduran diri karyawan.

5. Perbandingan Attrition Berdasarkan Departemen
Mengidentifikasi departemen mana yang memiliki tingkat **attrition** tertinggi.

6. Jumlah Attrition Berdasarkan Peran Pekerjaan
Menunjukkan tingkat **attrition** berdasarkan jabatan atau peran pekerjaan karyawan.

7. Distribusi Usia Berdasarkan Status Attrition
Menganalisis perbedaan distribusi usia antara karyawan yang keluar dan yang tetap bekerja.

8. Distribusi Penghasilan Bulanan Berdasarkan Status Attrition
Menganalisis hubungan antara penghasilan bulanan dan keputusan **attrition** karyawan.

9. Hubungan Penghasilan Bulanan dan Tarif Per Jam Berdasarkan Status Attrition dan Departemen
Mengidentifikasi apakah ada hubungan antara penghasilan dan tarif per jam yang mempengaruhi **attrition**.

10. Attrition Berdasarkan Bidang Pendidikan
Menunjukkan hubungan antara tingkat pendidikan karyawan dan **attrition**.

11. Attrition Berdasarkan Status Lembur
Menganalisis apakah bekerja lembur berhubungan dengan keputusan pengunduran diri karyawan.

12. Attrition Berdasarkan Work-Life Balance
Menilai dampak keseimbangan kehidupan kerja terhadap **attrition** karyawan.

13. Attrition Berdasarkan Status Overtime
Menganalisis apakah status lembur (bekerja lebih banyak dari waktu normal) berhubungan dengan **attrition**.

14. Attrition Berdasarkan Kepuasan Lingkungan Kerja
Mengidentifikasi apakah tingkat kepuasan terhadap lingkungan kerja mempengaruhi pengunduran diri.

15. Attrition Berdasarkan Kepuasan Kerja
Menganalisis hubungan antara kepuasan kerja dan **attrition**.

16. Distribusi Pengalaman Kerja untuk Karyawan yang Keluar dan Tetap
Menunjukkan sebaran pengalaman kerja antara karyawan yang mengundurkan diri dan yang tetap bekerja.

17. Perbandingan Attrition Berdasarkan Pengalaman Kerja (Total Tahun Bekerja)
Mengidentifikasi apakah pengalaman kerja mempengaruhi keputusan pengunduran diri.

18. Jumlah Attrition Berdasarkan Tingkat Pendidikan
Menganalisis hubungan antara tingkat pendidikan karyawan dan tingkat **attrition**.

# Employee Attrition Analysis Dashboard

## Conclusion

Berdasarkan hasil analisis yang ditampilkan pada dashboard, berikut adalah beberapa kesimpulan utama terkait faktor-faktor yang memengaruhi **attrition** karyawan di perusahaan:

1. **Attrition Rate**: Perusahaan memiliki attrition rate sebesar **16,93%** dengan jumlah karyawan yang keluar sebanyak 179 dari total 1.058 karyawan.
2. **Gender**: Karyawan pria memiliki tingkat pengunduran diri lebih tinggi dibandingkan wanita, dengan jumlah pria yang keluar sebanyak **108** orang.
3. **Business Travel**: Karyawan yang jarang melakukan perjalanan bisnis lebih cenderung keluar dibandingkan karyawan yang sering bepergian.
4. **Distance from Home**: Jarak rumah ke kantor memengaruhi **attrition**, dengan mayoritas karyawan yang keluar tinggal dalam jarak **0–4 km** dari kantor.
5. **Department**: Departemen **Research and Development (RnD)** memiliki tingkat **attrition** tertinggi.
6. **Job Role**: Jabatan **Laboratory Technician** memiliki jumlah karyawan keluar terbanyak.
7. **Age Distribution**: Karyawan yang keluar umumnya berada dalam rentang usia **28–29 tahun**.
8. **Monthly Income**: Karyawan dengan penghasilan bulanan sekitar **2000–2999** lebih banyak yang mengundurkan diri.
9. **Hourly Rate and Department**: Pada departemen **RnD**, karyawan dengan penghasilan bulanan dan tarif per jam terendah memiliki kecenderungan keluar lebih tinggi.
10. **Education Field**: Bidang pendidikan **Technical Degree** memiliki tingkat **attrition** tertinggi.
11. **Overtime Status**: Karyawan yang bekerja lembur memiliki risiko keluar lebih tinggi.
12. **Work-Life Balance**: Karyawan dengan tingkat **work-life balance** rendah cenderung keluar.
13. **Environment Satisfaction**: Karyawan dengan tingkat kepuasan lingkungan terendah memiliki attrition rate sebesar **27%**.
14. **Job Satisfaction**: Attrition rate tertinggi terjadi pada karyawan dengan tingkat kepuasan kerja terendah, yaitu **22%**.
15. **Years at Company**: Karyawan yang keluar umumnya memiliki pengalaman bekerja **0–4 tahun** di perusahaan.
16. **Years of Experience**: Karyawan yang keluar rata-rata memiliki pengalaman kerja **1 tahun**.
17. **Education Level**: Sebagian besar karyawan yang keluar memiliki tingkat pendidikan **Sarjana**.
18. **Education Background**: Tingkat **attrition** juga dipengaruhi oleh latar belakang pendidikan, dengan bidang pendidikan **Technical Degree** memiliki jumlah karyawan keluar tertinggi.

### Rekomendasi Action Items

Untuk mengatasi permasalahan **attrition** dan meningkatkan retensi karyawan, perusahaan dapat mempertimbangkan langkah-langkah berikut:

- **Evaluasi Work-Life Balance**: Tingkatkan program keseimbangan kehidupan kerja, seperti kebijakan jam kerja fleksibel atau dukungan kerja jarak jauh.
- **Meningkatkan Kepuasan Lingkungan dan Pekerjaan**: Sediakan lingkungan kerja yang kondusif dengan mengidentifikasi dan mengatasi masalah karyawan melalui survei kepuasan rutin.
- **Revisi Sistem Lembur**: Kurangi beban lembur dan pastikan kompensasi yang sesuai bagi karyawan yang bekerja di luar jam normal.
- **Program Pengembangan untuk Karyawan Baru**: Fokus pada pengembangan dan retensi karyawan dengan pengalaman kerja rendah melalui pelatihan, mentoring, atau program onboarding yang lebih baik.
- **Penyesuaian Gaji**: Tinjau kembali struktur gaji, khususnya untuk karyawan di departemen dengan penghasilan rendah, guna mengurangi risiko pengunduran diri.
- **Fokus pada Departemen RnD**: Identifikasi masalah spesifik di departemen RnD yang menyebabkan tingkat **attrition** tinggi dan implementasikan solusi yang relevan.

Dengan mengimplementasikan langkah-langkah di atas, perusahaan dapat mengurangi tingkat **attrition**, meningkatkan retensi, dan menciptakan lingkungan kerja yang lebih baik bagi karyawan.

