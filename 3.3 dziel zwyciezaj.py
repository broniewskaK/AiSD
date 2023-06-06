def find_max(arr, a, b):
    if a == b:
        return arr[a]

    c = (a + b) // 2
    max_a = find_max(arr, a, c)
    max_b = find_max(arr, c + 1, b)
    return max(max_a, max_b)

# Przykładowe użycie
v = [4, 9, 2, 7, 5, 1, 8, 3, 6]
max_element = find_max(v, 0, len(v) - 1)
print("Największy element to", max_element)