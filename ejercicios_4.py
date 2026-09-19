# %%
#ejercicio 1
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p = Persona("Ana", 21)

print(p.nombre, p.edad)
# %%
#ejercicio 2
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


a = Persona("Ana", 21)
b = Persona("Luis", 30)
c = Persona("Carlos", 25)

for x in [a, b, c]:
    print(x.nombre)
# %%
#ejercicio 3
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


p = Persona("Luis", 30)

print(p.edad)

p.edad = 31

print(p.edad)
# %%
#ejercicio 4
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


a = Persona("Ana", 21)
b = Persona("Ana", 21)

a.edad = 40

print(a.edad, b.edad)
# %%
#ejercicio 5
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


p = Persona("Ana", 21)

print(p.nombre)
# %%
#ejercicio 6 
class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprobo(self):
        return self.nota >= 3.0


estudiante = Estudiante("Ana", 4.2)

print(estudiante.aprobo())
# %%
#ejercicio 7
class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def subir(self, puntos):
        self.nota = min(5.0, self.nota + puntos)
        return self.nota


e = Estudiante("Luis", 4.8)

print(e.subir(0.5))
# %%
#ejercicio 8 
class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def promedio_con(self, otra):
        return round((self.nota + otra) / 2, 2)


e = Estudiante("Sara", 3.0)

print(e.promedio_con(4.0))
# %%
#ejercicio 9
class Estudiante:
    total = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Estudiante.total += 1


Estudiante("Ana")
Estudiante("Luis")

print(Estudiante.total)
# %%
#ejercicio 10
#codigo_curso = "20000151"-atributo de clase
#self.nombre = nombre-atributo de instancia
#self.nota = nota-atributo de instancia
#nota_minima = 3.0-atributo de clase
# %%
#ejercicio 11
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def con_iva(self):
        return self.precio * 1.19


producto = Producto("Computador", 1000000)

print(producto.con_iva())
# %%
#ejercicio 12
class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def consultar(self):
        return self.__saldo


c = Cuenta(100)

print(c.consultar())
# %%
#ejercicio 13
class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def consultar(self):
        return self.__saldo

    def consignar(self, valor):
        if valor <= 0:
            return "Valor inválido"

        self.__saldo = self.__saldo + valor

        return self.__saldo


c = Cuenta(100)

print(c.consignar(-20))
print(c.consignar(50))
# %%
#ejercicio 14
class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def consultar(self):
        return self.__saldo

    def consignar(self, valor):
        if valor <= 0:
            return "Valor inválido"

        self.__saldo = self.__saldo + valor

        return self.__saldo

    def retirar(self, valor):
        if valor > self.__saldo:
            return "Fondos insuficientes"

        self.__saldo = self.__saldo - valor

        return self.__saldo


c = Cuenta(150)

print(c.retirar(200))
# %%
#ejercicio 15
class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return f"{self.nombre}: {self.nota}"


estudiante = Estudiante("Ana", 4.2)

print(estudiante)
# %%
#ejercicio 16
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


class Estudiante(Persona):
    def __init__(self, nombre, nota):
        Persona.__init__(self, nombre)
        self.nota = nota


estudiante = Estudiante("Ana", 4.2)

print(estudiante.nombre)
# %%
#ejercicio 17
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"Hola, soy {self.nombre}"


class Estudiante(Persona):
    def __init__(self, nombre, nota):
        Persona.__init__(self, nombre)
        self.nota = nota

    def saludar(self):
        return f"Soy {self.nombre} y mi nota es {self.nota}"


estudiante = Estudiante("Ana", 4.2)

print(estudiante.saludar())
# %%
#ejercicio 18
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"Hola, soy {self.nombre}"


class Estudiante(Persona):
    def __init__(self, nombre, nota):
        Persona.__init__(self, nombre)
        self.nota = nota

    def saludar(self):
        return f"Soy {self.nombre} y mi nota es {self.nota}"


grupo = [
    Persona("Sara"),
    Estudiante("Ana", 4.2)
]


for p in grupo:
    print(p.saludar())
# %%
#ejercicio 19
# Un docente es una persona -> Herencia
# Un curso tiene estudiantes -> Composición
# Una cuenta de ahorros es una cuenta -> Herencia
# Una biblioteca tiene libros ->  Composición
# %%
#ejercicio retador 
class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def inscribir(self, estudiante):
        self.estudiantes.append(estudiante)

    def promedio(self):
        if len(self.estudiantes) == 0:
            return 0

        suma = sum(e.nota for e in self.estudiantes)

        return round(suma / len(self.estudiantes), 2)


class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota


curso = Curso("Programación para Analítica de Datos")

estudiante1 = Estudiante("Ana", 4.2)
estudiante2 = Estudiante("Luis", 3.1)
estudiante3 = Estudiante("Carlos", 2.7)

curso.inscribir(estudiante1)
curso.inscribir(estudiante2)
curso.inscribir(estudiante3)

print(curso.promedio())
# %%
#ejercicio 21
class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprobo(self):
        return self.nota >= 3.0


class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def inscribir(self, estudiante):
        self.estudiantes.append(estudiante)

    def reporte(self):
        aprobados = 0
        mejor = self.estudiantes[0]

        for e in self.estudiantes:
            if e.aprobo():
                aprobados = aprobados + 1

            if e.nota > mejor.nota:
                mejor = e

        return f"{aprobados} aprobados · mejor: {mejor.nombre}"


curso = Curso("Programación para Analítica de Datos")

curso.inscribir(Estudiante("Ana", 4.5))
curso.inscribir(Estudiante("Luis", 2.8))
curso.inscribir(Estudiante("Carlos", 3.2))

print(curso.reporte())
# %%
#ejercicio 22
class Vehiculo:
    def __init__(self, placa, tipo, hora_entrada):
        self.placa = placa
        self.tipo = tipo
        self.hora_entrada = hora_entrada


class Parqueadero:
    def __init__(self):
        self.vehiculos = []

    def recibir(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def entregar(self, placa):
        for vehiculo in self.vehiculos:
            if vehiculo.placa == placa:
                self.vehiculos.remove(vehiculo)
                return "Vehículo entregado"

        return "Vehículo no encontrado"

    def cantidad(self):
        return len(self.vehiculos)


parqueadero = Parqueadero()

vehiculo1 = Vehiculo("ABC123", "Carro", "08:00")
vehiculo2 = Vehiculo("XYZ789", "Moto", "09:30")

parqueadero.recibir(vehiculo1)
parqueadero.recibir(vehiculo2)

print(parqueadero.cantidad())

print(parqueadero.entregar("ABC123"))

print(parqueadero.cantidad())
# %%
