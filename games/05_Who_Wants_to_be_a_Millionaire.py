#QUIEN QUIERE SER MILLONARIO
#Autor: Alann Febres (Wally)
#------------------------------------------------
print(" ")
print("Bienvenidos a... Quien quiere ser Millonario❓")
print(" ")

print("Para ganar es super sencillo, debes responder una ronda de 10 preguntas")
print("Cada 3 preguntas obtendras premios por piso")
print("1er piso es por $50.000.- CLP")
print("2do piso por $100.000.- CLP")
print("3er piso por $500.000.- CLP")
print("4to y ultimo piso por $1.000.000.- CLP🎉🎉🎉")
print("")

piso0 = "$0.-CLP"
piso1 = "$10.000.-CLP"
piso2 = "$100.000.-CLP"
piso3 = "$500.000.- CLP"
piso4 = "$1.000.000.-CLP "
alternativa = ["a", "b", "c", "d"]
quiz = ["1er", "2da", "3ra", "4ta", "5ta", "6ta", "7ma", "8va", "9na", "10ma"]
question = ["Que pajaro tiene don?", "Cria cuervos y...?","Alex, Gloria y Melman fueron enviados a...?", "Cuantos años duro la guerra de los 100 años?", 
"Cuales eran los colores de la primera bandera Chile?", "De que nacionalidad era Juana de Arco", "En que año fallecio Napoleon?",
"De que marca fue la primera computadora?", "Como se llama el dueño de Virgin Mobile?", "Cuanto kilometros de largo tiene la muralla china"]

print("QUIEN QUIERE SER MILLONARIO INICIA AHORA")
print("")
preguntas = 1
while preguntas <= 10:
    rq1 = "a"    
    # if rq1 == alternativa[0] or rq1 == alternativa[1] or rq1 == alternativa[2] or rq1 == alternativa[3]:
    while rq1 == alternativa[0] or rq1 == alternativa[1] or rq1 == alternativa[2] or rq1 == alternativa[3]:  
        print(quiz[0],"pregunta:")
        print(question[0])
        print("a) El moscardon")
        print("b) El wombat")
        print("c) El camello")
        print("d) La mosca")
        rq1 = str.lower(input("Ingresa alternativa: ")) #Cambio de entrada de Mayuscula a Minuscula 
        if preguntas == 1 and rq1 == alternativa[0]:
            print("Si señoooor, respuesta correcta!!!")
            preguntas += 1
            print("")
        else:
            print("")
            print("Respuesta incorrecta, te vas con:", piso0)
            print("")
            preguntas = preguntas + 10
            break

        print(quiz[1],"pregunta:")
        print(question[1])
        print("a) Te sacaran las tripas")
        print("b) Te envenenaran")
        print("c) Te sacaran los ojos")
        print("d) Te daran un abrazo")
        rq2 = str.lower(input("Ingresa alternativa: "))
        if preguntas == 2 and rq2 == alternativa[2]:
            print("Si señoooor, respuesta correcta!!!")
            print("")
            preguntas += 1
        else:
            print("")
            print("Respuesta incorrecta, te vas con:", piso0)
            print("")
            preguntas = preguntas + 10
            break

        print(quiz[2],"pregunta:")
        print(question[2])
        print("a) Sumatra")
        print("b) Madagascar")
        print("c) Papua nueva ginea")
        print("d) Argentina")
        rq3 = str.lower(input("Ingresa alternativa: "))
        if preguntas == 3 and rq3 == alternativa[1]:
            print("Si señoooor, respuesta correcta!!!")
            print("")
            print("¡¡¡ YA TIENES EL", quiz[0],"PISO DE:",piso1, "!!!")
            preguntas += 1
        else:
            print("")
            print("Respuesta incorrecta, te vas con:", piso0)
            print("")
            preguntas = preguntas + 10
            break

        print("")
        print("VAMOS POR LAS SIGUIENTES PREGUNTAS Y EL SEGUNDO PISO")
        print("")
        #------------ 2do Piso ---------------#
        print(quiz[3],"pregunta:")
        print(question[3])
        print("a) 80 años")
        print("b) 150 años")
        print("c) 123 años")
        print("d) 116 años")
        rq4 = str.lower(input("Ingresa alternativa: "))
        if preguntas == 4 and rq4 == alternativa[3]:
            print("Si señoooor, respuesta correcta!!!")
            print("")
            preguntas += 1
        else:
            print("")
            print("Respuesta incorrecta, te vas con:", piso1)
            print("")
            preguntas = preguntas + 10
            break

        print(quiz[4],"pregunta:")
        print(question[4])
        print("a) Verde, Amarillo y Rojo")
        print("b) Cafe, Rosa, Blanco")
        print("c) Rojo, Celeste, Amarillo")
        print("d) Blanco, Amarillo, Azul")
        rq5 = str.lower(input("Ingresa alternativa: "))
        if preguntas == 5 and rq5 == alternativa[3]:
            print("Si señoooor, respuesta correcta!!!")
            print("")
            preguntas += 1
        else:
            print("")
            print("Respuesta incorrecta, te vas con:", piso1)
            print("")
            preguntas = preguntas + 10
            break

        print(quiz[5],"pregunta:")
        print(question[5])
        print("a) Alemania")
        print("b) Francia")
        print("c) Polonia")
        print("d) Italia")
        rq6 = str.lower(input("Ingresa alternativa: "))
        if preguntas == 6 and rq6 == alternativa[1]:
            print("Si señoooor, respuesta correcta!!!")
            print("")
            print("¡¡¡ YA TIENES EL", quiz[1],"PISO DE:",piso2, "!!!")
            print("")
            preguntas += 1
        else:
            print("")
            print("Respuesta incorrecta, te vas con:", piso1)
            print("")
            preguntas = preguntas + 10
            print("")
            break

        print("")
        print("VAMOS POR LAS SIGUIENTES PREGUNTAS Y EL TERCER PISO")
        print("")
        #------------ 3er Piso ---------------#

        print(quiz[6],"pregunta:")
        print(question[6])
        print("a) 1821")
        print("b) 1822")
        print("c) 1824")
        print("d) 1823")
        rq7 = str.lower(input("Ingresa alternativa: "))
        if preguntas == 7 and rq7 == alternativa[0]:
            print("Si señoooor, respuesta correcta!!!")
            print("")
            preguntas += 1
        else:
            print("")
            print("Respuesta incorrecta, te vas con:", piso2)
            print("")
            preguntas = preguntas + 10
            print("")
            break
        
        print(quiz[7],"pregunta:")
        print(question[7])
        print("a) Intel")
        print("b) IBM")
        print("c) Mac")
        print("d) HP")
        rq8 = str.lower(input("Ingresa alternativa: "))
        if preguntas == 8 and rq8 == alternativa[1]:
            print("Si señoooor, respuesta correcta!!!")
            print("")
            print("¡¡¡ YA TIENES EL", quiz[2],"PISO DE:",piso3, "!!!")
            print("")
            preguntas += 1
        else:
            print("")
            print("Respuesta incorrecta, te vas con:", piso2)
            print("")
            preguntas = preguntas + 10
            print("")
            break

        print("")
        print("VAMOS POR LAS SIGUIENTES PREGUNTAS Y EL CUARTO Y ULTIMO PISO")
        print("")
        #------------ 4to Piso ---------------#

        print(quiz[8],"pregunta:")
        print(question[8])
        print("a) Richard Branson")
        print("b) Steve Jobs")
        print("c) Elon Musk")
        print("d) Bill Gates")
        rq9 = str.lower(input("Ingresa alternativa: "))
        if preguntas == 9 and rq9 == alternativa[0]:
            print("Si señoooor, respuesta correcta!!!")
            print("")
            preguntas += 1
        else:
            print("")
            print("Respuesta incorrecta, te vas con:", piso3)
            print("")
            preguntas = preguntas + 10
            print("")
            break
        
        print(quiz[9],"pregunta:")
        print(question[9])
        print("a) 21.182 km")
        print("b) 22.000 km")
        print("c) 21.199 km")
        print("d) 21.196 km")
        rq8 = str.lower(input("Ingresa alternativa: "))
        if preguntas == 10 and rq8 == alternativa[3]:
            print("Si señoooor, respuesta correcta!!!")
            print("")
            print("FELICITACIONES, ERES EL FLAMANTE GANADOR DE...!!!")
            print("QUIEN QUIERE SER MILLONARIO ❓")
            print("¡¡¡ YA TIENES EL", quiz[3],"PISO DE:",piso4, "!!!")
            print("ERES UN CAMPEON 🌟🏆🌟")
            print("")            
            preguntas += 1
            break
        else:
            print("")
            print("Respuesta incorrecta, te vas con:", piso3)
            print("")
            preguntas = preguntas + 10
            print("")
            break

        # print(preguntas)
    
    else:
        print("")
        print("Valor ingresado incorrecto...")        
        print("")
        preguntas += 10
        


    # preguntas = preguntas + 10
    print("Juego terminado")



