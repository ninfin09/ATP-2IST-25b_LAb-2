#Введення координат
x = int(input("Введіть x: "))
y = int(input("Введіть y: "))
#Визначення чвертних координат площини
if x > 0 and y > 0:
    print("I")
elif x < 0 and y > 0:
    print("II")
elif x < 0 and y < 0:
    print("III")
else:
    print("IV")