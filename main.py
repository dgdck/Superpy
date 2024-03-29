# Imports
import csv
import os
from pathlib import Path
from date import set_time, validate_time, convert_time


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    pass


# SuperPy functions
def buy(product_name, expiration_date, amount='1', buy_price='1'):
    """
    Buying product and will be added to inventory
    >>> buy('orange', '2023-01-01', 10, 5.6)
    'done'

    Invalid date format will return Error
    >>> buy('orange', '01-01-2024', 10, 5.6)
    'Error: Please use dateformat [YYYY-MM-DD]'

    """
    validate_date = validate_time(expiration_date)
    amount = float(amount)
    buy_price = float(buy_price)

    if validate_date == True:
        if convert_time(expiration_date) < convert_time(read_txtfile('date.txt')):
            return 'Buy error: Product is already expired and has not been bought.'
        else:
            filename = 'bought.csv'
            id = read_lines(filename)
            buy_date = read_txtfile('date.txt')
            header = ['id', 'product_name', 'amount', 'buy_date', 'buy_price', 'expiration_date']
            values = [id, product_name, amount, buy_date, buy_price, expiration_date]
            if id == 0:
                csvwriter(filename, header)
                buy(product_name, expiration_date, amount, buy_price)
            elif id > 0:
                csvwriter(filename, values)
                add_inventory(product_name, amount, id, buy_date, buy_price, expiration_date)
            return 'done'
    else:
        return validate_date


def add_inventory(product_name, amount, buy_id, buy_date, buy_price, expiration_date):
    filename = 'inventory.csv'
    txtfile = 'inventory_id.txt'
    id = int(read_txtfile(txtfile))
    id += 1
    header = ['id', 'product_name', 'amount', 'buy_id', 'buy_date', 'buy_price', 'expiration_date']
    values = [id, product_name, amount, buy_id, buy_date, buy_price, expiration_date]
    if id == 1:
        csvwriter(filename, header)
        csvwriter(filename, values)
        overwrite_txtfile(txtfile, str(id))
    elif id > 1:
        csvwriter(filename, values)
        overwrite_txtfile(txtfile, str(id))    


def sold(product_name, amount, sell_price):
    amount = float(amount)
    sell_price = float(sell_price)
    products = find_product(product_name) #list of dictionaries
    if products == []:
        return f'Product Error: {product_name} has not been found.'
    product = products[0]
    today = convert_time(read_txtfile('date.txt'))
    for item in products:
        if convert_time(item['expiration_date']) < today:
                expired_products(read_txtfile('date.txt'))
                return 'Sell error: A product is expired and has been moved to expired list.'
        
    total_inventory = sum_inventory(product_name)

    if (total_inventory - amount) < 0:
        return f'Not enough inventory, there are {total_inventory} of {product_name}.'
    elif amount > 0:
        product_inventory = float(product['amount'])
        buy_id = product['buy_id']
        if amount >= product_inventory: #when stock-inventory gets depleted
            sold_log(product_name, product_inventory, sell_price, buy_id)
            amount = amount - product_inventory
            remove_product(product['id'])
            return sold(product_name, amount, sell_price)
        elif amount < product_inventory: #when stock-inventory is not depleted
            sold_log(product_name, amount, sell_price, buy_id)
            product_inventory = product_inventory - amount
            update_inventory(product['id'], 'amount', product_inventory)
            return 'done'
    else:
        return 'done'
            

def sold_log(product_name, amount, sell_price, buy_id):
    filename = 'sold.csv'
    id = read_lines(filename)
    sell_date = read_txtfile('date.txt')
    header = ['id', 'product_name', 'amount', 'buy_id', 'sell_date', 'sell_price']
    values = [id, product_name, amount, buy_id, sell_date, sell_price]
    if id == 0:
        csvwriter(filename, header)
        sold_log(product_name, amount, sell_price, buy_id)
    elif id > 0:
        csvwriter(filename, values)


def expired_products(today):
    products = csvreader('inventory.csv')
    date_today = convert_time(today)
    expired = []

    for item in products:
        expiration_date = convert_time(item['expiration_date'])
        if date_today > expiration_date:
            expired.append(item)
    expired_log(expired)
    return expired


def expired_log(products):
    # logs expired products and removes products from inventory
    filename = 'expired.csv'
    id = read_lines(filename)
    header = ['id', 'product_name', 'amount', 'buy_id', 'buy_date', 'buy_price', 'expiration_date']
    values = products
    if id == 0:
        csvwriter(filename, header)
        expired_log(values)
    elif id > 0:
        for item in values:
            remove_product(item['id'])
            csvwriter(filename, item.values())


def find_product(product_name='0', filename='inventory.csv'):
    # Finds product in .csv-file and returns list of dictionaries
    if product_name == '0':
        return csvreader(filename)
    list = csvreader(filename)
    found_list = []
    for item in list:
        if item['product_name'] == product_name:
            found_list.append(item)
    return found_list


def report_product(product_name='0', filename='inventory.csv', mode='inventory', begin_date='0001-01-01', end_date='9999-12-31'):
    # Finds product in specified log between specified dates and returns list of dictionaries
    # Returns whole inventory-log if nothing is specified
    final_list = []
    begin_date = convert_time(begin_date)
    end_date = convert_time(end_date)
    if mode == 'inventory':
        report_list = find_product(product_name, filename)
        for item in report_list:
            time = convert_time(item['buy_date'])
            if time >= begin_date and time <= end_date:
                final_list.append(item)
    elif mode == 'buy':
        report_list = find_product(product_name, filename='bought.csv')
        for item in report_list:
            time = convert_time(item['buy_date'])
            if time >= begin_date and time <= end_date:
                final_list.append(item)
    elif mode == 'sell':
        report_list = find_product(product_name, filename='sold.csv')
        for item in report_list:
            time = convert_time(item['sell_date'])
            if time >= begin_date and time <= end_date:
                final_list.append(item)
    elif mode == 'expired':
        report_list = find_product(product_name, filename='expired.csv')
        for item in report_list:
            time = convert_time(item['expiration_date'])
            if time >= begin_date and time <= end_date:
                final_list.append(item)
    elif mode == 'revenue':
        report_list = find_product(product_name, filename='revenue.csv')
        for item in report_list:
            time = convert_time(item['date'])
            if time >= begin_date and time <= end_date:
                final_list.append(item)
    return final_list
    

def sum_inventory(product_name):
    list = find_product(product_name)
    total = 0
    for item in list:
        total += float(item['amount'])
    return total


def update_inventory(id, key, value, filename='inventory.csv'):
    list = csvreader(filename)
    fieldnames = [*list[0]]
    with open(filename, mode='w', newline='') as file:
        write = csv.DictWriter(file, fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write.writeheader()
        for item in list:
            if item['id'] == id:
                item.update({key: value})
                write.writerow(item)
            elif item['id'] != id:
                write.writerow(item)


def remove_product(id, filename='inventory.csv'):
    list = csvreader(filename)
    fieldnames = [*list[0]]
    with open(filename, mode='w', newline='') as file:
        write = csv.DictWriter(file, fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write.writeheader()
        for item in list:
            if item['id'] != id:
                write.writerow(item)


# Filemanipulation tools
def reset():
    truncate_file(r'tests\testfile.csv')
    truncate_file('bought.csv')
    truncate_file('inventory.csv')
    truncate_file('sold.csv')
    truncate_file('expired.csv')
    truncate_file('revenue.csv')
    overwrite_txtfile('inventory_id.txt', str(0))
    set_time()


def read_lines(filename):
    with open(filename,mode="r") as file:
        csv_file = csv.reader(file)
        lines = len(list(csv_file))
    return lines


def read_txtfile(file):
    workdir = os.path.join(os.getcwd(), file)
    return Path(workdir).read_text()


def overwrite_txtfile(file, content):
    workdir = os.path.join(os.getcwd(), file)
    Path(workdir).write_text(content)


def truncate_file(file_name):
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, file_name)
    with open(abs_file_path, mode='w+') as file:
            file.close()


def csvwriter(file_name,columns):
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, file_name)
    with open(abs_file_path, mode='a', newline='') as file:
            write = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            write.writerow(columns)


def csvreader(file_name):
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, file_name)
    with open(abs_file_path, mode='r') as file:
        reader = csv.DictReader(file)
        list_csv = []
        for row in reader:
            list_csv.append(row)
        return list_csv


if __name__ == "__main__":
    main()
