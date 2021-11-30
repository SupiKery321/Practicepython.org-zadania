a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 55]

a_without_duplicates = list(set(a))
b_without_duplicates = list(set(b))

list = []

for number1 in a_without_duplicates:
    for number2 in b_without_duplicates:
        if number1 == number2:
            list.append(number1)

print(list)
        