import pandas as pd

data = {
    'Merk Mobil': ['Toyota', 'Honda', 'Suzuki', 'Hyundai', 'Mazda', 'Ford', 'BMW', 'Mercedes', 'Mitsubishi', 'Nissan'],
    'Kota Penjualan': ['Jakarta', 'Bandung', 'Jakarta', 'Surabaya', 'Bandung', 'Jakarta', 'Surabaya', 'Jakarta', 'Bandung', 'Surabaya'],
    'Harga (Juta Rupiah)': [200, 150, 120, 180, 220, 250, 500, 550, 200, 170],
    'Tahun': [2015, 2016, 2017, 2018, 2015, 2016, 2017, 2018, 2015, 2016],
    'Status': ['Sold', 'Sold', 'Available', 'Sold', 'Available', 'Sold', 'Sold', 'Available', 'Sold', 'Available']
}

df = pd.DataFrame(data)
print("\n", "=================================================================================")
print(df)
print("=================================================================================", "\n")

print(df.describe())
print("====================================================", "\n")

print(df.min(), "\n")
print(df.max(), "\n")
print(df.__len__(), "\n")
print(df["Harga (Juta Rupiah)"].mean(), "\n")
standard_deviation = df['Harga (Juta Rupiah)'].std()
print("Standar deviasi:", standard_deviation, "\n")
quartile_1 = df['Harga (Juta Rupiah)'].quantile(0.25)
quartile_2 = df['Harga (Juta Rupiah)'].quantile(0.50)  # Median
quartile_3 = df['Harga (Juta Rupiah)'].quantile(0.75)

print("Kuartil 1:", quartile_1)
print("Kuartil 2:", quartile_2)
print("Kuartil 3:", quartile_3, "\n")
print("====================================================", "\n")

kota = df['Kota Penjualan'].value_counts().head(3)
print("Top 3 Kota dengan jumlah mobil terjual terbanyak:")
print(kota)
print("====================================================", "\n")

mobil_harga_sama = df[df.duplicated(['Harga (Juta Rupiah)'], keep=False)]
print("Mobil dengan harga yang sama:")
print(mobil_harga_sama)
print("====================================================", "\n")

kuartil_1 = df['Harga (Juta Rupiah)'].quantile(0.25)
kuartil_3 = df['Harga (Juta Rupiah)'].quantile(0.75)
print("\n", "=================================================================================")

def kategori_harga(harga):
    if harga < kuartil_1:
        return 'Murah'
    elif harga > kuartil_3:
        return 'Mahal'
    else:
        return 'Sedang'

df['Kategori Harga'] = df['Harga (Juta Rupiah)'].apply(kategori_harga)
print("Dataframe dengan kolom baru 'Kategori Harga':")
print(df)
print("\n", "=================================================================================")