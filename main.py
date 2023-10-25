# Leah Jones and Justin Oh
def encode(password):
    encoded_string = ""
    for digit in password:
        if digit == "7":
            encoded_string += "0"
        if digit == "8":
            encoded_string += "1"
        if digit == "9":
            encoded_string += "2"
        encoded_string += str(int(digit) + 3)
    return encoded_string



