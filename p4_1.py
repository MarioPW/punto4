
print("""
 ●	Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno
(comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media,
la nota más alta que ha sacado y la menor.

Pasos:
1. Pedir al usuario las notas.
    1.1 Validar que las notas estén en el rango correcto. :)
    1.2 Almacenar las notas en una variable. :)
2. Calcular la nota media. :)
3. Calcular la nota mas alta. :)
4. Calcular la nota menor. :)
5. Mostrar los resultados. :)
""")

class Calculadora_notas():
    def __init__(self, notas = 0) -> None:
        self.notas = notas

    def calcular_nota_media (self):
        sumatoria_notas = 0
        for i in range(len(self.notas)):
            sumatoria_notas += self.notas[i]
        return sumatoria_notas / 5

    def calcular_nota_alta (self):
        nota_mas_alta = 0
        for i in range(len(self.notas)):
            if self.notas[i] > nota_mas_alta:
                nota_mas_alta = self.notas[i]
        return nota_mas_alta

    def calcular_nota_menor (self):
        nota_menor = sum(self.notas)
        print(nota_menor)
        for i in range(len(self.notas)):
            if self.notas[i] < nota_menor:
                nota_menor = self.notas[i]
        return nota_menor
    

print(f"========================= 4.1 NOTAS =====================================")
notas = []
while len(notas) < 5:
    try:
        nota = int(input(f"Ingrese la nota en el indice {len(notas)}: "))
    except:
        nota = None
        print("La nota debe ser numérica.")
    if nota in range(0,10):
        notas.append(nota)
    else:
        print("La nota debe estar enrte 1 y 10.")


resultados = Calculadora_notas(notas)
nota_media = resultados.calcular_nota_media()
nota_mas_alta = resultados.calcular_nota_alta()
nota_menor = resultados.calcular_nota_menor()

print(f"========================= 4.1 NOTAS =====================================")
print(f"Notas: {notas} \nNota Media: {nota_media} \nNota mas Alta: {nota_mas_alta}\nNota Menor: {nota_menor}")
print(f"=========================================================================")
