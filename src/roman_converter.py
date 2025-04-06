def decimal_to_roman(number):
    if not 1 <= number <= 3999:
        raise ValueError("El número debe estar entre 1 y 3999.")
    
    roman_numerals = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]
    
    result = []
    
    for value, symbol in roman_numerals:
        while number >= value:
            result.append(symbol)
            number -= value
    
    return ''.join(result)

def get_decimal_input():
    while True:
        try:
            number = int(input("Introduce un número decimal entre 1 y 3999: "))
            if 1 <= number <= 3999:
                return number
            else:
                print("Error: El número debe estar entre 1 y 3999.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

def main():
    while True:
        number = get_decimal_input()
        roman = decimal_to_roman(number)
        print(f"El número romano correspondiente es: {roman}")
        break  

if __name__ == "__main__":
    main()












