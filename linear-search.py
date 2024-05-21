# Linear Search (Doğrusal Arama):
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Kullanım
print(linear_search([64, 34, 25, 12, 22, 11, 90], 22))
# Çıktı: 4 (22 sayısı dizinin 4. indeksindedir)
