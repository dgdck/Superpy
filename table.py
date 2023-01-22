from prettytable import PrettyTable
from main import csvreader


def main():
    print(table())


def table(filename='inventory.csv'):
    # Specify the Column Names while initializing the Table
    myTable = PrettyTable(table_header(filename))

    # Add rows
    for item in table_values(filename):
            myTable.add_row(item.values())
    
    return myTable


# Table input is list of dictionaries or csv-file
def table_header(filename='inventory.csv'):
    if type(filename) == list:
        fieldnames = [*filename[0]]
    elif '.csv' in filename:
        input = csvreader(filename)
        fieldnames = [*input[0]]
    return fieldnames


def table_values(filename='inventory.csv'):
    if type(filename) == list:
        input = filename
    elif '.csv' in filename:
        input = csvreader(filename)
    return input


if __name__ == '__main__':
    main()
