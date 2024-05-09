def encode_amount(n):
    digit_to_symbol = {
        '0': '!',
        '1': '@',
        '2': '#',
        '3': '$',
        '4': '%',
        '5': '^',
        '6': '&',
        '7': '*',
        '8': '>',
        '9': '<'
    }
    formatted_number = f"{n:.2f}"
    encoded_amount = ''.join(digit_to_symbol.get(char, char) for char in formatted_number)
    return encoded_amount

input_amount = float(input("Enter the amount: "))
encoded_string = encode_amount(input_amount)
print(encoded_string)
