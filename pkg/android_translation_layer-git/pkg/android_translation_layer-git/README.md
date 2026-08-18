# Custom Android Translation Layer (ATL) - Advanced Anti-Detect & Spoofed Edition

---

## 🌍 ENGLISH VERSION

Proyek ini adalah repositori kustom untuk membangun versi modifikasi dari **Android Translation Layer (ATL)** secara native di distribusi Linux Arch-based (dioptimalkan khusus untuk **CachyOS x86_64** dengan **Kernel BORE** dan **COSMIC Desktop Environment**).

The main objective of this modification is to dismantle and bypass strict security enforcement systems inside modern Android applications (such as advanced encryption, anti-cheat engines, or device integrity checks) that typically block emulator environments or vanilla translation layers.

---

### 🚀 Advanced Modification Features (Bypass Architecture)

#### 1. Real-Time Low-Level JNI C Hooking Engine
High-security Android apps call low-level native libc bionic functions to sniff out the underlying system architecture. This modification intercepts these calls directly inside the heart of the \`src/api-impl-jni/util.c\` file by completely refactoring the native \`__system_property_get\` function.

Whenever an APK requests device specifications, our custom C engine hijacks the call and feeds it official **Google Pixel 6 (Raven)** metadata on the fly:
* \`ro.product.model\` → \`Pixel 6\`
* \`ro.product.brand\` → \`google\`
* \`ro.product.manufacturer\` → \`Google\`
* \`ro.product.device\` & \`ro.product.product\` → \`raven\`
* \`ro.build.tags\` → \`release-keys\` *(Hides custom build signatures)*
* \`ro.build.fingerprint\` → \`google/raven/raven:12/SP1A.210812.016/7701450:user/release-keys\`
* \`ro.secure\` = \`1\` & \`ro.debuggable\` = \`0\` *(Silences root status and active debugger detection)*
* **Emulator Memory Eraser**: Any other emulator-tracing system properties outside the defined whitelist are automatically returned as an empty string (\`\0\`), blinding the APK from discovering the true Linux backend.

#### 2. Telephony & Permission Bypass (PackageManager)
Our automation script injects logical bypasses during the compilation of the integrated Android framework. It forces \`hasSystemFeature\` for the \`android.hardware.telephony\` feature flag to always return \`true\`, and grants instant \`0\` (Granted) access status to the highly sensitive \`READ_PHONE_STATE\` permission.

#### 3. Modern Toolchain Mitigation (OpenJDK 26 Tolerance)
When building on cutting-edge rolling release systems like CachyOS utilizing **Java 26 / OpenJDK 26**, the upstream ATL build system crashes entirely (\`ninja: build stopped: subcommand failed\`) because the Ninja compiler treats old Java 8 source/target arguments as strictly obsolete.

This modification automates compiler tolerance flag injection into the \`meson.build\` configuration file and spawns a standalone *Javac Wrapper*:
\`\`\`bash
-Xlint:-options -Xlint:-rawtypes -Xlint:-unchecked
\`\`\`
This cleanly mutes 300+ strict-lint Java warnings without breaking the binary compilation chain.

---

### 🛠️ Python Patcher Engine Automation
To prevent escape character constraints on modern shell interpreters like **Fish Shell**, the C code patching process is dynamically processed via an external Python Regular Expression (Regex) engine script:

\`\`\`python
import re
pattern = r"int\s+__system_property_get\s*\([^)]*\)\s*\{"
# The regex safely pinpoints the exact original function declaration and inserts the C spoofing block at the top of the function body.
\`\`\`

---

### 📦 Local Build & Installation Guide

1. **Prepare Your Workspace & Extract Source Code:**
   \`\`\`bash
   mkdir -p $HOME/atl_pro && cd $HOME/atl_pro
   makepkg -od --noconfirm
   \`\`\`

2. **Run Injection & Compilation:**
   Execute the automated script provided in this repository to inject all structural bypasses into the code, then assemble the binary using the Arch Linux build utility:
   \`\`\`bash
   makepkg -efi --noconfirm
   \`\`\`

3. **Install the Resulting Package onto CachyOS:**
   \`\`\`bash
   sudo pacman -U *.pkg.tar.zst
   \`\`\`

---

### 🖥️ Graphics Rendering Optimization (Wayland/COSMIC)

If you notice applications (such as WhatsApp) rendering text as blank or stuck on a white/black screen due to *font rendering* bugs on Wayland, force ATL to use a stable fallback graphics rendering engine by injecting environment variables on launch:

\`\`\`bash
# Option 1: Force Cairo Software Rendering (Highly Stable for Text/Fonts)
env GSK_RENDERER=cairo android-translation-layer /path/to/app.apk

# Option 2: Force Next-Gen OpenGL Renderer
env GSK_RENDERER=ngl android-translation-layer /path/to/app.apk
\`\`\`

Ensure Android-compliant system fonts are installed globally on your Linux host:
\`\`\`bash
sudo pacman -S ttf-roboto noto-fonts && fc-cache -fv
\`\`\`

---
---

## 🇮🇩 TERJEMAHAN BAHASA INDONESIA

Proyek ini adalah repositori kustom untuk membangun versi modifikasi dari **Android Translation Layer (ATL)** secara native di distribusi Linux Arch-based (dioptimalkan khusus untuk **CachyOS x86_64** dengan **Kernel BORE** dan **COSMIC Desktop Environment**).

Tujuan utama dari modifikasi ini adalah membongkar dan menembus sistem keamanan ketat aplikasi Android modern (seperti enkripsi, anti-cheat, atau pengecekan integritas lingkungan) yang sering memblokir emulator atau layer translasi standar.

---

### 🚀 Fitur Unggulan Modifikasi (Bypass Architecture)

#### 1. Real-Time Low-Level JNI C Hooking Engine
Aplikasi Android dengan keamanan ketat memanggil fungsi native libc bionik untuk mengendus lingkungan sistem. Modifikasi ini melakukan **interupsi dinamis tepat di jantung file \`src/api-impl-jni/util.c\`** dengan merombak total fungsi \`__system_property_get\`.

Setiap kali APK memanggil sistem properti, engine C buatan kami akan langsung memotong dan menyuapi data **Google Pixel 6 (Raven)** resmi:
* \`ro.product.model\` → \`Pixel 6\`
* \`ro.product.brand\` → \`google\`
* \`ro.product.manufacturer\` → \`Google\`
* \`ro.product.device\` & \`ro.product.product\` → \`raven\`
* \`ro.build.tags\` → \`release-keys\` *(Menyamarkan status tanda tangan kustom build)*
* \`ro.build.fingerprint\` → \`google/raven/raven:12/SP1A.210812.016/7701450:user/release-keys\`
* \`ro.secure\` = \`1\` & \`ro.debuggable\` = \`0\` *(Membungkam deteksi status root/debugger)*
* **Emulator Memory Eraser**: Properti sistem pelacak emulator lain di luar daftar di atas akan otomatis dikembalikan sebagai string kosong (\`\0\`), membuat APK buta terhadap identitas asli Linux.

#### 2. Telephony & Permission Bypass (PackageManager)
Skrip otomatisasi kami menyuntikkan fungsi bypass logis pada level kompilasi framework Android bawaan untuk memaksa \`hasSystemFeature\` pada fitur \`android.hardware.telephony\` selalu bernilai \`true\`, serta memberikan hak akses instan \`0\` (Granted) pada izin sensitif \`READ_PHONE_STATE\`.

#### 3. Mitigasi Modern Toolchain (OpenJDK 26 Tolerance)
Saat dibangun di atas sistem mutakhir seperti CachyOS yang menggunakan **Java 26 / OpenJDK 26**, sistem kompilasi bawaan ATL akan mengalami macet total (*subcommand failure*) karena Ninja menganggap parameter Java 8 lama sudah usang (*obsolete*).

Modifikasi ini mengotomatiskan injeksi bendera toleransi compiler ke dalam file konfigurasi \`meson.build\` dan meluncurkan *Wrapper Javac* mandiri:
\`\`\`bash
-Xlint:-options -Xlint:-rawtypes -Xlint:-unchecked
\`\`\`
Ini membungkam 300+ peringatan *strict-lint* bawaan Java secara bersih tanpa memutus rantai perakitan biner.

---

### 🛠️ Cara Kerja Otomatisasi Script Penambal (Python Engine)
Untuk menghindari pembatasan karakter lepas (*escape character*) pada interpreter shell modern seperti **Fish Shell**, proses penambalan kode C dilakukan menggunakan mesin ekspresi reguler (Regex) Python eksternal secara dinamis:

\`\`\`python
import re
pattern = r"int\s+__system_property_get\s*\([^)]*\)\s*\{"
# Regex mendeteksi deklarasi fungsi asli lalu menyisipkan blok kode C spoofing tepat di baris atas tubuh fungsi
\`\`\`

---

### 📦 Panduan Kompilasi & Instalasi Lokal

1. **Persiapkan Lingkungan Kerja & Unduh Source Code:**
   \`\`\`bash
   mkdir -p $HOME/atl_pro && cd $HOME/atl_pro
   makepkg -od --noconfirm
   \`\`\`

2. **Jalankan Skrip Injeksi & Kompilasi:**
   Gunakan skrip otomatisasi yang berada di repositori ini untuk menyuntikkan seluruh bypass ke dalam source code, lalu rakit paket biner menggunakan utilitas Arch Linux:
   \`\`\`bash
   makepkg -efi --noconfirm
   \`\`\`

3. **Pasang Paket ke Sistem CachyOS Anda:**
   \`\`\`bash
   sudo pacman -U *.pkg.tar.zst
   \`\`\`

---

### 🖥️ Panduan Optimalisasi Render Grafis (Wayland/COSMIC)

Jika Anda mendapati tampilan aplikasi (seperti WhatsApp) mengalami *blank putih/hitam* karena bug pemrosesan huruf (*font rendering*) pada Wayland, paksa ATL menggunakan *fallback engine* grafis dengan menyuntikkan variabel lingkungan berikut saat meluncurkan APK:

\`\`\`bash
# Opsi 1: Menggunakan rendering perangkat lunak Cairo (Sangat Stabil untuk Teks)
env GSK_RENDERER=cairo android-translation-layer /path/ke/aplikasi.apk

# Opsi 2: Menggunakan Next-Gen OpenGL Renderer
env GSK_RENDERER=ngl android-translation-layer /path/ke/aplikasi.apk
\`\`\`

Pastikan juga font sistem Android telah terpasang di Linux Anda:
\`\`\`bash
sudo pacman -S ttf-roboto noto-fonts && fc-cache -fv
\`\`\`

---

## ⚖️ License / Lisensi
Distribusi ulang dan modifikasi tunduk pada lisensi sumber asli ATL.
