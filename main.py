import csv

user_input = ''
items = [{'Name': 'Milk', 'Quantity': 120, 'Unit': 'l', 'Unit Price (PLN)': 2.3},
         {'Name': 'Sugar', 'Quantity': 1000, 'Unit': 'Kg', 'Unit Price (PLN)': 3},
         {'Name': 'Flour', 'Quantity': 12000, 'Unit': 'Kg', 'Unit Price (PLN)': 1.2}
         ]
sold_items = []


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
    quantity_input = int(input('Quantity to sell:'))
    global sold_items
    for i in items:
        if i['Name'] == name_sell:
            new = i['Quantity'] - int(quantity_input)
            i['Quantity'] = int(new)
            unit = i['Unit']
            unit_price = i['Unit Price (PLN)']
            sold_items = [{'Name': name_sell, 'Quantity': int(quantity_input), 'Unit': unit, 'Unit Price (PLN)': float(unit_price)}]
            print(f'Successfully sold {quantity_input} {unit} of {name_sell}')
            print(sold_items)
    get_items()


def get_costs():
    costs = sum(item['Quantity'] * item['Unit Price (PLN)'] for item in items) * -1
    income = sum(item['Quantity'] * item['Unit Price (PLN)'] for item in sold_items)
    revenue = costs + income
    print(f'Costs: {costs}')
    print(f'Income: {income}')
    print('____________')
    print(f'Revenue: {revenue}')

def export_items_to_csv():
    with open('Magazyn.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Quantity', 'Unit', 'Unit Price (PLN)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(items)
    print('Items saved')


def export_sales_to_csv():
    with open('Sales.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Quantity', 'Unit', 'Unit Price (PLN)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(sold_items)
    print('Sales saved')


def load_items_from_csv(path):
    items.clear()
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            items.append(row)
    print(items)


if __name__ == '__main__':
    user_input = input('Enter path to Input File: ')
    load_items_from_csv(user_input)

    while user_input != 'exit':
        user_input = input('What would you like to do?')
        if user_input == 'show':
            get_items()

        elif user_input == 'add':
            add()

        elif user_input == 'sell':
            sell_item()

        elif user_input == 'rev':
            get_costs()

        elif user_input == 'save':
            export_items_to_csv()
            export_sales_to_csv()

        elif user_input == 'load':
            load_items_from_csv('Magazyn.csv')

    print('Exiting... Bye')
