
print("""
● Crear un array o arreglo unidimensional donde indique el tamaño por teclado y crear
una función que rellene el array o arreglo con los múltiplos de un número pedido
por teclado, por ejemplo, si define un array de tamaño 5 y elije un 3 en la
función, el array contendrá 3, 6, 9, 12, 15. Mostrarlos por pantalla usando
otra función distinta.

Pasos:
1. Pedir al usuario el tamaño del arreglo validando que sea entero. :)
2. Almacenar el valor dado en una variable. :)
3. Pedir al usuario el valor del cual se van a calcular los múltiplos. :)
4. Almacenar el valor dado en otra variable. :)
5. Crear la función que recibe por parámetro los valores de las dos variables y retorna los cálculos. :)
6. Almacenar el resultado en otra variable. :)
7. Crear otra función que reciba por parámetro el resultado y lo muestre por pantalla. :)
""")
def pedir_valor_entero():
    entero = 0
    contador = 0
    while contador < 1:
        try:
            validar = int(input(f"Ingrese un valor entero: "))
        except:
            validar = False
            contador = 0
            print("La entrada debe ser numérica.")
        if validar:
            entero = validar
            contador += 1
    return entero

def calcular_multiplos(rango, valor):
    multiplos = []
    for i in range(rango):
        multiplos.append(valor * (i + 1))
    return multiplos

def mostrar_resultado(rango, valor, resultado):
    print(f"Los primeros {rango} múltiplos de {valor} son: ")
    for i in range(rango):
        print(f"\t{i + 1}. {resultado[i]}")
    
print(f"========================= 4.5 CLACULAR MULTIPLOS =====================================")

print("Ingrese el tamaño del array:")
tamano = pedir_valor_entero()
print("Ingrese el valor para calcular sus múltiplos: ")
valor_multiplos = pedir_valor_entero()
resultado = calcular_multiplos(tamano, valor_multiplos)

mostrar_resultado(tamano, valor_multiplos, resultado)