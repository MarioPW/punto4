from random import randint
print(f"========================= 4.3 ORDENAR VALORES ALEATORIOS ====================================="
"""
 ●	Hacer un programa que inicialice un vector de números con valores aleatorios y posteriormente
 ordene los elementos de menor a mayor.

Pasos:
1. Crear el vector con valores aleatorios. :)
2. Almacenar los valores en una variable. :)
3. Ordenar mediante un bucle los vaores. :)
4. Mostrar el resultado. :)
""")

#### Se utiliza un bucle en vez de los métodos nativos del lenguaje atendiendo 
#### al sentido didáctico de la actividad. ( método sort() )

valores_aleatorios = [ randint(0, 999) for i in range(12) ] # Se agregan 12 valores por comodidad.

print(f"Lista de valores aleatorios:")
print(valores_aleatorios)
n = len(valores_aleatorios)
for i in range(n):
    for j in range(0, n-i-1):
        if valores_aleatorios[j] > valores_aleatorios[j+1]:
            valores_aleatorios[j], valores_aleatorios[j+1] = valores_aleatorios[j+1], valores_aleatorios[j]

print(f"Lista de valores ordenados:")
print(valores_aleatorios)