a = int(input("Введите положительное число "))
b = a
maximum = b % 10
while b > 0:
    c = b % 10
    if c > maximum:
        maximum = c
    b = b // 10
print(f"Максимальная цифра в веденном числе {a} это {maximum}")
