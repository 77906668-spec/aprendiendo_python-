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

# break - ejemplo

print("La instrucción break:")
for i in range(1, 6):
        pass
        print("Dentro del bucle.", i)
print("Fuera del bucle.")

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

largest_number = -99999999
counter = 0

while True:
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")

largest_number = -99999999
counter = 0

number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

if counter:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")

i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)


print("=== Dato 1: entrada 6 ===")
bloques = 6
altura = 0
capa = 1
while capa <= bloques:
    print(f"{bloques} - {capa} = {bloques - capa}   (capa {capa})")
    bloques -= capa
    altura += 1
    capa += 1
print(f"La capa {capa} necesita {capa} y quedan {bloques}: no alcanza.")
print("La altura de la pirámide:", altura) 
