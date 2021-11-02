import random
x = int (input ("¿Cual quieres que sea el valor mas pequeño que puede alcanzar el numero aleatorio? "))
y = int (input ("¿Y el mas grande? "))
num = random.randint(x,y)

contador = 0

while num:
    intento = int (input ("Diga un numero, entre " + str(x) + " y " + str(y) + " ambos incluidos: "))
    if intento < num:
        print ("Demasiado pequeño")
        contador += 1
    elif num < intento:
        print ("Demasiado grande")
        contador += 1
    else:
        print ("¡Ha ganado! ✌ ")
        num = False
        contador += 1
        print ("Ha necesitado ", contador, " intentos para conseguirlo!")