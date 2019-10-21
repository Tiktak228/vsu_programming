def stupid_sort(data):
    i = 0
    n = len(data) - 1
    while i < n:
        if data[i + 1] < data[i]:
            data[i], data[i + 1] = data[i + 1], data[i]
            i = 0
        else:
            i += 1
    return data

element = []
b = int(input("Введите кол-во элементов массива"))
for x in range(b):
    a = input("Введите элемент массива")
    element.append(a)
print(stupid_sort(element))
