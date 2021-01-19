num = int(input("Ingresa un numero para multiplicar: "))

for n in range (1,10):
    print("Tabla del ",num)
    for y in range (1,11):
        print(y ,"*", num ,"=", y * num)