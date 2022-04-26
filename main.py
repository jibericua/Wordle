import string
import random
import time

print("Dificultades disponibles: \n 1 (4 letras) \n 2 (5 letras) \n 3 (6 letras)")
dificultad = input("Ingresarla aqui: ")

if dificultad == "1":
    palabra = "----"
    f = open("C:\\Users\\alumno\\Desktop\\wordle\\facil.txt", "r")
    lista = f.readlines()
    f.close()
    palabraParaAdivinar = random.choice(lista)
elif dificultad == "2":
    palabra = "-----"
    f = open("C:\\Users\\alumno\\Desktop\\wordle\\normal.txt", "r")
    lista = f.readlines()
    f.close()
    palabraParaAdivinar = random.choice(lista)
elif dificultad == "3":
    palabra = "-----"
    f = open("C:\\Users\\alumno\\Desktop\\wordle\\dificil.txt", "r")
    lista = f.readlines()
    f.close()
    palabraParaAdivinar = random.choice(lista)

start = time.perf_counter()
print("Tiempo inicio: 0")


palabraParaAdivinar = palabraParaAdivinar.upper()
resultadoP = ""
resultadoC = ""

dicc = [string.ascii_uppercase]


while palabra != palabraParaAdivinar:
    palabra = str(input("Ingrese una palabra: "))
    palabra = palabra.upper()
    palabraParaAdivinar = palabraParaAdivinar.rstrip("\n")


    if len(palabra) != len(palabraParaAdivinar): 
        print("La cantidad de caracteres ", len(palabra), " no es correcta. Deben ser ", len(palabraParaAdivinar))
    elif len(palabra) == len(palabraParaAdivinar):

        letras = []
        correcion = []

        for i in range(len(palabraParaAdivinar)):
            if palabra[i] == palabraParaAdivinar[i]:
                letras.append(palabra[i])
                correcion.append("=")
            elif palabra[i] in palabraParaAdivinar:
                if palabra.count(palabra[i]) <= palabraParaAdivinar.count(palabra[i]):
                    letras.append(palabra[i])
                    correcion.append("-")
                else:
                    letras.append(palabra[i])
                    correcion.append("x")
            else:
                letras.append(palabra[i])
                correcion.append("x")
            
        for x in range(len(palabra)):
            resultadoP += " " + palabra[x]
            resultadoC += " " + correcion[x]
        
        print(resultadoP)
        print(resultadoC)
        resultadoC = ""
        resultadoP = ""

end = time.perf_counter()
final = int(end - start)
print("Tardaste ", final, " segundos.")