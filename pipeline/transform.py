
import pandas as pd
from pathlib import Path


def transform_data(df):
    print("=== MEMULAI TRANSFORMASI DATA ===")

    # 1. Menghapus data duplikat
    df = df.drop_duplicates()

    # 2. Mengisi nilai kosong
    df["country"] = df["country"].fillna("Unknown")
    df["agent"] = df["agent"].fillna(0)
    df["company"] = df["company"].fillna(0)
    df["children"] = df["children"].fillna(0)

    # 3. Membuat kolom total malam menginap
    df["total_nights"] = (
        df["stays_in_weekend_nights"] +
        df["stays_in_week_nights"]
    )

    # 4. Membuat kolom total tamu
    df["total_guests"] = (
        df["adults"] +
        df["children"] +
        df["babies"]
    )

    # 5. Menghitung estimasi pendapatan
    df["estimated_revenue"] = (
        df["adr"] * df["total_nights"]
    )

    # Pembatalan tidak dihitung sebagai pendapatan aktual
    df.loc[df["is_canceled"] == 1, "estimated_revenue"] = 0

    # 6. Menghapus pemesanan tanpa tamu atau malam menginap
    df = df[
        (df["total_guests"] > 0) &
        (df["total_nights"] > 0)
    ].copy()

    print("=== TRANSFORMASI BERHASIL ===")
    print(f"Total data setelah dibersihkan: {len(df)}")
    print(f"Total kolom setelah transformasi: {len(df.columns)}")

    return df


if __name__ == "__main__":
    project_dir = Path(__file__).resolve().parent.parent

    input_file = project_dir / "data" / "raw" / "hotel_bookings.csv"
    output_file = project_dir / "data" / "processed" / "hotel_bookings_clean.csv"

    df = pd.read_csv(input_file)
    df_clean = transform_data(df)

    df_clean.to_csv(output_file, index=False)

    print(f"\nData bersih disimpan di: {output_file}")
