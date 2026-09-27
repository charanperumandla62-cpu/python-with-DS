def remove_duplicates(a):
    if not a:
        return 0

    ind = 1

    for i in range(1, len(a)):
        if a[i] != a[i - 1]:
            a[ind] = a[i]
            ind += 1

    return ind


a = [1, 2, 2, 3, 4, 4, 5]
new_length = remove_duplicates(a)

print(a[:new_length])