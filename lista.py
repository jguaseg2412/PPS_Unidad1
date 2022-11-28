def estaEnRango(numero, min, max):
    if numero > max:
        print("Has introducido un numero mayor al intervalo estipulado")
        return False
    elif numero < min:
        print("Has introducido un numero menor al intervalo estipulado")
        return False
    else:
        print("Has introducido un numero  con las caracteristics correctas")
        return True

def estaEnLista(numero, lista):

    find = 0

    for numeros in lista:
        if numero == numeros:
            find = 1
    if find == 1:
        print("El numero está en la lista")
        return True
    else:
        print("El numero no esta en la lista")
        return False
    
numero = int(input("Introduzca un numero entre 1 y 20: "))
min = 1
max = 20

estaEnRango(numero, min, max)

lista = [5, 14, 11, 3, 2, 1, 15, 19]

valor = int(input("Introduzca el numero de nuevo: "))
estaEnLista(valor, lista)