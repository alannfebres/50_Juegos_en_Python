#SIMULADOR TIRAR EL DADO
#Autor: Alann Febres (Wally)
#----------------------------------------------------------
import random
print("Simulador Arroja el Dado 🎲")
enter =  "y"
while enter == "y":
    print("")
    enter = input("Ingresa Y para arrojar el 🎲 - y N para terminar simulador: ")
    print("----------------------------------------------")
    print("")
    if enter == "y":
        dado = random.randint(1, 6)
        print("🔄 🔄 🔄 🔄 🔄 🔄 🔄 🔄 🔄 ")
        print("El resultado del dado es?:", dado)
    else:   
        print("🎲 🎲 🎲 🎲 🎲 🎲 🎲 🎲 🎲")
        print("Se guarda el Dado... Hasta la Proxima 😉👍")
        print("🎲 🎲 🎲 🎲 🎲 🎲 🎲 🎲 🎲")





















