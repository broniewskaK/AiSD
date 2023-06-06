def merge(A, B):
    merged = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            merged.append(A[i])
            i += 1
        else:
            merged.append(B[j])
            j += 1
    while i < len(A):
        merged.append(A[i])
        i += 1
    while j < len(B):
        merged.append(B[j])
        j += 1

    return merged
A = [1, 35, 42, 65, 68, 25, 55, 59, 70, 79]
B = [len(A)]
A.sort()
B.sort()
merged_v = merge(A, B)
print("Scalone wektory:", merged_v)