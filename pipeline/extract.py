
import pandas as pd
from pathlib import Path


def extract_data():
    # Menentukan lokasi folder utama proyek
    project_dir = Path(__file__).resolve().parent.parent

    # Lokasi dataset mentah
    file_path = project_dir / "data" / "raw" / "hotel_bookings.csv"

    # Membaca dataset CSV
    df = pd.read_csv(file_path)

    print("=== EXTRACT DATA BERHASIL ===")
    print(f"Total baris: {len(df)}")
    print(f"Total kolom: {len(df.columns)}")

    print("\nPreview data:")
    print(df.head())

    return df


if __name__ == "__main__":
    extract_data()
