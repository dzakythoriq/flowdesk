# Progres dan konteks FlowDesk

Terakhir diperbarui: 15 Oktober 2026, zona waktu Asia/Jakarta.

## Cara menggunakan catatan ini

Baca README.md dan AGENTS.md bersama catatan ini sebelum melanjutkan. Periksa kembali keadaan berkas dan Git; jangan menganggap catatan lama lebih akurat daripada hasil pemeriksaan aktual.

Catatan ini menyimpan konteks proyek yang diperlukan untuk melanjutkan belajar. Isinya tidak menjamin memory lintas chat dan tidak menggantikan peninjauan kode.

## Preferensi kerja yang disepakati

- Bahasa Indonesia yang natural, rinci, dan bertahap.
- Satu milestone kecil setiap waktu; jelaskan tujuan, konsep, langkah, dan hasil yang diharapkan.
- Beri ruang untuk prediksi, pseudocode, atau percobaan kecil sebelum solusi lengkap jika bermanfaat.
- Setelah milestone, dokumentasikan perubahan, pemeriksaan aktual, batasan, dan langkah berikutnya.
- Gunakan data fiktif. Kode harus dapat dijelaskan oleh pembelajar.
- Tujuan belajar jangka panjang tetap berkaitan dengan AI/ML engineering.
- Nama repository yang diminta adalah `flowdesk`, dengan visibilitas public.

## Keadaan yang sudah diverifikasi

- Root proyek lokal: `C:\Project\flowdesk`.
- Environment tersedia pada `.venv` di root proyek.
- Versi Python environment: 3.14.8.
- Versi pip environment: 26.2.1.
- Interpreter berada pada `.venv\Scripts\python.exe`.
- `sys.prefix != sys.base_prefix` menghasilkan `True`.
- Lokasi pip berada dalam `.venv\Lib\site-packages`.
- Git tersedia: 2.37.3.windows.1.
- Belum ada kode aplikasi atau tes aplikasi.

## Pemeriksaan aktual sesi setup

Dijalankan dari root proyek, baik oleh pembelajar maupun pemeriksaan ulang pendamping:

```powershell
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -c "import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)"
.\.venv\Scripts\python.exe -m pip --version
```

Hasil: Python 3.14.8, interpreter di environment proyek, hasil `True`, dan pip 26.2.1 untuk Python 3.14 pada environment proyek.

## Konsep yang telah dibahas

- Case dibedakan dengan ID otomatis, meskipun judulnya sama.
- Status terkini berbeda dengan history kejadian.
- State machine menentukan transisi yang diperbolehkan.
- Transisi ilegal tidak mengubah status, `updated_at`, atau history.
- Atomicity menjaga status dan event berhasil atau gagal bersama. Pada latihan konseptual, kegagalan menyimpan event mempertahankan status `OPEN` dan jumlah history sebelumnya.
- Percobaan gagal tidak menghasilkan event `FAILED` pada history dalam scope awal. Log diagnosis aplikasi dapat dibahas kemudian.
- Idempotency membahas efek pengulangan operasi, berbeda dari atomicity.
- Environment memisahkan paket proyek. Lokasinya boleh di subfolder `.venv`; kode proyek tidak ditulis di dalamnya.
- Memori, SQLite, dan API memisahkan persoalan aturan, penyimpanan, dan antarmuka. Pemahaman praktisnya masih perlu dilatih saat tahap terkait.

Pembahasan konsep bukan bukti bahwa seluruh topik telah dikuasai. Lanjutkan dengan contoh kecil dan penjelasan pembelajar.

## Milestone sesi ini

Menyiapkan README, AGENTS.md, panduan setup, catatan progres, dan .gitignore. Menyiapkan Git lokal serta publikasi dokumentasi ke repository GitHub public yang diminta.

Git lokal telah diinisialisasi pada branch `main`. Pemeriksaan `git check-ignore -v .venv/Scripts/python.exe` menunjukkan bahwa `.venv` dikecualikan oleh .gitignore. Commit fondasi telah dibuat: `be73004` dengan pesan `docs: establish FlowDesk setup and learning workflow`. Setelah commit tersebut, working tree bersih. Pemeriksaan staged diff tidak menemukan masalah whitespace; empat dokumen Markdown diperiksa dan tidak ada tautan lokal yang rusak. Daftar tracked files hanya berisi empat dokumen Markdown dan .gitignore; environment tidak ikut tersimpan. Akun GitHub terhubung adalah `dzakythoriq`; repository remote `flowdesk` belum tersedia melalui koneksi pada saat pemeriksaan. Publikasi belum dilakukan. Gunakan `git log --oneline -5` untuk membaca commit aktual, dan jangan menganggap commit lokal otomatis sudah ada di GitHub.

## Langkah belajar berikutnya

Latihan Stage 1: merepresentasikan satu kasus fiktif dalam dictionary Python, membaca nilai berdasarkan key, lalu memahami perbedaan nilai yang disimpan dan nilai yang dicetak.

Acceptance criteria latihan berikutnya:

1. Dapat menjelaskan variable, string, dictionary, key, dan value pada contoh satu kasus.
2. Dapat mengambil serta menampilkan title dan status.
3. Dapat memprediksi hasil ketika nilai status dalam dictionary diubah.
4. Memahami bahwa perubahan dictionary langsung belum menerapkan aturan state machine.

Belum membuat file latihan atau fungsi aplikasi pada milestone dokumentasi ini. Sebelum implementasi latihan, jelaskan contoh kecil dan beri ruang pembelajar mencoba.

## Batasan saat ini

- Tidak ada tes aplikasi yang dapat dijalankan karena kode aplikasinya belum tersedia.
- Database, API, pytest, dan Postman belum menjadi bagian dari implementasi.
- Setup menggunakan interpreter environment secara eksplisit. Aktivasi terminal belum diperlukan untuk menjalankan pemeriksaan.

## Revisi presentasi repository, 15 Oktober 2026

Permintaan: README public harus menonjolkan produk dan perilaku teknis, tanpa menjadikan label "proyek belajar Python" atau kurikulum sebagai pengantar utama. Gaya pendampingan dan proses belajar tetap berlaku pada sesi pengembangan.

Referensi yang dibaca: README AthillaZaidan/SafeTrip, AthillaZaidan/Understand-Any-Paper, dan AthillaZaidan/PacketForge. Pola yang diadaptasi adalah pengantar fungsi produk, kapabilitas, workflow, setup, dan status milestone. Tidak menyalin teks, pencapaian, atau klaim implementasi dari proyek referensi.

Perubahan: README ditulis ulang untuk menjelaskan FlowDesk sebagai workflow case tracker; tabel kurikulum serta penjelasan memory dan tujuan karier tidak lagi menjadi bagian halaman utama. Status early development dan kemampuan yang direncanakan tetap dinyatakan jelas. Preferensi ini dicatat pada AGENTS.md agar digunakan pada pembaruan berikutnya.

Tidak ada kode aplikasi, dependency, environment, atau aturan transisi yang diubah. Publikasi GitHub tetap menunggu repository remote tersedia. Periksa riwayat Git untuk commit aktual revisi ini.

Verifikasi revisi: empat dokumen Markdown diperiksa tanpa tautan lokal yang rusak; pemeriksaan diff tidak menemukan masalah whitespace. Tidak ada tes aplikasi yang dijalankan karena perubahan hanya mencakup dokumentasi.
