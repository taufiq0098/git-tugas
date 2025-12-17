data_panen = {
'lokasi1': {
'nama_lokasi': 'Kebun A',
'hasil_panen': {
'padi': 1200,
'jagung': 800,
'kedelai': 500
}
},
'lokasi2': {
'nama_lokasi': 'Kebun B',
'hasil_panen': {
'padi': 1500,
'jagung': 900,
'kedelai': 450
}
},
'lokasi3': {
'nama_lokasi': 'Kebun C',
'hasil_panen': {
'padi': 1100,
'jagung': 750,
'kedelai': 600
}
},
'lokasi4': {
'nama_lokasi': 'Kebun D',
'hasil_panen': {
'padi': 1300,
'jagung': 850,
'kedelai': 550
}
},
'lokasi5': {
'nama_lokasi': 'Kebun E',
'hasil_panen': {
'padi': 1400,
'jagung': 950,
'kedelai': 480
}
}
}


# Menampilkan seluruh data
for key, value in data_panen.items():
    print(key, value)


# Jumlah jagung dari lokasi2
jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print('Jagung lokasi2:', jagung_lokasi2)


# Nama lokasi dari lokasi3
nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print('Nama lokasi3:', nama_lokasi3)


# Variabel jumlah padi dan kedelai tiap lokasi
padi_kedelai = {}
for key, value in data_panen.items():
    padi = value['hasil_panen']['padi']
    kedelai = value['hasil_panen']['kedelai']
    padi_kedelai[key] = {'padi': padi, 'kedelai': kedelai}


# Percabangan kondisi
for key, value in data_panen.items():
    padi = value['hasil_panen']['padi']
    jagung = value['hasil_panen']['jagung']
if padi > 1300 or jagung > 800:
    print(value['nama_lokasi'], 'memerlukan perhatian khusus')
else:
    print(value['nama_lokasi'], 'dalam kondisi baik')