
print("""
●	Crear un array o arreglo unidimensional con un tamaño de 5, asignar los
valores numéricos manualmente (los que quiera) y mostrarlos por pantalla.
Pasos:
1. Crear un arreglo unidimensional con un tamaño de 5. :)
2. Asignar valores manualmente. :)
3. Mostrar los valores por pantalla. :)

""")
array = [0] * 5

array[0] = 10
array[1] = 20
array[2] = 30
array[3] = 40
array[4] = 50
print(f"========================= 4.4 ARREGLO UNIDIMENSIONAL =====================================")

print("Valores del arreglo:")
for valor in array:
    print(valor)