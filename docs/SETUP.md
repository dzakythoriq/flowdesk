# Setup FlowDesk dan dasar Git

## Target setup

Satu environment Python untuk FlowDesk. Keadaan yang terverifikasi pada sesi awal adalah Python 3.14.8 dan pip 26.2.1. Nomor versi pip di komputer lain dapat berbeda.

Panduan pembuatan ulang berikut berlaku untuk clone atau folder proyek baru yang belum memiliki `.venv`. Jika environment sudah ada dan bekerja, cukup jalankan pemeriksaan; tidak perlu membuatnya ulang.

## Menyiapkan Python

Gunakan Python 3.14 untuk Windows 64-bit dari [situs resmi Python](https://www.python.org/downloads/windows/). Saat membuat ulang setup di masa mendatang, periksa pembaruan yang tersedia dalam seri tersebut.

Pada setup awal dipilih instalasi Python mandiri, terpisah dari Python Laragon dan Conda. Instalasi per-user yang digunakan berada di bawah `%LOCALAPPDATA%\Programs\Python\Python314`.

Lokasi tersebut harus disesuaikan jika Python dipasang di tempat lain. Jangan menganggap perintah `python` biasa memilih versi yang benar ketika terdapat beberapa instalasi.

## Membuat environment pada proyek baru

Buka PowerShell pada root proyek. Perintah berikut mengasumsikan lokasi instalasi per-user di atas:

```powershell
$flowdeskPython = Join-Path $env:LOCALAPPDATA 'Programs\Python\Python314\python.exe'
& $flowdeskPython --version
```

Pastikan hasil menunjukkan seri 3.14 sebelum melanjutkan:

```powershell
& $flowdeskPython -m venv .venv
```

`-m venv` menjalankan modul bawaan pembuat environment; `.venv` adalah nama folder tujuan. Python membuat dan mengisi folder itu secara otomatis. Environment mengikuti versi interpreter yang digunakan untuk membuatnya.

## Memeriksa environment

```powershell
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -c "import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)"
.\.venv\Scripts\python.exe -m pip --version
```

Hasil yang benar:

- Versi Python sesuai interpreter yang dipilih.
- Lokasi interpreter berakhir dengan `.venv\Scripts\python.exe` di proyek ini.
- Perbandingan prefix menghasilkan `True`.
- Lokasi pip berada di `.venv\Lib\site-packages`.

Perintah di atas memanggil Python environment secara langsung. Aktivasi hanya mempermudah pemanggilan `python` dan `pip` pada terminal terkait; aktivasi bukan syarat jika alamat interpreter sudah diberikan.

Belum perlu mengubah execution policy PowerShell, mengubah PATH global, memasang FastAPI, atau mengubah Conda base untuk mengikuti langkah ini.

## Apa yang disimpan dalam Git

Git menyimpan riwayat perubahan berkas proyek. Repository lokal berada di komputer, sedangkan GitHub menjadi tempat repository remote yang dapat diakses sesuai visibilitasnya.

- `.gitignore` mengecualikan environment, cache, konfigurasi lokal, dan database hasil aplikasi.
- `.venv` tidak dikirim ke GitHub. Environment dibuat ulang pada komputer masing-masing.
- `git add` memilih perubahan untuk commit berikutnya, disebut staging.
- `git diff --cached` memperlihatkan perubahan yang sudah dipilih.
- `git commit` mencatat snapshot lokal dengan pesan yang menjelaskan tujuannya.
- `git push` mengirim commit ke remote. Commit lokal tidak otomatis berarti sudah ada di GitHub.

Perintah pembacaan yang aman untuk memeriksa keadaan proyek:

```powershell
git status --short --branch
git log --oneline -5
git remote -v
git check-ignore -v .venv/Scripts/python.exe
```

Branch adalah jalur riwayat pengembangan. Branch awal proyek ini menggunakan nama `main`. Remote adalah nama dan alamat repository lain; `origin` lazim digunakan untuk repository GitHub utama.

## Membuat repository GitHub

Visibilitas yang dipilih untuk FlowDesk adalah public. Jika repository lokal sudah berisi dokumentasi, buat repository GitHub kosong dengan nama `flowdesk` tanpa README, .gitignore, atau license otomatis. Berkas yang sama sudah dikelola dari lokal, dan inisialisasi terpisah dapat menimbulkan dua riwayat awal.

Sebelum mengirim commit, periksa staged diff dan pastikan hanya berkas proyek yang relevan yang dipilih. Jangan mengunggah environment, konfigurasi rahasia, dokumen handoff pribadi, atau transkrip percakapan.

Keberhasilan publikasi diperiksa dengan membandingkan commit branch lokal dengan branch remote, bukan hanya keberhasilan menambahkan alamat remote.

## Dokumentasi setelah milestone

Perbarui `docs/PROGRESS.md` dengan hasil aktual, konsep yang perlu dilatih, dan satu langkah berikutnya. Perbarui README ketika kemampuan aplikasi berubah. Dokumentasi tidak boleh menyebut fitur atau tes berhasil jika belum diimplementasikan atau dijalankan.

## Referensi

- [Python venv](https://docs.python.org/3.14/library/venv.html)
- [Git init](https://git-scm.com/docs/git-init)
- [Gitignore](https://git-scm.com/docs/gitignore)
- [Membuat repository GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)
