from main import report_product


def main():
    print(income())
    print(investments())
    print(revenue())


def revenue(date_1='0001-01-01', date_2='9999-12-31'):
    money_in = income(date_1, date_2)
    money_out = investments(date_1, date_2)
    revenue =  money_in - money_out
    return round(revenue, 2)


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


if __name__ == '__main__':
    main()