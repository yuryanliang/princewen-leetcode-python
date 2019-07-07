def rem_dup(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return arr[:i + 1]


arr = [1, 2, 2, 3, 3, 5, 5]
print(rem_dup(arr))
