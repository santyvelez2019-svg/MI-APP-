# =============================================================
# Tema 01 · Variables, tipos, entrada y salida · EJEMPLOS
# python-adso · SENA ADSO
#
# Cómo usar este archivo:
#   1. Léelo de arriba a abajo. Cada línea con # es una explicación.
#   2. Ejecútalo:  python ejemplos.py
#   3. Cambia algo en cada ejemplo y vuelve a ejecutarlo.
# =============================================================


# -------------------------------------------------------------
# EJEMPLO 1 · print(): mostrar en pantalla
# -------------------------------------------------------------
# print() muestra en la terminal lo que pongas entre paréntesis.
# El texto va entre comillas: "así" o 'así'.

print("=== EJEMPLO 1: print() ===")
print("Hola, bienvenido a mi primera app en Python")
print("Esta es otra línea")
print()  # un print() vacío deja una línea en blanco


# -------------------------------------------------------------
# EJEMPLO 2 · Variables y tipos de dato
# -------------------------------------------------------------
# Una variable es una caja con nombre donde guardas un dato.
# Se crea con el signo =  (se lee "guarda en").
#
# Los tres tipos que más vas a usar:
#   str   → texto            "Barbería El Corte"
#   int   → número entero    12
#   float → número decimal   25000.50

print("=== EJEMPLO 2: variables ===")
negocio = "Barbería El Corte"   # str
sillas = 3                      # int
precio_corte = 25000.0          # float

print(negocio)
print(sillas)
print(precio_corte)

# type() te dice de qué tipo es una variable
print(type(negocio))
print(type(sillas))
print(type(precio_corte))
print()


# -------------------------------------------------------------
# EJEMPLO 3 · f-strings: mezclar texto y variables
# -------------------------------------------------------------
# Pon una f antes de las comillas y escribe las variables
# entre llaves { }. Python las reemplaza por su valor.

print("=== EJEMPLO 3: f-strings ===")
producto = "Pan"
cantidad = 12
precio = 800

print(f"Producto: {producto}")
print(f"Tengo {cantidad} unidades de {producto}")

# Dentro de las llaves también puedes hacer cuentas
print(f"Valor del inventario: {cantidad * precio} pesos")

# :, pone separador de miles · :.2f muestra 2 decimales
total = 1234567.891
print(f"Total con separador: {total:,.0f}")
print(f"Total con 2 decimales: {total:.2f}")
print()


# -------------------------------------------------------------
# EJEMPLO 4 · input(): preguntarle al usuario
# -------------------------------------------------------------
# input() muestra una pregunta, espera a que el usuario escriba
# y presione Enter, y devuelve lo que escribió.
# OJO: input() SIEMPRE devuelve texto (str).

print("=== EJEMPLO 4: input() ===")
nombre = input("¿Cómo te llamas? ")
ciudad = input("¿En qué ciudad vives? ")

print(f"Mucho gusto, {nombre}. Saludos a {ciudad}.")
print()


# -------------------------------------------------------------
# EJEMPLO 5 · int() y float(): convertir texto en número
# -------------------------------------------------------------
# Si vas a hacer cuentas con lo que escribió el usuario,
# primero conviértelo a número.
#   int("25")      → 25
#   float("3.5")   → 3.5

print("=== EJEMPLO 5: convertir a número ===")

# Así NO funciona: se pegan los textos
a = input("Escribe un número: ")
b = input("Escribe otro número: ")
print(f"Sin convertir: {a} + {b} = {a + b}")   # "5" + "5" = "55"

# Así SÍ funciona: convertimos primero
a = int(a)
b = int(b)
print(f"Convertidos:   {a} + {b} = {a + b}")   # 5 + 5 = 10
print()


# -------------------------------------------------------------
# EJEMPLO 6 · Todo junto: un préstamo entre amigos
# -------------------------------------------------------------
# Un programa pequeño que usa todo lo anterior:
# pregunta datos, convierte, calcula y muestra un resumen.

print("=== EJEMPLO 6: préstamo ===")
amigo = input("¿A quién le prestaste? ")
monto = float(input("¿Cuánto le prestaste? "))
cuotas = int(input("¿En cuántas cuotas te va a pagar? "))

valor_cuota = monto / cuotas

print()
print("---- RESUMEN DEL PRÉSTAMO ----")
print(f"Amigo:          {amigo}")
print(f"Monto:          ${monto:,.0f}")
print(f"Cuotas:         {cuotas}")
print(f"Valor de cuota: ${valor_cuota:,.0f}")
print("------------------------------")


# =============================================================
# RETO RÁPIDO (no se entrega)
# Cambia el ejemplo 6 para que también pregunte el interés en %
# y muestre cuánto pagará en total.  Pista: monto * (1 + interes / 100)
# =============================================================