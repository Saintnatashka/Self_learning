number = int(input("Введіть 5-значне число: "))

# Перевірка на 5-значне число
if 10000 <= number <= 99999:
    reversed_number = int(str(number)[::-1])
    print("Перевернуте число:", reversed_number)
else:
    print("Введіть правильне пʼятизначне число!")