# Manajemen Mata Kuliah
## Harisya Miranti - 122140049

## API Endpoints

### Mata Kuliah (Course) Endpoints

| Method | Endpoint                              | Deskripsi                       |
|--------|-------------------------------------|--------------------------------|
| GET    | `http://localhost:6543/api/matakuliah`      | Mendapatkan semua data Mata Kuliah  |
| GET    | `http://localhost:6543/api/matakuliah/{id}` | Mendapatkan detail Mata Kuliah       |
| POST   | `http://localhost:6543/api/matakuliah`      | Menambahkan Mata Kuliah baru          |
| PUT    | `http://localhost:6543/api/matakuliah/{id}` | Mengupdate data Mata Kuliah            |
| DELETE | `http://localhost:6543/api/matakuliah/{id}` | Menghapus data Mata Kuliah             |

---

## Langkah Kerja

Ikuti langkah-langkah berikut untuk menyiapkan dan menjalankan proyek Pyramid ini:

1. **Masuk ke direktori proyek**

   ```bash
   cd pyramid_matakuliah

2. **Buat virtual environment Python**

   ```bash
   python3 -m venv venv
   venv\Scripts\activate 

3. **update packaging tools**

    ```bash
    pip install --upgrade pip setuptools

4.  **update packaging tools**
    ```bash
    pip install -e ".[testing]"

5. **Inisialisasi dan migrasi database dengan Alembic** 
    ```bash
    alembic -c development.ini revision --autogenerate -m "init"
    alembic -c development.ini upgrade head

6. **Load data default ke database menggunakan skrip inisialisasi** 
    ```bash
    initialize_manajemen_matakuliah_db development.ini

7. **jalankan proyek**
    ```bash
    pserve development.ini --reload


