# %%
#ejercicio 1
notas = [4.5, 3.0, 5.0, 3.2, 1.5]
print(len(notas))
print(notas)

# %%
#ejercicio 2
temperaturas = [18, 20, 19, 21, 22]
print(temperaturas[0])
print(temperaturas[2])
print(temperaturas[4])
# %%
#ejercicio 3
ventas = [120, 80, 200, 50]
ventas[1] = 85
print(ventas)

# %%
#ejercicio 4
notas = [3.5, 4.0, 2.8]
notas.append(4.6)
ultima = notas.pop()
print(ultima)
print(notas)

# %%
#ejercicio 5
notas = [4.2, 3.8, 5.0, 2.9]
total = 0
for nota in notas:
 total = total + nota
promedio = total / len(notas)
print(round(promedio, 2))

# %%
#ejercicio 6
notas = [4.2, 2.5, 3.0, 1.8, 4.7]
aprobados = 0
for nota in notas:
 if nota >= 3.0:
    aprobados = aprobados + 1
print(aprobados)

# %%
#ejercicio 7
lecturas = [18, 200, 21, -99, 19, 22]
validas = []
for t in lecturas:
 if t >= -10 and t <= 50:
    validas.append(t)
print(validas)

# %%
#ejercicio 8
montos = [120000, 85000, 210000, 50000]
ordenados = sorted(montos)
print(montos)
print(ordenados)
# %%
#ejercicio 9
numeros = [1, 2, 3, 4, 5, 6]
cuadrados_pares = [n**2 for n in numeros if n % 2 == 0]
print(cuadrados_pares)
# %%
#ejercicio 10
matriz = [[1, 2, 3], [4, 5, 6]]
total = 0

for fila in matriz:
    for valor in fila:
        total += valor

print(total)
# %%
#ejercico 11
ubicacion = (4.7110, -74.0721)

print(ubicacion)
print(type(ubicacion))
# %%
#ejercicio 12
registro = ("A01", "Laura", 4.6)

codigo, nombre, nota = registro

print(nombre)
print(nota)
# %%
#ejercicio 13
codigo = ("A01",)

print(codigo)
print(type(codigo))
# %%
#ejercico 14
columnas = ["fecha", "monto", "cliente"]
columnas_fijas = tuple(columnas)

print(columnas_fijas)
# %%
#ejercicio 15
def resumen(valores):
    menor = min(valores)
    mayor = max(valores)
    return menor, mayor

minimo, maximo = resumen([8, 3, 10, 5])

print(minimo, maximo)
# %%
#ejercicio 16 
punto = (10, 20)
punto[0] = 99
print(punto)
#La línea punto[0] = 99 intenta cambiar el 10 por 99, pero una tupla no permite modificaciones.
# %%
#ejercicio 17
lecturas = {}
coordenada = (4.65, -74.05)

lecturas[coordenada] = 18.5

print(lecturas[(4.65, -74.05)])
# %%
#ejercicio 18
nombres = ["Ana", "Luis", "Marta"]
notas = [4.2, 3.8, 5.0]

pares = list(zip(nombres, notas))

print(pares)
# %%
#ejercicio 19
estudiante = {
    "codigo": "A01",
    "nombre": "Laura",
    "nota": 4.6
}

print(estudiante)
# %%
#ejercicio 20
cliente = {"nombre": "Carlos", "puntaje": 720}
saldo = cliente.get("saldo", 0)
print(saldo)
# %%
#ejercicio 21
producto = {"codigo": "P01", "stock": 8}
producto["stock"] = producto["stock"] - 3

print(producto["stock"])
# %%
#ejercicio 22
producto = {"codigo": "P01", "precio": 12000, "stock": 8}

for clave, valor in producto.items():
    print(clave, valor)
# %%
#ejercicio 23 
tipos = ["Debito", "Credito", "Debito", "Debito", "Credito"]
conteo = {}

for tipo in tipos:
    conteo[tipo] = conteo.get(tipo, 0) + 1

print(conteo)
# %%
#ejercicio 24
tipos = ["Debito", "Credito", "Debito", "Debito", "Credito"]
conteo = {}

for tipo in tipos:
    conteo[tipo] = conteo.get(tipo, 0) + 1

print(conteo)
# %%
#ejercico 25
transacciones = [
    {"id": "T01", "monto": 120000},
    {"id": "T02", "monto": 85000},
    {"id": "T03", "monto": 210000}
]

total = 0

for t in transacciones:
    total += t["monto"]

print(total)
# %%
#ejercicio 26
estudiantes = [
    {"codigo": "A01", "nombre": "Laura"},
    {"codigo": "A02", "nombre": "Luis"}
]

buscado = "A02"
resultado = None

for e in estudiantes:
    if e["codigo"] == buscado:
        resultado = e["nombre"]

print(resultado)
# %%
#ejercicio 27
estudiantes = [
    {"nombre": "Ana", "nota": 4.2},
    {"nombre": "Luis", "nota": 2.8},
    {"nombre": "Marta", "nota": 3.5}
]

aprobados = []

for e in estudiantes:
    if e["nota"] >= 3.0:
        aprobados.append(e["nombre"])

print(aprobados)
# %%
#ejercicio 28
clientes = [
    {"nombre": "Ana", "riesgo": "bajo"},
    {"nombre": "Luis", "riesgo": "alto"},
    {"nombre": "Marta", "riesgo": "bajo"}
]

grupo = {}

for c in clientes:
    riesgo = c["riesgo"]
    if riesgo not in grupo:
        grupo[riesgo] = []
    grupo[riesgo].append(c["nombre"])

print(grupo)
# %%
#ejercicio 29
inventario = [
    {"producto": "Marcador", "stock": 4},
    {"producto": "Cuaderno", "stock": 20},
    {"producto": "Borrador", "stock": 2}
]

bajos = []

for item in inventario:
    if item["stock"] < 5:
        bajos.append(item["producto"])

print(bajos)
# %%
#ejercico 30 reto integrador 
transacciones = [
    {"cliente": "Ana", "tipo": "Credito", "monto": 120000},
    {"cliente": "Luis", "tipo": "Debito", "monto": 85000},
    {"cliente": "Marta", "tipo": "Credito", "monto": 210000}
]

total_creditos = 0
clientes = []

for t in transacciones:
    if t["tipo"] == "Credito" and t["monto"] >= 100000:
        total_creditos += t["monto"]
        clientes.append(t["cliente"])

print(total_creditos)
print(clientes)
# %%
"""
Lista: almacena las transacciones y la lista de clientes.
Diccionario: guarda los datos de cada transacción mediante claves como "cliente", "tipo" y "monto".
Ciclo for: recorre las transacciones.
Condicional if: filtra los créditos de mínimo 100000.
Acumulador: total_creditos suma los montos.
append(): agrega los clientes que cumplen la condición.

"""
# %%
#auto evaluacion 
"""
1. ¿Puedo elegir entre lista, tupla y diccionario según el problema?
2. ¿Puedo recorrer una colección y acumular un resultado?
3. ¿Puedo filtrar registros dentro de una lista de diccionarios?
4. ¿Puedo explicar por qué una tupla no admite asignación por índice?
"""
# %%
"""
Sí, puedo elegir la estructura adecuada según el problema: lista para colecciones modificables, tupla para datos que no deben cambiar y diccionario para datos organizados por claves y valores.
Sí, puedo recorrer una colección con for y acumular resultados usando una variable acumuladora.
Sí, puedo filtrar registros usando for e if dentro de una lista de diccionarios.
Sí, porque las tuplas son inmutables, es decir, una vez creadas no se pueden modificar sus elementos mediante índices.
"""
# %%
