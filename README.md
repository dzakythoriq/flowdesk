# FlowDesk

**Workflow Case Tracker & Simulator**

FlowDesk dirancang untuk melacak kasus dengan alur status yang eksplisit, identitas otomatis, dan riwayat perubahan yang dapat ditelusuri. Fokusnya adalah menjaga konsistensi antara status kasus dan catatan perubahannya.

## Status Pengembangan

**Early development.** Environment Python dan dokumentasi awal sudah tersedia. Implementasi core workflow, CLI, penyimpanan, dan API belum tersedia.

## Kapabilitas yang Direncanakan

- Membuat kasus dengan ID otomatis, judul, deskripsi, dan timestamp.
- Menampilkan daftar kasus dan detail berdasarkan ID.
- Memvalidasi perubahan status sesuai aturan workflow.
- Menyimpan event pembuatan dan perubahan status sebagai history kasus.
- Mempertahankan data secara lokal menggunakan SQLite.
- Menyediakan CLI, kemudian REST API untuk operasi inti yang sama.

Contoh alur: operator membuat kasus `Review sample invoice`, membuka kasus, memulai pemeriksaan, lalu menandainya selesai dan menutupnya. Jika pekerjaan terhambat, kasus dapat masuk ke `BLOCKED` sebelum dilanjutkan kembali. Seluruh data contoh bersifat fiktif.

## Workflow

Alur utama:

```text
NEW -> OPEN -> IN_PROGRESS -> RESOLVED -> CLOSED
```

| Status sekarang | Transisi yang diizinkan |
|---|---|
| `NEW` | `OPEN`, `CANCELLED` |
| `OPEN` | `IN_PROGRESS`, `CANCELLED` |
| `IN_PROGRESS` | `BLOCKED`, `RESOLVED` |
| `BLOCKED` | `IN_PROGRESS` |
| `RESOLVED` | `CLOSED` |
| `CLOSED` | Tidak ada |
| `CANCELLED` | Tidak ada |

Transisi yang ditolak harus mempertahankan status, `updated_at`, dan history. Pada tahap persistence, perubahan status dan penambahan event akan disimpan dalam satu transaksi database.

## Model Data

| Entitas | Field yang direncanakan |
|---|---|
| `Case` | `case_id`, `title`, `description`, `status`, `created_at`, `updated_at` |
| `CaseEvent` | `event_id`, `case_id`, `event_type`, `old_status`, `new_status`, `reason`, `created_at` |

`Case` menyimpan keadaan terkini. `CaseEvent` menyimpan kejadian yang terkait dengan satu kasus. Jenis event awal adalah `CASE_CREATED` dan `STATUS_CHANGED`.

## Teknologi

| Komponen | Teknologi | Status |
|---|---|---|
| Runtime | Python 3.14 | Environment tersedia |
| Persistence | SQLite melalui `sqlite3` | Direncanakan |
| API | FastAPI | Direncanakan |
| Automated testing | pytest | Direncanakan |

## Setup

Lihat [panduan setup](docs/SETUP.md) untuk menyiapkan environment lokal. Jika `.venv` sudah tersedia, jalankan pemeriksaan berikut dari root repository melalui PowerShell:

```powershell
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -c "import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)"
.\.venv\Scripts\python.exe -m pip --version
```

Interpreter dan pip harus mengarah ke `.venv` proyek ini. Pemeriksaan environment menghasilkan `True`.

Perintah menjalankan aplikasi dan pengujian akan ditambahkan bersama implementasinya.

## Roadmap

- [x] Environment lokal dan dokumentasi awal.
- [ ] Core model, validasi input, aturan transisi, dan event history dalam memori.
- [ ] Pengujian perilaku inti.
- [ ] CLI untuk membuat, melihat, dan memperbarui kasus.
- [ ] SQLite persistence dengan transaksi dan pengujian rollback.
- [ ] REST API dan pengujian endpoint.
- [ ] Koleksi Postman untuk skenario API utama.

## Scope

Versi awal ditujukan untuk satu operator lokal dengan data fiktif. Frontend web, authentication, multi-user, notifikasi, integrasi eksternal, AI/LLM, dan deployment cloud berada di luar scope awal.
