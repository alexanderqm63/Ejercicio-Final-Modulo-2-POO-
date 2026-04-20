

"""Ejercicio Final Modulo 2 Programación Orientada a Objetos"""

"""Sistema de Gestión de la clinica Veterinaria el Perrito Wow Wow"""

#Se comienza creando la primera clase abstracta: "Persona" con la herramienta importada ABC

from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, documento): # Aqui aplicanos el metodo constructuror (con init) para crear la super clase "Persona"
        # Definimos los atributo de "Persona"
        self.nombre = nombre 
        self.documento = documento 

    @abstractmethod # Con esto indicamos  el metodo abstracto que van a heredar las posteriores clases hijas
    def mostrar_rol(self):
        pass

# Aqui empezamos a crear las clases herederas del padre ("Persona")

class Veterinario(Persona): #Aqui indicamos que la clse hija de veterinario herada de la clse padre "Persona"
    def __init__(self, nombre, documento, especialidad):
        super().__init__(nombre, documento) # Con "#Super()" llamamos los atributos de la clase padre para no tener que repetirlos en cada clase hija
        self.especialidad = especialidad #Aqui creamos el nuevo atrubuto exclusivo de esta clae hija

    def mostrar_rol(self): # Con esto buscamos que la clase hija implemente el metodo heredado de la clase padre
        print(f"{self.nombre} es un veterinario especialista en {self.especialidad}")

    def atender_mascota(self, mascota):# Aqui creamos el nuevo metodo exclusivo de esta clae hija
        print(f"El veterinario {self.nombre} está atendiendo a {mascota.nombre}")

class Cliente(Persona):
    def __init__(self, nombre, documento, telefono):
        super().__init__(nombre, documento)
        self.telefono = telefono
        self.mascotas = []  # Aqui estamos indicando al sistema que agregue a la lista las mascotas (Agregacion)

    def mostrar_rol(self):
        print(f"{self.nombre} es Cliente del hospital")

    def agregar_mascota(self, mascota): #Creamos el metodo para ingresar las mascotas del cliente
        self.mascotas.append(mascota) #Con el .append estaestamos indicando al sistema que agregue la mascota a la anterior lista de "mascotas"
        print(f"Mascota {mascota.nombre} agregada al cliente {self.nombre}")

    def mostrar_mascotas(self):
        print(f"Mascotas de {self.nombre}:")
        for i in self.mascotas:
            print(f" - {i.nombre} ({i.especie})")
            
class Recepcionista(Persona):
    def mostrar_rol(self):
        print(f"{self.nombre} es Recepcionista de la clinica Veterinaria")

    def registrar_cliente(self, cliente):
        print(f"Cliente {cliente.nombre} registrado por la recepcionista {self.nombre}")



# Aqui creamos la nueva clase de mascota, que va a estar en relación de agregación con la anterior clase de "cliente"
class Mascota:
    def __init__(self, nombre, especie, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def mostrar_info(self):
        print(f"{self.nombre}, {self.especie},Edad: {self.edad},Peso: {self.peso}kg")


# Aqui creamos la nueva clase de consulta, que va a estar en relación de composición con la subsiguiente clase de "tratamiento", y en asociación con "veterinario"

class Consulta:
    def __init__(self, mascota, veterinario, motivo):
        self.mascota = mascota
        self.veterinario = veterinario
        self.motivo = motivo
        self.diagnostico = "" # con (" ") indicamos que este atributo esta ahora vacio pero que se llena con la información que se diligencie en la consulta
        self.tratamientos = []  # Creamos la lista par alos tratamientos que se derivan de las consultas, en una realación de composición con ésta

    def crear_tratamiento(self, nombre, costo, duracion):
        nuevo = Tratamiento(nombre, costo, duracion) # crearmos la variable "nuevo" para traer los atributos de la posterior clase de "tratamiento"
        self.tratamientos.append(nuevo)
        print(f"Tratamiento '{nombre}' creado dentro de la consulta.")

    def mostrar_resumen(self):
        print("===== RESUMEN DE CONSULTA =====")
        print(f"Mascota: {self.mascota.nombre}")
        print(f"Veterinario: {self.veterinario.nombre}")
        print(f"Motivo: {self.motivo}")
        print(f"Diagnóstico: {self.diagnostico}")
        print("Tratamientos:")
        for t in self.tratamientos:
            t.mostrar_tratamiento()

    def calcular_costo_consulta(self):
        total = 70000  # Aqui colocamos cuanto cuesta la consulta
        for tratamiento in self.tratamientos: #Y con esto indicamos que para  tratamiento (t) guardado en la lista de "tratamientos" le sume el valor al costo total al tratamiento y lo retorne con el total
            total += tratamiento.costo
        return total

# Aqui creamos la nueva clase de tratamiento, que va a estar en relación de composición con la anterior clase de "cliente"

class Tratamiento:
    def __init__(self, nombre, costo, duracion_dias):
        self.nombre = nombre
        self.costo = costo
        self.duracion_dias = duracion_dias

    def mostrar_tratamiento(self):
        print(f"Tratamiento: {self.nombre}, Costo: {self.costo}, Duración: {self.duracion_dias} días")


#Continuamos creando la segunda  clase abstracta: "Metodo de pago" y hacemos polimorfismo

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass

#Creamos las clases hijas para cada metodo de pago

class PagoEfectivo(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Pago en efectivo recibido: ${monto}")
         

class PagoTarjeta(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Pago con tarjeta procesado por ${monto}")
        

class PagoTransferencia(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Pago por transferencia completado: ${monto}")
        

#Aqui craemos  la clase factura, que va a estar asocaida a la clase de consulta y metodo de pago

class Factura:
    def __init__(self, consulta):
        self.consulta = consulta
        self.subtotal = consulta.calcular_costo_consulta() #Traemos de una vez el costo de la consulta de la funcion de "Consulta"
        self.impuesto = self.subtotal * 0.19 #Al subtotal le damos de una vez el valor del IVA del servicio
        self.total = self.subtotal + self.impuesto #Finalmente al subtotal  le sumamos el valor del IVA

    def calcular_total(self): #Con este metodo mostramos el costo en la facutra
        print(f"Subtotal: ${self.subtotal}")
        print(f"Impuesto (19%): ${self.impuesto}")
        print(f"TOTAL A PAGAR: ${self.total}")

    def pagar(self, metodo_pago): # Usamos poliformismo para procesar el pago del coste anterior
        print("Procesando pago...")
        metodo_pago.procesar_pago(self.total)
        print("Pago completado. ¡Gracias por uasr los servicios de la clinica el Perrito Wow Wow!")


# Hacemos este codigo para probar que funcione el codigo anterior

if __name__ == "__main__":
    # Personas
    vet = Veterinario("Laura", "217765", "Cirugía")
    cliente = Cliente("Carlos", "218863", "3018001234")
    recep = Recepcionista("Ana", "1037853663")

    # Mascota
    mascota1 = Mascota("Chucho", "Perro", 5, 12.5)
    cliente.agregar_mascota(mascota1)
    
    mascota2 = Mascota("Michilin", "Gato", 10, 8)
    cliente.agregar_mascota(mascota2)

    # Registrar cliente
    recep.registrar_cliente(cliente)

    # Consulta
    consulta = Consulta(mascota1, vet, "Dolor en la pata")
    consulta.diagnostico = "Esguince leve"
    consulta.crear_tratamiento("Analgésicos", 15000, 5)
    consulta.crear_tratamiento("Reposo", 0, 3)

    consulta.mostrar_resumen()

    # Factura
    factura = Factura(consulta)
    factura.calcular_total()

    metodo = PagoTarjeta()
    factura.pagar(metodo)