#Введення кольорів
color1 = input("Введіть перший колір (red, green, blue) : ")
color2 = input("Введіть другий колір (red, green, blue): ")
#Перевірка  правильності вводу кольорів
valid_colors = ["red", "green", "blue"]
if color1 not in valid_colors or color2 not in valid_colors:
    print("Відсутня така палітра.")
elif color1 == color2:
    print("Ви ввели однакові кольори:", color1)
else:
#Можливі комбінації кольорів
    if(color1 == "red" and color2 == "green") or (color1 == "green" and color2 == "red"):
        print("Yellow")
    elif(color1 == "blue" and color2 == "green") or (color1 == "green" and color2 == "blue"):
        print("Cyan")
    elif(color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
        print("Magenta")