from ucimlrepo import fetch_ucirepo
import pandas as pd
import time

print("[INFO] Memulai proses download & saving...")
start_time = time.time()

# 1. Fetch dataset dari UCI Repository
covertype = fetch_ucirepo(id=31)

# 2. Ambil data (X = Features, y = Target)
X = covertype.data.features
y = covertype.data.targets

# 3. Gabungkan jadi satu DataFrame Pandas
print("[INFO] Menggabungkan Features dan Target...")
df = pd.concat([X, y], axis=1)

# 4. SIMPAN KE CSV
output_filename = 'covtype.csv'
print(f"[INFO] Sedang menulis file '{output_filename}' ke hardisk... (Tunggu bentar)")
df.to_csv(output_filename, index=False)

end_time = time.time()
print(f"[SUKSES] File '{output_filename}' sudah muncul di folder proyek lo.")
print(f"[INFO] Waktu total: {end_time - start_time:.2f} detik")
print(f"[INFO] Total Data Tersimpan: {df.shape}")

# 5. Cek Sebaran Data (Imbalance Check)
print("\n[ANALISIS] SEBARAN KELAS HUTAN (TARGET):")
print(df['Cover_Type'].value_counts())