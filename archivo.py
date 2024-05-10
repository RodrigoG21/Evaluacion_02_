#Numeros <=15
#generar una lista del 0 al numero 
#pedir al usuario numero x que este en la lista
#sorteo:
#crear loop que recorre lista y saque numero al azar, decir el numero, si el numero es el ganador fin si no vuelve a mezclar
#aca le pediremos el numero limite al usuario
from random import shuffle
from os import system
print('¡BIENVENIDO AL SORTEO!')
list = [0]
obtenidos = [0]
while True:
    try:
        lim = int(input('Por favor, Ingresa un numero para generar el sorteo:\n'))
    except:
        system('cls')
        print('ERROR, ingresa numero valido.')
    if lim <1 or lim >15:
        system('cls')
        print('El numero debe estar entre 1 y 15\n')
    else:
        break
for i in range(lim):
    list.append(i+1)
while True:
    try:
        win = int(input('ingresa un numero ganador'))
    except:
        system('cls')
        print('Error:Ingresa numero')
    if win not in list:
        system('cls')
        print('Error debe ser un numero valido\n')
    else:
        system('cls')
        break
while True:
    shuffle(list)
    num = list[0]
    print(f'El numero obtenido es:{num}', end ='')
    obtenidos.append(num)
    del list[0]
    if num == win:
        print('Es el numero ganador!')
        print(f'Los numeros que aparecieron en el sorteo fueron:', end = '')
        break
    else:
        print('Mala suerte, intentalo otra vez')


    
