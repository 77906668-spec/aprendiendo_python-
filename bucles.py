# bucle infinito
while True:
    print("Estoy atrapdo dentro de un bucle.")
tamanio_numero = -999999999

numero = int(input("Introduce un número o escribe -1 para detener: "))
while numero != -1:
    if numero > tamanio_numero:
        tamanio_numero = numero
    numero = int(input("Introduce un número o escribe -1 para detener: "))

print("El número más grande :", tamanio_numero)

odd_numbers = 0
even_numbers = 0

numero = int(input("Ingrese un número o escribe 0 para detener: "))

while numero != 0:
    # verificar si el número es impar
    if numero % 2 == 1:
        # incrementar el contador de números impares
        odd_numbers += 1
    else:
        # incrementar el contador de números pares
        even_numbers += 1
    numero = int(input("Ingrese un número o escribe 0 para detener: "))

print("Conteo de números impares:", odd_numbers)
print("Conteo de números pares:", even_numbers)

contador = 5
while contador != 0:
    print("Dentro del bucle.", contador)
    contador -= 1
print("Fuera del bucle.", contador)

numero_secreto = 29

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

numero = int(input("Ingresa un número entero: "))

while numero != numero_secreto:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    numero = int(input("Ingresa un número entero: "))

print(numero, "¡Es el número secreto! ¡Felicidades!")
print("¡Bien hecho, muggle! Eres libre ahora.")
