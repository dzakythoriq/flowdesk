# Progres dan konteks FlowDesk

Terakhir diperbarui: 19 Oktober 2026, zona waktu Asia/Jakarta.

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

- Repository GitHub: https://github.com/dzakythoriq/flowdesk (public).
- Remote origin: https://github.com/dzakythoriq/flowdesk.git.
- Branch lokal main sudah mengikuti origin/main.

- Root proyek lokal: `C:\Project\flowdesk`.
- Environment tersedia pada `.venv` di root proyek.
- Versi Python environment: 3.14.8.
- Versi pip environment: 26.2.1.
- Interpreter berada pada `.venv\Scripts\python.exe`.
- `sys.prefix != sys.base_prefix` menghasilkan `True`.
- Lokasi pip berada dalam `.venv\Lib\site-packages`.
- Git tersedia: 2.37.3.windows.1.
- `main.py` tersedia sebagai skrip awal dengan dictionary kasus dan aturan pembukaan: hanya status awal NEW yang dapat menjadi OPEN. Percobaan NEW dan CLOSED sudah diverifikasi; seluruh workflow dan suite tes tersimpan belum tersedia.

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

Simpan checkpoint implementasi pertama melalui Git. Berkas yang terkait: `main.py`, `README.md`, dan `docs/PROGRESS.md`. Pembelajar mencoba staging, membaca staged diff, membuat commit, dan push sendiri dengan petunjuk pendamping. Belum ada commit atau push baru atas latihan ini saat catatan diperbarui.

Setelah checkpoint dikonfirmasi, lanjutkan ke fungsi kecil untuk mengelompokkan operasi membuka kasus agar dapat dipanggil pada data kasus yang berbeda tanpa menyalin blok if/else. Jelaskan `def`, parameter, pemanggilan fungsi, dan return secara bertahap sesuai kebutuhan, bukan sekaligus. Belum ada fungsi baru yang ditulis.

## Batasan saat ini

- Belum ada suite tes aplikasi yang disimpan di repository. Pemeriksaan sementara sudah menjalankan dua input status pada kode yang sama tanpa mengubah source file.
- Database, API, pytest, dan Postman belum menjadi bagian dari implementasi.
- Setup menggunakan interpreter environment secara eksplisit. Aktivasi terminal belum diperlukan untuk menjalankan pemeriksaan.

## Revisi presentasi repository, 15 Oktober 2026

Permintaan: README public harus menonjolkan produk dan perilaku teknis, tanpa menjadikan label "proyek belajar Python" atau kurikulum sebagai pengantar utama. Gaya pendampingan dan proses belajar tetap berlaku pada sesi pengembangan.

Referensi yang dibaca: README AthillaZaidan/SafeTrip, AthillaZaidan/Understand-Any-Paper, dan AthillaZaidan/PacketForge. Pola yang diadaptasi adalah pengantar fungsi produk, kapabilitas, workflow, setup, dan status milestone. Tidak menyalin teks, pencapaian, atau klaim implementasi dari proyek referensi.

Perubahan: README ditulis ulang untuk menjelaskan FlowDesk sebagai workflow case tracker; tabel kurikulum serta penjelasan memory dan tujuan karier tidak lagi menjadi bagian halaman utama. Status early development dan kemampuan yang direncanakan tetap dinyatakan jelas. Preferensi ini dicatat pada AGENTS.md agar digunakan pada pembaruan berikutnya.

Tidak ada kode aplikasi, dependency, environment, atau aturan transisi yang diubah. Publikasi GitHub tetap menunggu repository remote tersedia. Periksa riwayat Git untuk commit aktual revisi ini.

Verifikasi revisi: empat dokumen Markdown diperiksa tanpa tautan lokal yang rusak; pemeriksaan diff tidak menemukan masalah whitespace. Tidak ada tes aplikasi yang dijalankan karena perubahan hanya mencakup dokumentasi.

## Revisi bahasa README, 15 Oktober 2026

Permintaan terbaru: hapus seluruh bagian Roadmap beserta checklist dari README dan gunakan bahasa Inggris yang rapi serta profesional. Seluruh prosa README diterjemahkan dan disunting ke bahasa Inggris. Aturan workflow dan status implementasi tetap dipertahankan. Preferensi bahasa README dan penghilangan roadmap dicatat dalam AGENTS.md; bahasa percakapan tetap Bahasa Indonesia. Perubahan hanya mencakup dokumentasi.

## Publikasi GitHub, 16 Oktober 2026

Repository public `dzakythoriq/flowdesk` tersedia dan izin push terverifikasi. Remote `origin` dihubungkan ke `https://github.com/dzakythoriq/flowdesk.git`. Pemeriksaan branch remote sebelum pengiriman menunjukkan repository kosong.

Perintah yang benar-benar dijalankan dari root proyek:

```powershell
git remote add origin https://github.com/dzakythoriq/flowdesk.git
git ls-remote --heads origin
git push -u origin main
git rev-parse HEAD
git ls-remote origin refs/heads/main
git status --short --branch
```

Hasil pengiriman pertama: branch `main` berhasil dibuat di GitHub dan branch lokal diatur mengikuti `origin/main`. Commit lokal serta remote sama-sama `be8d81f8f43117ec4ee295b27e17f3e4b150bbf0`. Working tree bersih. README kemudian dibaca langsung melalui integrasi GitHub; isinya berbahasa Inggris, berfokus pada produk, dan tidak memiliki bagian Roadmap.

Lima berkas proyek dipublikasikan: `.gitignore`, `AGENTS.md`, `README.md`, `docs/PROGRESS.md`, dan `docs/SETUP.md`. `.venv`, konfigurasi lokal, dan dokumen handoff pribadi tidak berada dalam tracked files.

Panduan setup diperbarui dengan alamat repository serta arti remote, origin, push, dan upstream. Pembaruan catatan ini disimpan dalam commit dokumentasi tersendiri dan dikirim setelah pengiriman pertama. Untuk SHA terbaru, baca `git log -1 --oneline` dan bandingkan dengan `git ls-remote origin refs/heads/main`.

Milestone GitHub selesai pada pengiriman pertama yang telah diverifikasi. Langkah berikutnya tetap Stage 1: merepresentasikan satu kasus dengan dictionary Python, membaca field, dan memprediksi perubahan nilai. Belum ada implementasi aplikasi atau tes aplikasi yang dijalankan.

## Membaca dictionary, 18 Oktober 2026

Pembelajar menulis `main.py` sendiri. Versi yang diperiksa menyimpan `title`, `description`, dan `status` dalam satu dictionary bernama `case`, lalu menampilkan title dan status melalui dua pemanggilan `print()`.

Pendamping menjalankan perintah berikut tanpa mengubah source:

```powershell
.\.venv\Scripts\python.exe -B main.py
```

Hasil aktual, exit code 0:

```text
Review sample invoice
NEW
```

Konsep yang dibahas: pasangan key dan value; pembacaan nilai berdasarkan key; ekspresi pembacaan yang berdiri sendiri tidak mencetak output pada skrip; satu pemanggilan print dengan beberapa argumen menampilkan nilai dalam satu baris secara bawaan; dua pemanggilan print menampilkan dua baris.

Bukti pemahaman: pembelajar dapat menyebut key `description` untuk mengambil deskripsi, menulis pembacaan title/status, menghapus ekspresi mandiri yang tidak diperlukan, dan menyatakan sudah memahami pembahasan. Ini belum membuktikan penguasaan assignment, validasi transisi, atau keseluruhan Python.

Source `main.py` tetap hasil tulisan pembelajar dan tidak diubah pendamping. Saat pemeriksaan Git, file masih untracked. Catatan progres diperbarui secara lokal; tidak ada commit atau push baru pada sesi pembacaan ini.

## Memperbarui value dictionary, 18 Oktober 2026

Versi `main.py` yang diperiksa membuat dictionary kasus dengan status awal `NEW`, mencetak status, memperbarui `case["status"]` menjadi `OPEN`, dan mencetak status kembali. Pendamping menjalankan `.\.venv\Scripts\python.exe -B main.py`; exit code 0 dan output aktual:

```text
NEW
OPEN
```

Dibahas bahwa assignment memperbarui value pada dictionary yang sama, bukan membuat variabel kasus baru. Nama `current_case` pada percobaan sebelumnya belum didefinisikan; nama yang sudah tersedia adalah `case`. Urutan baris menentukan apakah print membaca nilai sebelum atau sesudah perubahan.

Pembelajar menyatakan sudah memahami pembaruan status. Hasil yang diperiksa memperlihatkan assignment langsung berjalan. Validasi transisi, kondisi if/else, serta persistence belum dibuktikan. Source tidak diubah pendamping. Catatan diperbarui lokal tanpa commit atau push baru; `main.py` masih untracked saat pemeriksaan.

## Kondisi pembukaan kasus, 19 Oktober 2026

Pembelajar berhasil memprediksi bahwa status awal `CLOSED` akan masuk ke cabang else dan tidak menjalankan assignment ke `OPEN`. Kode tersimpan memeriksa `case["status"] == "NEW"`, memperbarui status di dalam blok if, dan menampilkan status akhir setelah if/else.

Verifikasi pendamping menggunakan Python environment proyek (`python.exe -B -`) dengan pemeriksa sementara melalui stdin. Source dibaca dan salinan program di memori dijalankan dua kali dengan hanya nilai status awal yang dibedakan. Hasil:

| Status awal | Pesan aktual | Status akhir | Hasil pemeriksaan |
|---|---|---|---|
| NEW | This case is new | OPEN | Sesuai |
| CLOSED | This case is not new | CLOSED | Sesuai |

Title dan description tidak berubah pada kedua percobaan. Hash source file sebelum dan sesudah pemeriksaan sama; pendamping tidak mengubah `main.py`. Pemeriksaan selesai dengan exit code 0. Tidak menambahkan pytest, berkas tes, dependency, atau implementasi baru.

README berbahasa Inggris diperbarui untuk menjelaskan kemampuan skrip yang benar-benar tersedia, cara menjalankannya, batas aturan saat ini, serta bahwa data dibuat ulang pada setiap eksekusi. README tetap tanpa Roadmap atau checklist pengembangan.

Latihan membaca data, assignment, dan kondisi sederhana telah memperlihatkan hasil sesuai untuk skenario yang dicoba. Ini belum membuktikan keseluruhan tabel transisi atau persistence. Catatan ini masih lokal; commit/push checkpoint berikutnya akan dicoba oleh pembelajar.
