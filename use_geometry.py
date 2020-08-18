from geometri.persegipanjang import hitung_luas_persegi_panjang, info as info_persegipanjang
from geometri.segitiga import hitung_luas_segitiga, info as info_segitiga

print('import cara pertama')
from geometri.segitiga import hitung_luas_segitiga  # cara paling gampang

hitung_luas_segitiga(10, 3)  # setelah mengetik 'hitung_luas_segitiga', lalu tekan alt dan enter, maka otomatis ada import
print(f'Hitung luas segitiga = {hitung_luas_segitiga(10, 3)}')

print('\nImport cara kedua')
import geometri.segitiga

print(f'Hitung luas segitiga = {geometri.segitiga.hitung_luas_segitiga(10, 3)}')

print('\nImport cara ketiga')
import geometri.segitiga as gs

print(f'Hitung luas segitiga = {gs.hitung_luas_segitiga(10, 3)}')

print('\nMengitung luas persegipanjang')
print(f'Hitung luas persegi panjang = {hitung_luas_persegi_panjang(10, 3)}')

