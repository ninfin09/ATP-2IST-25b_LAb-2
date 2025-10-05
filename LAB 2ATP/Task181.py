numbers = [231, 255 ,178]
for num in numbers:
    # двійкове представлення з 8 бітами
    binary = format(num, '08b')
    # перевірка на паліндром
    if binary == binary[::-1]:
        print(True)
    else:
        print(False)