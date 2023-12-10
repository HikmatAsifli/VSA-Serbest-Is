def matrisi_sirala(matris):
    for satir in matris:
        satir.sort(reverse=True)

# Örnek bir matris
matris = [
    [5, 8, 1],
    [4, 7, 2],
    [3, 6, 9]
]

# Matrisi sırala
matrisi_sirala(matris)

# Sonucu görüntüle
for satir in matris:
    print(satir)
