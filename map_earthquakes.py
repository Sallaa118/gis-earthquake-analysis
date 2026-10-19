
import pandas as pd
import folium
from pathlib import Path

base_dir = Path(__file__).resolve().parent
data_path = base_dir / "data" / "earthquakes.csv"
output_dir = base_dir / "outputs"

df = pd.read_csv(data_path)

# Memeriksa dan membersihkan data
df["time"] = pd.to_datetime(
    df["time"], errors="coerce", utc=True
)

df["latitude"] = pd.to_numeric(
    df["latitude"], errors="coerce"
)
df["longitude"] = pd.to_numeric(
    df["longitude"], errors="coerce"
)
df["mag"] = pd.to_numeric(
    df["mag"], errors="coerce"
)
df["depth"] = pd.to_numeric(
    df["depth"], errors="coerce"
)

df = df.dropna(
    subset=["latitude", "longitude", "mag"]
)

# Filter wilayah Indonesia secara perkiraan.
# Ini hanya filter kotak koordinat, bukan batas resmi.
indonesia = df[
    df["latitude"].between(-11, 6)
    & df["longitude"].between(95, 141)
].copy()

print("Total gempa global:", len(df))
print("Gempa dalam wilayah filter:", len(indonesia))

# Jika filter Indonesia kosong, jangan buat peta kosong
if indonesia.empty:
    raise ValueError(
        "Tidak ada data pada filter wilayah. "
        "Periksa rentang koordinat atau dataset."
    )

peta = folium.Map(
    location=[-2.5, 118],
    zoom_start=5
)

for _, baris in indonesia.iterrows():
    magnitudo = baris["mag"]

    # Ukuran lingkaran mengikuti magnitudo
    folium.CircleMarker(
        location=[
            baris["latitude"],
            baris["longitude"]
        ],
        radius=max(3, min(12, magnitudo * 2)),
        popup=(
            f"Lokasi: {baris.get('place', 'Tidak diketahui')}<br>"
            f"Magnitudo: {magnitudo}<br>"
            f"Kedalaman: {baris.get('depth', 'N/A')} km<br>"
            f"Waktu: {baris['time']}"
        ),
        fill=True
    ).add_to(peta)

output_dir.mkdir(exist_ok=True)
peta.save(output_dir / "peta_gempa.html")

# Ringkasan statistik
indonesia.to_csv(
    output_dir / "gempa_indonesia.csv",
    index=False
)

print("Peta tersimpan di outputs/peta_gempa.html")
