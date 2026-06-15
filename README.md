# Nexus Code (nexus-code)

AI Coding Agent CLI yang terintegrasi secara native dengan **NexusRouter.net**. Nexus Code membantu Anda menulis kode, me-refactor, melakukan debug, dan mengelola workflow Git langsung dari terminal.

---

## 🚀 Persyaratan Minimum Keanggotaan (Membership)
* Nexus Code **tidak dapat digunakan oleh akun ber-plan Free**.
* Anda harus memiliki plan minimal **Basic**, **Plus**, **Pro**, **Dedicated**, atau plan **PAYG (Pay-As-You-Go)** dengan saldo balance di atas nol.
* Upgrade plan Anda melalui [Dashboard NexusRouter Billing](https://nexusrouter.net/dashboard/billing).

---

## 📥 Instalasi Cepat (Step-by-Step)

### 1. Jalankan Installer Script
Jalankan perintah berikut di terminal Anda untuk mengunduh dan menginstal binary `nexus-code` secara otomatis:

**Linux & macOS:**
```bash
curl -fsSL https://nexusrouter.net/install | bash
```

**Windows (PowerShell):**
Silakan download file binary ZIP dari [GitHub Releases](https://github.com/nexusrouters/nexus-code/releases), ekstrak ke folder pilihan Anda, dan tambahkan folder tersebut ke System environment `PATH` Anda.

### 2. Muat Ulang Terminal
Buka jendela terminal baru atau jalankan perintah berikut untuk me-load path yang baru ditambahkan:
```bash
source ~/.bashrc # atau ~/.zshrc sesuai shell Anda
```

### 3. Hubungkan Akun (OAuth Device Login)
Hubungkan CLI ke akun NexusRouter Anda dengan menjalankan perintah:
```bash
nexus-code account login
```

Langkah login:
1. CLI akan menampilkan instruksi berupa URL dan 8-karakter kode verifikasi:
   * Contoh: `Buka browser ke: https://nexusrouter.net/auth/device`
   * Contoh: `Masukkan kode: EJ4G-A6FJ`
2. Buka browser Anda, login ke dashboard NexusRouter.
3. Masukkan kode tersebut, lalu klik **Otorisasi Sekarang**.
4. Terminal Anda otomatis mendeteksi otorisasi dan login sukses!

### 4. Mulai Gunakan
Masuk ke folder project Anda dan jalankan agen:
```bash
cd /path/to/your/project
nexus-code
```

---

## ⚙️ Perintah CLI yang Tersedia

| Perintah | Deskripsi |
| :--- | :--- |
| `nexus-code` | Memulai interactive session coding agent di folder aktif |
| `nexus-code account login` | Melakukan proses autentikasi (OAuth Device Flow) |
| `nexus-code account logout` | Keluar dari akun aktif |
| `nexus-code --version` | Menampilkan versi Nexus Code yang terinstall |
| `nexus-code --help` | Menampilkan panduan bantuan command |

---

## 🛠️ Troubleshoot & Error Handling
* **Error `403 Forbidden` / `unsupported_plan`**: Terjadi jika Anda mencoba login dengan akun ber-tier **Free**. Pastikan Anda sudah meng-upgrade plan Anda.
* **Error `401 Unauthorized` / `authentication_error`**: API token Anda tidak valid atau kedaluwarsa. Silakan jalankan `nexus-code account logout` lalu lakukan login ulang.
