#ð«± Rock Paper Scissors
#Autor: Alann Febres (Wally)
#--------------------------------------------------------
print("Jugamos al ðª¨ ð â")
print("")
print("COMENCEMOS!!!")
i = "y"
while i == "y":
    print("Jugador 1Â°: Selecciona tu opcion indicando el numero")
    print("1) Piedra")
    print("2) Papel")
    print("3) Tijera")
    op1 = int(input("Ingresa tu opciÃ³n: "))
    print("")
    print("Jugador 2Â°: Selecciona tu opcion indicando el numero")
    print("1) Piedra")
    print("2) Papel")
    print("3) Tijera")
    op2 = int(input("Ingresa tu opciÃ³n: "))
    print("")
    print("-------------------------------------------------------------")
    print("")
    if op1 == 1 and op2 == 2:
        print("ð  gana a ðª¨ : Jugador 2 gana")
        i = input("Desean seguir jugando?: digita y o n : ")
        print("")
    elif op1 == 1 and op2 == 3:
        print("ðª¨  gana a â : Jugador 1 gana")
        i = input("Desean seguir jugando?: digita y o n : ")
        print("")
    elif op1 == 1 and op2 == 1:
        print("ðª¨  con ðª¨ : Empate")
        i = input("Desean seguir jugando?: digita y o n : ")
        print("")
    elif op1 == 2 and op2 == 1:
        print("ð  gana a ðª¨ : Jugador 1 gana")
        i = input("Desean seguir jugando?: digita y o n : ")
        print("")
    elif op1 == 2 and op2 == 2:
        print("ð  con ð : Empate")
        i = input("Desean seguir jugando?: digita y o n : ")
        print("")
    elif op1 == 2 and op2 == 3:
        print("â  gana a ð : Jugador 2 gana")
        i = input("Desean seguir jugando?: digita y o n : ")
    elif op1 == 3 and op2 == 1:
        print("ðª¨  gana a â : Jugador 2 gana")
        i = input("Desean seguir jugando?: digita y o n : ")
        print("")
    elif op1 == 3 and op2 == 2:
        print("â  gana a ð : Jugador 1 gana")
        i = input("Desean seguir jugando?: digita y o n : ")
        print("")
    elif op1 == 3 and op2 == 1:
        print("ðª¨  gana a â : Jugador 2 gana")
        i = input("Desean seguir jugando?: digita y o n : ")
        print("")
    elif op1 == 3 and op2 == 3:
        print("â  con â : Empate")
        i = input("Desean seguir jugando?: digita y o n : ")
        print("")
    else:
        i = input("Desean seguir jugando?: digita y o n : ")
else:
    print("")
    print("Gracias por Jugar Piedra, Papel y Tijera!!! ðª¨ ð â")














