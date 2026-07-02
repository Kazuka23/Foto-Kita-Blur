# ✌️ Foto Kita Blur: Hand Gesture Blur Cam

> Waktu itu fyp gw isinya trend "foto kita blur semua", terus yang menarik ada yang bikin pake python, tapi pas gw cari code pythonnya gaada yang ngasih, alhasil gw coba bikin. Logika nya sederhana, kalo ada isyarat jari atau ada pose dari tangan dan terdeteksi pake anatomi webcam otomatis blur. Sebaliknya, kalo anatomi ga ngedeteksi ada jari atau pose ya webcam jernih.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11.9-blue?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.9-orange)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Mac%20%7C%20Linux-lightgrey)

**Creator: [Kazuka23](https://github.com/Kazuka23)**

</div>

---

## 📖 Tentang Project Ini

"Foto Kita Blur" adalah tren viral TikTok di mana layar kamera seseorang akan blur saat mereka mengangkat jari, dan kembali jernih saat tangan diturunkan. Project ini mengimplementasikan tren tersebut secara nyata menggunakan **OpenCV** untuk pemrosesan gambar dan **MediaPipe Hands** untuk deteksi landmark tangan secara real-time.

---

## ✨ Fitur

- **Blur otomatis berbasis gesture** — layar blur saat jari terdeteksi terangkat, jernih saat tidak ada tangan
- **Visualisasi kerangka tangan (hand skeleton)** — titik sendi (biru) dan tulang (hijau) tergambar real-time di atas frame
- **Penghitungan jari dinamis** — mendeteksi semua 5 jari termasuk jempol dengan logika koordinat landmark
- **Optimasi performa** — resolusi proses terpisah dari resolusi tampilan agar tetap ringan
- **Mirror effect** — tampilan di-flip otomatis agar natural seperti kamera depan

---

## 🛠️ Prasyarat

Sebelum mulai, pastikan kamu punya:
- Laptop/PC dengan webcam
- Koneksi internet (untuk download installer dan library)
- **Python 3.11.9** — versi ini wajib, jangan pakai yang lebih baru (alasannya dijelaskan di bagian instalasi)

---

## 🚀 Instalasi & Cara Pakai

### Langkah 1 — Install Python 3.11.9

> ⚠️ **Kenapa harus 3.11.9?** MediaPipe versi stabil (`0.10.9`) hanya tersedia untuk Python 3.9–3.11. Jika kamu pakai Python 3.12 ke atas, versi mediapipe yang bisa ter-install adalah 0.10.30–0.10.35, dan semua versi itu punya bug `AttributeError: module 'mediapipe' has no attribute 'solutions'` yang belum diperbaiki. Jadi skip versi terbaru, pakai 3.11.9.

1. Download installer dari link resmi ini:
   **[⬇️ Download Python 3.11.9 (Windows 64-bit)](https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe)**

2. Jalankan file `.exe` yang sudah didownload.

3. **PENTING — jangan langsung klik Install Now.** Di halaman pertama installer, **centang dulu** checkbox:
   ```
   ☑ Add python.exe to PATH
   ```
   Ini sering kelewat dan bikin masalah kalau lupa.

4. Pilih **"Customize installation"**, klik Next di halaman Optional Features (biarkan default).

5. Di halaman Advanced Options, centang:
   ```
   ☑ Add Python to environment variables
   ```

6. Klik **Install**, tunggu selesai, lalu klik **Close**.

7. Verifikasi instalasi berhasil — buka terminal baru lalu ketik:
   ```
   py -0
   ```
   Harus muncul `Python 3.11` di list. Kalau sudah ada, lanjut ke langkah berikutnya.

---

### Langkah 2 — Clone atau Download Repository Ini

Pilih salah satu:

**Opsi A — Pakai Git:**
```bash
git clone https://github.com/Kazuka23/foto-kita-blur.git
cd foto-kita-blur
```

**Opsi B — Download ZIP:**
Klik tombol **Code → Download ZIP** di halaman repository ini, lalu ekstrak, lalu buka foldernya di VS Code (`File > Open Folder`).

---

### Langkah 3 — Buat Virtual Environment

Virtual environment berguna agar library project ini tidak bertabrakan dengan project Python lain di laptopmu.

Buka terminal di VS Code (`Ctrl + `` ` ``  atau `Terminal > New Terminal`). Pastikan terminal sudah menunjuk ke folder project. Lalu jalankan:

```powershell
py -3.11 -m venv venv
```

Perintah ini akan membuat folder `venv` di dalam folder project. Setelah itu, aktifkan:

```powershell
venv\Scripts\activate
```

**Kalau muncul error merah seperti ini:**
```
...cannot be loaded because running scripts is disabled on this system...
```
Itu artinya PowerShell Windows kamu memblokir eksekusi script. Jalankan perintah ini dulu:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Ketik `Y` lalu Enter saat diminta konfirmasi. Setelah itu ulangi perintah activate di atas.

**Tanda berhasil:** di awal baris terminal akan muncul `(venv)`:
```
(venv) PS C:\...\foto-kita-blur>
```

---

### Langkah 4 — Pilih Interpreter di VS Code

Agar VS Code tahu harus pakai Python dari `venv` (bukan Python global):

1. Tekan `Ctrl+Shift+P`
2. Ketik: `Python: Select Interpreter`
3. Pilih opsi yang ada tulisan `('venv': venv)` dan versinya `3.11.9`

Kalau sudah terpilih, di status bar bawah VS Code akan tertulis: `Python 3.11.9 ('venv': venv)`

---

### Langkah 5 — Install Library

Pastikan `(venv)` masih aktif di terminal, lalu jalankan:

```powershell
pip install opencv-python mediapipe==0.10.9
```

> ⚠️ **Kenapa `mediapipe==0.10.9`?** Wajib cantumkan versi spesifiknya. Tanpa `==0.10.9`, pip akan otomatis install versi terbaru yang punya bug `solutions` seperti yang dijelaskan di Langkah 1. Versi `0.10.9` adalah versi yang sudah terbukti stabil untuk project ini.

Tunggu hingga semua selesai terunduh dan terinstall (mediapipe cukup besar, sekitar 50–100 MB). Setelah selesai, verifikasi:

```powershell
pip list
```

Pastikan ada baris `opencv-python` dan `mediapipe 0.10.9` di dalam list.

---

### Langkah 6 — Sesuaikan Indeks Kamera (Jika Perlu)

Buka file `foto_kita_blur.py`, lihat baris paling atas:

```python
CAMERA_INDEX = 0
```

- `0` → biasanya webcam bawaan laptop
- `1` → kamera eksternal/USB

Kalau program jalan tapi kamera yang terbuka bukan yang kamu mau, coba ganti angkanya satu per satu sampai ketemu yang benar.

---

### Langkah 7 — Jalankan Program

```powershell
python foto_kita_blur.py
```

Atau klik tombol **▶ (Run)** di pojok kanan atas VS Code.

Jendela kamera bertuliskan **"TikTok Trend: Foto Kita Blur"** akan muncul.

**Cara pakainya:**
- Default: layar **jernih**
- Angkat jari ke arah kamera → layar **blur + kerangka tangan muncul**
- Turunkan tangan → layar **kembali jernih**
- Tekan `Q` di keyboard untuk keluar

---

## ⚙️ Cara Kerja Singkat

| Tahap | Penjelasan |
|---|---|
| **1. Capture** | Kamera menangkap frame video secara terus-menerus lalu di-flip (mirror effect) |
| **2. Resize** | Frame dikecilkan ke 320×240 untuk proses agar lebih ringan di CPU |
| **3. Deteksi** | MediaPipe memproses frame dan menghasilkan 21 titik landmark per tangan |
| **4. Hitung jari** | Koordinat Y ujung jari dibandingkan dengan sendi di bawahnya — jika lebih tinggi, jari dianggap terangkat |
| **5. Blur** | Jika ada jari terangkat (`raised_count > 0`), Gaussian Blur diterapkan ke frame |
| **6. Skeleton** | Titik sendi (biru) dan koneksi antar sendi (hijau) digambar di atas frame hasil akhir |
| **7. Tampil** | Frame ditampilkan di resolusi 640×480 |

---

## 🐛 Troubleshooting

| Masalah | Solusi |
|---|---|
| `ModuleNotFoundError: No module named 'cv2'` | Interpreter VS Code belum menunjuk ke `venv`. Ulangi Langkah 4. |
| `AttributeError: module 'mediapipe' has no attribute 'solutions'` | Versi mediapipe salah. Jalankan: `pip uninstall mediapipe -y` lalu `pip install mediapipe==0.10.9` |
| Jendela kamera tidak muncul / langsung crash | `CAMERA_INDEX` salah. Coba ganti ke `1` atau `2`. |
| `venv\Scripts\activate` error merah | Jalankan `Set-ExecutionPolicy` dulu (lihat Langkah 3). |
| Deteksi tangan lambat atau tidak akurat | Pastikan pencahayaan ruangan cukup dan tangan tidak terpotong di tepi layar. |

---

## 📦 Dependensi

```
opencv-python
mediapipe==0.10.9
```

---

## 👤 Creator

**Kazuka23**
[github.com/Kazuka23](https://github.com/Kazuka23)

---

## ☕ Dukung Project Ini

Kalau project ini bermanfaat buat kamu, kamu bisa support via:

[![Saweria](https://img.shields.io/badge/Donate-Saweria-orange?style=for-the-badge)](https://saweria.co/siryagami)

---

<div align="center">

Made with ❤️ by [Kazuka23](https://github.com/Kazuka23)

</div>
