user_input = ''
items = [{'Name': 'Milk', 'Quantity': 120, 'Unit': '    l', 'Unit Price (PLN)': 2.3},
         {'Name': 'Sugar', 'Quantity': 1000, 'Unit': 'Kg', 'Unit Price (PLN)': 3},
         {'Name': 'Flour', 'Quantity': 12000, 'Unit': 'Kg', 'Unit Price (PLN)': 1.2}
         ]
sold_items = []


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def get_items():
    print("Name\tQuantity\tUnit\tUnit Price (PLN)")
    print("____\t________\t____\t________________")

    for i in items:
        print("{:9s}\t{}\t{:7s}\t{}".format(i['Name'], i['Quantity'], i['Unit'], i['Unit Price (PLN)']))


def add():

    print('Adding new items...')
    name_input = input('Item name:')
    quantity_input = input('Item Quantity:')
    unit_input = input('Item Unit of Measure:')
    unit_price_input = input('Item Unit Price in PLN:')
    new_item = {"Name": name_input, "Quantity": quantity_input, "Unit": unit_input, "Unit Price (PLN)": unit_price_input}
    items.append(new_item)
    get_items()


def sell_item():
    name_sell = input('Item name:')
    quantity_input = input('Quantity to sell:')
    global sold_items
    for i in items:
        if i['Name'] == name_sell:
            new = i['Quantity'] - int(quantity_input)
            i['Quantity'] = new
            unit = i['Unit']
            unit_price = i['Unit Price (PLN)']
            sold_items = {'Name': name_sell, 'Quantity': quantity_input, 'Unit': unit, 'Unit Price (PLN)': unit_price}
            print(f'Successfully sold {quantity_input} {unit} of {name_sell}')
            print(sold_items)
    get_items()

def get_costs():
    

if __name__ == '__main__':
    while user_input != 'exit':
        user_input = input('What would you like to do?')
        if user_input == 'show':
            get_items()

        elif user_input == 'add':
            add()

        elif user_input == 'sell':
            sell_item()

    print('Exiting... Bye')
