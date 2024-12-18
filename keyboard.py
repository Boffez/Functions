def input_string(message):
    return input(message)

def input_integer(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def input_real(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a real number.")

def input_boolean(message):
    while True:
        response = input(message).strip().lower()
        if response in ['y', 'n']:
            return response == 'y'
        else:
            print("Invalid input. Please enter 'y' or 'n'.")