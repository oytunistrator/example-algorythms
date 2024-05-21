# def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Kullanım
print(quick_sort([64, 34, 25, 12, 22, 11, 90]))
# Çıktı: [11, 12, 22, 25, 34, 64, 90]
