#Este será el código principal
def desplegar_menu_principal():
    print("\n********************")
    print("** MENÚ PRINCIPAL **")
    print("********************")
    print("K - Determinar si los dígitos suman 21")
    print("P - Determinar si un número es par")
    print("R - Calcular el área de un rectángulo")
    print("X - SALIR")

def identificar_pares(numero):
    return numero % 2 == 0


def main():
    """Esta es la función que presentará el menú principal de nuestro código """
    while True:
        desplegar_menu_principal()
        eleccion = input("Elija una opción: ")
        match eleccion.upper():
            case "K":
                pass
            case "P":
                valor = int(input("Indica el número entero a evaluar: "))
                if identificar_pares(valor):
                    print(f"El número {valor} SI es par")
                else:
                    print(f"El número {valor} NO es par")
                print()
            case "R":
                pass
            case "X":
                break
            case _:
                print("\n* ELECCIÓN INVÁLIDA, ELIJA NUEVAMENTE *")

if __name__ == "__main__":
    main()