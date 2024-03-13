print("""
 ●	Crear un vector de 5 elementos de cadenas de caracteres, inicialice el vector
con datos leídos por el teclado. Copie los elementos del vector en otro vector,
pero en orden inverso y muéstrelo por la pantalla.

Pasos:
1. Pedir al usuario los elementos. :)
2. Almacenar los valores en una variable. :)
3. Crear otra variable con los elementos en orden inverso. :)
4. Mostras por consola los resultados. :)
""")
print(f"========================= 4.2 VECTOR INVERSO =====================================")
vector_original = [input(f"Ingrese el elemento {i + 1}: ")  for i in range(5)]

####Se utiliza un bucle en vez de los métodos nativos del lenguaje atendiendo 
#### al sentido didáctico de la actividad. ( vector_inverso = vector_original[::-1] )

contador = len(vector_original)
vector_inverso = []
while contador >= 0:
    vector_inverso.append(vector_original[contador - 1])
    contador -= 1

print(f"========================= 4.2 VECTOR INVERSO =====================================")
print("Vector Original:", vector_original)
print("Vector Inverso:", vector_inverso)
print(f"==================================================================================")