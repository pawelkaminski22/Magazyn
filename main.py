user_input = ''
items = [{'Name': 'Milk', 'Quantity': 120, 'Unit': 'l', 'Unit Price (PLN)': 2.3},
         {'Name': 'Sugar', 'Quantity': 1000, 'Unit': 'Kg', 'Unit Price (PLN)': 3},
         {'Name': 'Flour', 'Quantity': 12000, 'Unit': 'Kg', 'Unit Price (PLN)': 1.2}
         ]


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    while user_input != 'exit':
        user_input = input('What would you like to do?')

    print('Exiting... Bye')
