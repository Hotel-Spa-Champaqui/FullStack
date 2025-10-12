class Reserva:
    def __init__(self, nombre, fecha, habitacion):
        self._nombre = nombre
        self._fecha = fecha
        self._habitacion = habitacion

    # Propiedades
    @property
    def nombre(self):
        return self._nombre

    @property
    def fecha(self):
        return self._fecha

    @property
    def habitacion(self):
        return self._habitacion

    # Métodos
    def mostrar(self):
        print(f"Reserva: {self.nombre} | Fecha: {self.fecha} | Habitación: {self.habitacion}")

    def es_valida(self):
        return all([self.nombre, self.fecha, self.habitacion])


class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.reservas = []

    def agregar_reserva(self, reserva):
        if reserva.es_valida():
            self.reservas.append(reserva)
            print("✅ Reserva agregada correctamente.")
        else:
            print("⚠️ La reserva no es válida.")

    def mostrar_reservas(self):
        print(f"\n📋 Reservas en {self.nombre}:")
        for i, r in enumerate(self.reservas):
            print(f"{i+1}. ", end="")
            r.mostrar()

    def eliminar_reserva(self, indice):
        if 0 <= indice < len(self.reservas):
            del self.reservas[indice]
            print("🗑️ Reserva eliminada.")
        else:
            print("❌ Índice inválido.")


# Simulación del formulario
hotel = Hotel("Hotel & Spa Champaquí")

while True:
    print("\n1. Agregar reserva\n2. Ver reservas\n3. Eliminar reserva\n4. Salir")
    opcion = input("Elegí una opción: ")

    if opcion == "1":
        nombre = input("Nombre del huésped: ")
        fecha = input("Fecha (YYYY-MM-DD): ")
        habitacion = input("Tipo de habitación: ")
        nueva = Reserva(nombre, fecha, habitacion)
        hotel.agregar_reserva(nueva)

    elif opcion == "2":
        hotel.mostrar_reservas()

    elif opcion == "3":
        hotel.mostrar_reservas()
        indice = int(input("Número de reserva a eliminar: ")) - 1
        hotel.eliminar_reserva(indice)

    elif opcion == "4":
        print("👋 ¡Gracias por usar el sistema de reservas!")
        break

    else:
        print("❌ Opción inválida.")
