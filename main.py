import csv
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_filas(file):
    with open(file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        filas = list(reader)
        for i, fila in enumerate(filas):
            print(f"Fila {i+1}: {fila}")
        return filas

def actualizar_estado(file, filas, fila_id, nuevo_estado):
    filas[fila_id][2] = nuevo_estado 
    with open(file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(filas)
    print(f"Estado de la fila {fila_id+1} actualizado a: {filas[fila_id]}")

def elden_ring():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(script_dir, 'eldenringdb.csv')
    while True:
        limpiar_pantalla()
        filas = mostrar_filas(file)
        try:
            fila_id = int(input("Ingrese el ID de la fila que desea modificar (0 para salir, 100 para volver a seleccionar): ")) - 1
            if fila_id == -1:
                print("Saliendo del programa.")
                break
            if fila_id == 99:
                limpiar_pantalla
                main()
            if fila_id < 0 or fila_id >= len(filas):
                print("ID de fila no válido. Intente nuevamente.")
            else:
                nuevo_estado = input("Ingrese el nuevo estado (V para positivo, X para negativo): ")
                if nuevo_estado not in ('V', 'X'):
                    print("Entrada no válida. Por favor, ingrese 'V' para positivo o 'X' para negativo.")
                else:
                    actualizar_estado(file, filas, fila_id, nuevo_estado)
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número válido.")

def sekiro():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(script_dir, 'sekirodb.csv')
    while True:
        limpiar_pantalla()
        filas = mostrar_filas(file)
        try:
            fila_id = int(input("Ingrese el ID de la fila que desea modificar (0 para salir, 100 para volver a seleccionar): ")) - 1
            if fila_id == -1:
                print("Saliendo del programa.")
                break
            if fila_id == 99:
                limpiar_pantalla
                main()
            if fila_id < 0 or fila_id >= len(filas):
                print("ID de fila no válido. Intente nuevamente.")
            else:
                nuevo_estado = input("Ingrese el nuevo estado (V para positivo, X para negativo): ")
                if nuevo_estado not in ('V', 'X'):
                    print("Entrada no válida. Por favor, ingrese 'V' para positivo o 'X' para negativo.")
                else:
                    actualizar_estado(file, filas, fila_id, nuevo_estado)
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número válido.")

def main():
    print("Selecciona una base de datos:")
    choose = int(input("1 Elden Ring, 2 Sekiro "))
    lista = {1, 2}
    if choose == 1:
        elden_ring()
    elif choose == 2:
        sekiro()
    elif choose is not lista:
        print("Error, intentalo de nuevo")
        main()

if __name__ == '__main__':
    main()
