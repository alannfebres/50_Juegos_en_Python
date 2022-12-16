#🫱 Rock Paper Scissors
#Autor: Alann Febres (Wally)
#--------------------------------------------------------
print("Jugamos al 🪨 📄 ✂")
print("")
print("COMENCEMOS!!!")
i = "y"
while i == "y":
    print("Jugador 1°: Selecciona tu opcion indicando el numero")
    print("1) Piedra")
    print("2) Papel")
    print("3) Tijera")
    op1 = int(input("Ingresa tu opción: "))
    print("")
    print("Jugador 2°: Selecciona tu opcion indicando el numero")
    print("1) Piedra")
    print("2) Papel")
    print("3) Tijera")
    op2 = int(input("Ingresa tu opción: "))
    print("")
    print("-------------------------------------------------------------")
    print("")
    if op1 == 1 and op2 == 2:
        print("📄  gana a 🪨 : Jugador 2 gana")
        i = input("Desean seguir jugando?: digita y o n : ")
        print("")
    elif op1 == 1 and op2 == 3:
        print("🪨  gana a ✂ : Jugador 1 gana")
        i = input("Desean seguir jugando?: digita y o n : ")
        print("")
    elif op1 == 1 and op2 == 1:
        print("🪨  con 🪨 : Empate")
        i = input("Desean seguir jugando?: digita y o n : ")
        print("")
    elif op1 == 2 and op2 == 1:
        print("📄  gana a 🪨 : Jugador 1 gana")
        i = input("Desean seguir jugando?: digita y o n : ")
        print("")
    elif op1 == 2 and op2 == 2:
        print("📄  con 📄 : Empate")
        i = input("Desean seguir jugando?: digita y o n : ")
        print("")
    elif op1 == 2 and op2 == 3:
        print("✂  gana a 📄 : Jugador 2 gana")
        i = input("Desean seguir jugando?: digita y o n : ")
    elif op1 == 3 and op2 == 1:
        print("🪨  gana a ✂ : Jugador 2 gana")
        i = input("Desean seguir jugando?: digita y o n : ")
        print("")
    elif op1 == 3 and op2 == 2:
        print("✂  gana a 📄 : Jugador 1 gana")
        i = input("Desean seguir jugando?: digita y o n : ")
        print("")
    elif op1 == 3 and op2 == 1:
        print("🪨  gana a ✂ : Jugador 2 gana")
        i = input("Desean seguir jugando?: digita y o n : ")
        print("")
    elif op1 == 3 and op2 == 3:
        print("✂  con ✂ : Empate")
        i = input("Desean seguir jugando?: digita y o n : ")
        print("")
    else:
        i = input("Desean seguir jugando?: digita y o n : ")
else:
    print("")
    print("Gracias por Jugar Piedra, Papel y Tijera!!! 🪨 📄 ✂")














