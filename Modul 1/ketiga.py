import numpy as np

# Membuat array dengan elemen numerik acak
arr = np.random.randint(1, 60, size=10)
print("Array awal:", arr)

# Normalisasi array menggunakan Min-Max Scaling
min_val = np.min(arr)
max_val = np.max(arr)
normalized_arr = (arr - min_val) / (max_val - min_val)
print("Array setelah dinormalisasi:", normalized_arr)

# Mengurutkan array dari nilai terbesar ke terkecil
sorted_arr = np.sort(arr)[::-1]
print("Array sort:", sorted_arr)
