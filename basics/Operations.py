import math

def main():
    x = 6
    y = 2
    z = 5

    print(f"Operación suma {x} + {y} = {x + y}")
    print(f"Operación resta {x} - {y} = {x - y}")
    print(f"Operación multiplicacion {x} * {y} = {x * y}")
    print(f"Operación division {z} / {y} = {z / y}")
    print(f"Operación division resultado {z} / {y} = {z // y}")
    print(f"Operación division modulo {z} % {y} = {z % y}")
    print(f"Operación potencia {x} ^ {y} = {x**y}")
    print(f"Operación raiz {x}  = {math.sqrt(x)}")

if __name__ == '__main__':
    main()