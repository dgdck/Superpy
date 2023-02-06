# Imports
import os
from pathlib import Path
from datetime import datetime, timedelta


def main():
    #set_time()
    #print(current_time())
    # print(advance_time(2))
    #print(convert_time('1999-01-12'))
    print(expired_products('2024-01-01'))


def validate_time(date):
    try:
        return bool(datetime.strptime(date, '%Y-%m-%d'))
    except ValueError:
        return 'Error: Please use dateformat [YYYY-MM-DD]'


def set_time(date='2022-01-01'):
    """
    Set time to specified date, or if none specified to '2022-01-01.'
    
    Examples:
    >>> set_time()
    'Time is set as: 2022-01-01'

    >>> set_time('1999-05-03')
    'Time is set as: 1999-05-03'

    Invalid dateformat will return Error
    >>> set_time('01-01-2022')
    'Error: Please use dateformat [YYYY-MM-DD]'
    
    """
    validate_date = validate_time(date)

    if validate_date == True:
        workdir = os.path.join(os.getcwd(), 'date.txt')
        Path(workdir).write_text(date)
        return f'Time is set as: {Path(workdir).read_text()}'
    else:
        return validate_date


def current_time():
    """
    >>> set_time()
    'Time is set as: 2022-01-01'

    Return current date from textfile.
    >>> current_time()
    'Today is: 2022-01-01'

    """
    workdir = os.path.join(os.getcwd(), 'date.txt')
    return f'Today is: {Path(workdir).read_text()}'


def advance_time(add_days):
    # Advances time with x days and starts function that checks for expired products
    """
    >>> set_time()
    'Time is set as: 2022-01-01'

    Advances the date with specified days and returns new date.
    >>> advance_time(2)
    'Today is: 2022-01-03'
    
    """
    workdir = os.path.join(os.getcwd(), 'date.txt')
    date_current = find_date()
    next_date = date_current + timedelta(days=add_days)
    content = next_date.strftime("%Y-%m-%d")

    Path(workdir).write_text(content)
    expired_products(content)
    return f'Today is: {Path(workdir).read_text()}'


def expired_products(today):
    from main import csvreader, expired_log

    products = csvreader('inventory.csv')
    date_today = convert_time(today)
    expired = []

    for item in products:
        expiration_date = convert_time(item['expiration_date'])
        if date_today > expiration_date:
            expired.append(item)
    expired_log(expired)
    return expired


def find_date():
    # Returns date from file ready for calculations.
    workdir = os.path.join(os.getcwd(), 'date.txt')
    content = Path(workdir).read_text()
    return datetime.strptime(content, "%Y-%m-%d")


def convert_time(content):
    return datetime.strptime(content, "%Y-%m-%d")
    

if __name__ == "__main__":
    main()
