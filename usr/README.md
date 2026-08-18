# Custom /usr System Directory (ATL)

Folder ini berisi modifikasi pada hierarki sistem \`/usr\` yang disesuaikan untuk **Android Translation Layer (ATL) Spoofed Edition**. 

## 📂 Struktur Direktori

* **\`usr/bin/\`** : Memuat eksekusi biner utama yang telah ditambal.
* **\`usr/lib/\`** : Memuat pustaka asli (*native libraries*) dan framework Android (file DEX, \`api-impl.jar\`, \`framework-res.apk\`) yang telah diinjeksi dengan instruksi bypass *telephony* dan *property spoofing*.
* **\`usr/share/\`** : Konfigurasi font tambahan dan aset sistem untuk peredam *glitch* grafis di Wayland.

> **Catatan Instalasi Manual:** Jika Anda tidak menggunakan pengelola paket Arch Linux (\`pacman\`), Anda dapat mengintegrasikan modifikasi ini dengan menyalin seluruh isi folder ini langsung ke direktori root (\`/\`) pada distribusi Linux Anda (membutuhkan akses root).
