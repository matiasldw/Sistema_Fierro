def variante() -> bool:
    while True:
        response = input(
            "Desea parametrizar los valores (valor final, potencia aplicada) No/si: "
        )
        if response.lower() == "no" or response == "":
            return False
        elif response.lower() == "si":
            return True


def is_happy_number(number: int, value_happy: int = 1, pow: int = 2) -> bool:
    sub_total = 0
    unhappy = {4, 16, 37, 58, 89, 145, 42, 20}

    while True:
        sub_total = sum(int(i) ** pow for i in str(number))

        if sub_total == value_happy:
            return True
        elif sub_total in unhappy:
            return False
        else:
            unhappy.add(sub_total)
            number = str(sub_total)
            sub_total = 0


def main():
    custom = variante()
    number_for_test = 1

    numbers = int(input("Cuantos numeros felices desea encontrar ----->: "))

    if custom:
        final_value = int(input("Valor final ----->: "))
        pow = int(input("Potencia a aplicar ----->: "))

    find_numbers = 0

    while find_numbers != numbers:
        if custom:
            if is_happy_number(number_for_test, final_value, pow):
                print(number_for_test)
                find_numbers += 1
        else:
            if is_happy_number(number_for_test):
                print(number_for_test)
                find_numbers += 1
        number_for_test += 1


if __name__ == "__main__":
    main()

# Para la variante b), una optimizacion seria guardar todos los resultados de las multiplicaciones
# que ya sabemos que no generan numeros felices e ir sumandolos al set de "unhappy". El programa lo hace pero cuando se
# evalua otro numero el set vuelve con los valores por defecto.
