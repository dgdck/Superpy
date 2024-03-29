from main import report_product, csvwriter, read_lines
from date import find_date
from datetime import datetime


def main():
    print(revenue_today())


def revenue(date_1='0001-01-01', date_2='9999-12-31'):
    money_in = income(date_1, date_2)
    money_out = investments(date_1, date_2)
    revenue_lost = lost(date_1, date_2)
    revenue =  money_in - money_out - revenue_lost
    return round(revenue, 2)


def revenue_today():
    today = str(datetime.strftime(find_date(), '%Y-%m-%d'))
    money_in = income(today, today)
    money_out = investments(today, today)
    revenue_lost = investments(today, today)
    revenue = money_in - money_out - revenue_lost
    return revenue


def investments(date_1='0001-01-01', date_2='9999-12-31'):
    list_investments = report_product(mode='buy', begin_date=date_1, end_date=date_2)
    total_investments = 0
    for item in list_investments:
        total_investments += (float(item['buy_price']) * float(item['amount']))
    return round(total_investments, 2)


def income(date_1='0001-01-01', date_2='9999-12-31'):
    list_income = report_product(mode='sell', begin_date=date_1, end_date=date_2)
    total_income = 0
    for item in list_income:
        total_income += (float(item['sell_price']) * float(item['amount']))
    return round(total_income, 2)


def lost(date_1='0001-01-01', date_2='9999-12-31'):
    list_lost = report_product(mode='expired', begin_date=date_1, end_date=date_2)
    total_lost = 0
    for item in list_lost:
        total_lost += (float(item['buy_price']) * float(item['amount']))
    return round(total_lost, 2)


def end_of_day(revenue_date, filename='revenue.csv'):
    id = read_lines(filename)
    header = ['date', 'costs', 'income', 'lost', 'revenue']
    write_costs = investments()
    write_income = income()
    write_lost = lost()
    write_revenue = revenue()
    values = [revenue_date, write_costs, write_income, write_lost, write_revenue]

    if id == 0:
        csvwriter(filename, header)
        csvwriter(filename, values)
    elif id > 0:
        csvwriter(filename, values)
    return 'Done'


if __name__ == '__main__':
    main()
