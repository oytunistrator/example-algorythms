# Binary Search (İkili Arama)

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Kullanım
print(binary_search([11, 12, 22, 25, 34, 64, 90], 22))
# Çıktı: 2 (22 sayısı dizinin 2. indeksindedir)
