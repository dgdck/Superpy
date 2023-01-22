import main, date


def execute(x):
    main.reset()
    while x > 0:
        buyloop()
        date.advance_time(2)
        selloop()
        x -= 1


def buyloop():
    main.buy('apple', '2023-02-01', '5', '1.5')
    main.buy('biscuits', '2024-01-01', '5', '3')
    main.buy('detergent', '2030-12-31', '20', '10')


def selloop():
    main.sold('apple', '2', '1.7')
    main.sold('biscuits', '1', '3.5')
    main.sold('detergent', '1', '12')


if __name__ == "__main__":
    execute(5)