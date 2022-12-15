#Galleta de la Fortuna
import random
print("")
print("Pidele 3 consejo a la Galleta de la Fortuna 🥠")
print("----------------------------------------------")
print("")
for i in range(3):
    i += 1
    #print("La galleta N°",i,"dice:")
    num = random.randint(1, 5)
    enter = input("Presiona enter para romper la galleta")
    print("")
    if num == 1:
        print("crunch🥠💥!")
        print("=> La galleta N°",i,"dice:")
        print("Hoy será un día maravilloso, aprovechalo!")
        print("")
    elif num == 2:
        print("crunch🥠💥!")
        print("=> La galleta N°",i,"dice:")
        print("Haz el bien y no mires a quien!")
        print("")
    elif num == 3:
        print("crunch🥠💥!")
        print("=> La galleta N°",i,"dice:")
        print("No mal gaste el dinero, invierte y traera frutos!")
        print("")
    elif num == 4:
        print("crunch🥠💥!")
        print("=> La galleta N°",i,"dice:")
        print("Trata de mantenerte quieto, no abuses de los excesos!")
        print("")
    else:
        print("crunch🥠💥!")
        print("=> La galleta N°",i,"dice:")
        print("Descansa!, a sido un largo trayecto")
        print("")
print("*********************************")
print("Adios y buena suerte en todo!!!")
print("*********************************")

