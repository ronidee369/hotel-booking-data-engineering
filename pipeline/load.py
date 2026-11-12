
import pandas as pd
import os
from pathlib import Path
from sqlalchemy import create_engine, text
from dotenv import load_dotenv


def load_data():
    # Menentukan lokasi folder utama project
    project_dir = Path(__file__).resolve().parent.parent

    # Lokasi file CSV hasil transformasi
    file_path = (
        project_dir
        / "data"
        / "processed"
        / "hotel_bookings_clean.csv"
    )

    # Load environment variables dari file .env
    env_path = project_dir / ".env"
    load_dotenv(env_path)

    # Mengambil koneksi PostgreSQL dari .env
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise ValueError(
            "DATABASE_URL tidak ditemukan di file .env"
        )

    # Membuat koneksi ke PostgreSQL
    engine = create_engine(database_url)

    try:
        # Membaca data hasil transformasi
        df = pd.read_csv(file_path)

        # Memasukkan data ke tabel PostgreSQL
        df.to_sql(
            "hotel_bookings",
            engine,
            if_exists="replace",
            index=False
        )

        # Memeriksa jumlah data di PostgreSQL
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT COUNT(*) FROM hotel_bookings")
            )
            total_rows = result.scalar()

        print("=== LOAD DATA BERHASIL ===")
        print(f"Total data masuk PostgreSQL: {total_rows}")

    finally:
        engine.dispose()


if __name__ == "__main__":
    load_data()
