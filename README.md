# FlowDesk

FlowDesk adalah proyek belajar Python untuk membuat dan melacak kasus fiktif dengan aturan perpindahan status dan riwayat kejadian.

Tujuannya adalah memahami cara membangun, menguji, dan menjelaskan software secara bertahap. Proyek ini menguatkan fondasi engineering yang relevan untuk jalur AI/ML.

## Status saat ini

Setup environment telah diverifikasi pada 15 Oktober 2026: Python 3.14.8, virtual environment `.venv`, dan pip 26.2.1.

Repository saat ini berisi dokumentasi dan aturan belajar. Belum ada implementasi aplikasi, CLI, database, API, atau tes aplikasi.

## Contoh penggunaan yang direncanakan

Operator membuat kasus berjudul `Review sample invoice` dengan deskripsi fiktif. Aplikasi menghasilkan ID, status awal `NEW`, timestamp, dan event `CASE_CREATED`.

Operator kemudian dapat melihat daftar dan detail kasus, meminta perubahan status yang valid, serta membaca history. Kasus dan prosedurnya selalu fiktif.

## Aturan status versi pertama

| Status sekarang | Status berikutnya yang diizinkan |
|---|---|
| `NEW` | `OPEN`, `CANCELLED` |
| `OPEN` | `IN_PROGRESS`, `CANCELLED` |
| `IN_PROGRESS` | `BLOCKED`, `RESOLVED` |
| `BLOCKED` | `IN_PROGRESS` |
| `RESOLVED` | `CLOSED` |
| `CLOSED` | Tidak ada |
| `CANCELLED` | Tidak ada |

Transisi yang ditolak tidak boleh mengubah status, `updated_at`, atau history. Percobaan gagal tidak menghasilkan event `FAILED` dalam rancangan awal.

## Model data yang direncanakan

- `Case`: `case_id`, `title`, `description`, `status`, `created_at`, `updated_at`.
- `CaseEvent`: `event_id`, `case_id`, `event_type`, `old_status`, `new_status`, `reason`, `created_at`.

Case menyimpan keadaan terkini. CaseEvent menyimpan kejadian yang berhasil dicatat. ID dibuat otomatis; rekomendasi awalnya adalah awalan `CASE-` diikuti UUIDv4.

Saat SQLite ditambahkan, pembuatan kasus beserta event awal disimpan dalam satu transaksi. Perubahan status dan penambahan event juga harus berhasil atau dibatalkan bersama.

## Tahapan belajar

| Tahap | Fokus | Status |
|---|---|---|
| 0 | Memahami produk dan aturan | Dibahas; tetap direview melalui latihan |
| Setup | Python dan environment khusus | Diverifikasi |
| 1 | Python refresh melalui contoh kasus kecil | Berikutnya |
| 2 | Logika inti dan tes dalam memori | Direncanakan |
| 3 | CLI sederhana | Direncanakan |
| 4 | SQLite, relasi data, dan transaksi | Direncanakan |
| 5 | FastAPI dengan service yang sama | Direncanakan |
| 6 | Eksplorasi API melalui Postman | Direncanakan |
| 7 | Perbaikan kualitas yang punya manfaat jelas | Bertahap sesuai kebutuhan |

MVP awal selesai pada CLI + SQLite yang benar, teruji, terdokumentasi, dan dapat dijelaskan oleh pembelajar. API bukan syarat untuk menyelesaikan MVP tersebut.

## Batas ruang lingkup

Belum mencakup AI/LLM, frontend web, login, multi-user, notifikasi, integrasi perusahaan, deployment cloud, penghapusan kasus, atau pembukaan kembali kasus tertutup.

## Environment dan pemeriksaan

Lihat [panduan setup](docs/SETUP.md) untuk membuat ulang environment pada clone baru. Untuk environment yang sudah tersedia, dari root proyek jalankan:

```powershell
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -c "import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)"
.\.venv\Scripts\python.exe -m pip --version
```

Python harus mengarah ke `.venv\Scripts\python.exe`, pemeriksaan environment menghasilkan `True`, dan lokasi pip harus berada di dalam `.venv`.

Belum ada perintah menjalankan aplikasi atau tes aplikasi karena implementasinya belum dibuat. Paket aplikasi akan ditambahkan saat diperlukan.

## Catatan untuk melanjutkan

- [Progres dan konteks proyek](docs/PROGRESS.md): pekerjaan selesai, bukti pemeriksaan, pertanyaan terbuka, dan langkah berikutnya.
- [Setup dan Git](docs/SETUP.md): environment, pemeriksaan, serta hubungan Git lokal dengan GitHub.
- [Instruksi pendamping](AGENTS.md): aturan belajar dan batas perubahan untuk coding assistant.

Catatan tersebut adalah konteks berbasis file, bukan jaminan memory akun yang otomatis tersedia di semua chat. Saat melanjutkan, baca catatan progres dan kode yang benar-benar ada.
