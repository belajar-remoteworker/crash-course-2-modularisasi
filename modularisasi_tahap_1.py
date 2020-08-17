"""
Program menghitung luas segitiga
luas_segitiga = alas * tinggi /2
"""
print('Menghitung luas segitiga')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi /2
print(f'Segitiga dengan alas ={alas} dan tinggi ={tinggi} memiliki luas ={luas_segitiga}')

print('\nMembuat fungsi hitung_luas_segitiga')
def hitung_luas_segitiga(alas, tinggi) : # menggunakan : untuk menjelaskan fungsi dibawahnya
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

alas = 10
tinggi = 6
print(f'Dengan fungsi, Segitiga dengan alas ={alas} dan tinggi ={tinggi} memiliki luas ={hitung_luas_segitiga(10, 6)}')
print(f'Menghitung segitiga dengan fungsi, hasilnya={hitung_luas_segitiga(10, 6)}')
print(f'Menghitung segitiga dengan fungsi, hasilnya={hitung_luas_segitiga(20, 2)}')




