
def main():
    nombre = input("Por favor introduce tu nombre: ")
    ventas = input("Introduzca las ventas totales del mes: ")

    ventas = int(ventas)
    comision = (ventas * 13) / 100
    comision = round(comision, 2)

    print(f"Hola {nombre}. La comisión actual del mes es: {comision}")

if __name__ == '__main__':
    main()