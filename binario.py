def binarioDecimal(strbinario):
    num_dec = 0

    for posicion, digito in enumerate(strbinario[::-1]):
        num_dec += int(digito) * 2 ** posicion

    print(f"La conversión del numero binario {strbinario} es: {num_dec}")
    return num_dec
    
def esBinario(strbinario):
    for numeros in strbinario:
        if((numeros == "0") or (numeros == "1")):
            print("Has introducido un numero  binario")

            binarioDecimal(strbinario)
            return True
        else:
            print ("Has introducido un numero que no es binario")
            return False
        
unidad = input("Bienvenido al programa. Introduce un numero del tipo binario: ")
esBinario(unidad)

