import numpy as np
import pandas as pd

print("="*50)
print("Neural Genesis |:-:| Log 01: Environment Check")
print("="*50)

# Eksperimen NumPy 
print(" - NumPy Array -")
data_angka = np.array([10, 20, 30, 40, 50])
print("Data asli:", data_angka)
print("Rata-rata (Mean) dari data:", np.mean(data_angka))
print("\n")

# Eksperimen Pandas
print(" - Pandas DataFrame -")
data_tabel = {
    "Nama": ["Alpha", "Beta", "Gamma"],
    "Usia": [25, 30, 22],
    "Skor": [85.5, 92.0, 78.5]
}
df = pd.DataFrame(data_tabel)
print(df)
print(f"\n{"="*50}")