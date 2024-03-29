import main
import date
import demo

testfile = r'tests\testfile.csv'


def test_reset():
    main.reset()
    assert main.csvreader(testfile) == []
    assert main.csvreader('bought.csv') == []
    assert main.csvreader('inventory.csv') == []
    assert main.csvreader('sold.csv') == []
    assert main.csvreader('expired.csv') == []
    assert main.csvreader('revenue.csv') == []
    assert main.read_txtfile('inventory_id.txt') == '0'
    assert main.read_txtfile('date.txt') == '2022-01-01'


def test_csvreader():
    assert main.csvreader(testfile) == []


def test_csvwriter():
    main.truncate_file(testfile)
    main.csvwriter(testfile, ['This is a test'])
    main.csvwriter(testfile, ['This is a test'])
    assert main.csvreader(testfile) == [{'This is a test': 'This is a test'}]


def test_read_lines():
    assert main.read_lines(testfile) == 2
    assert main.read_lines('date.txt') == 1


def test_read_txtfile():
    assert main.read_txtfile(testfile) == 'This is a test\nThis is a test\n'


def test_overwrite_txtfile():
    main.overwrite_txtfile(testfile, 'Test')
    assert main.read_txtfile(testfile) == 'Test'


# Test Superpy functions
def test_buy():
    main.reset()
    assert main.buy('apple', 'invalid', '5', '0.5') == 'Error: Please use dateformat [YYYY-MM-DD]'
    assert 'Buy error:' in main.buy('apple', '1900-01-01', '5', '0.5')
    main.buy('apple', '2023-01-01', '5', '0.5')
    assert main.csvreader('bought.csv') == [{'id': '1', 'product_name': 'apple', 'amount': '5.0', 'buy_date': '2022-01-01', 'buy_price': '0.5', 'expiration_date': '2023-01-01'}]
    assert main.csvreader('inventory.csv') == [{'id': '1', 'product_name': 'apple', 'amount': '5.0', 'buy_id': '1', 'buy_date': '2022-01-01', 'buy_price': '0.5', 'expiration_date': '2023-01-01'}]


def test_add_inventory():
    main.reset()
    main.buy('apple', '2023-01-01', '5', '0.5')
    assert main.csvreader('inventory.csv') == [{'id': '1', 'product_name': 'apple', 'amount': '5.0', 'buy_id': '1', 'buy_date': '2022-01-01', 'buy_price': '0.5', 'expiration_date': '2023-01-01'}]
    main.buy('orange', '2023-01-20', '10', '0.6')
    assert main.csvreader('inventory.csv') == [
        {'id': '1', 'product_name': 'apple', 'amount': '5.0', 'buy_id': '1', 'buy_date': '2022-01-01', 'buy_price': '0.5', 'expiration_date': '2023-01-01'},
        {'id': '2', 'product_name': 'orange', 'amount': '10.0', 'buy_id': '2', 'buy_date': '2022-01-01', 'buy_price': '0.6', 'expiration_date': '2023-01-20'}]


def test_sold_product_not_found():
    main.reset()
    main.buy('apple', '2023-01-01', '5', '0.5')
    assert main.sold('appl', '1', '2') == 'Product Error: appl has not been found.'


def test_sold_expired():
    main.reset()
    main.buy('apple', '2023-01-01', '5', '0.5')
    main.buy('apple', '2023-01-01', '2', '0.5')
    main.add_inventory('apple', '99', '99', '2022-01-01', '99', '1900-01-01')
    assert 'Sell error' in main.sold('apple', '5', '2')


def test_sold():
    main.reset()
    main.buy('apple', '2023-01-01', '5', '0.5')
    main.buy('apple', '2023-01-01', '2', '0.5')
    assert main.sold('apple', '2', '1.5') == 'done'
    assert main.csvreader('sold.csv') == [
        {'id': '1', 'product_name': 'apple', 'amount': '2.0', 'buy_id': '1', 'sell_date': '2022-01-01', 'sell_price': '1.5'}
        ]
    assert main.csvreader('inventory.csv') == [
        {'id': '1', 'product_name': 'apple', 'amount': '3.0', 'buy_id': '1', 'buy_date': '2022-01-01', 'buy_price': '0.5', 'expiration_date': '2023-01-01'},
        {'id': '2', 'product_name': 'apple', 'amount': '2.0', 'buy_id': '2', 'buy_date': '2022-01-01', 'buy_price': '0.5', 'expiration_date': '2023-01-01'}
        ]
    

def test_sold2():
    assert main.sold('apple', '2', '1.5') == 'done'
    assert main.csvreader('sold.csv') == [
        {'id': '1', 'product_name': 'apple', 'amount': '2.0', 'buy_id': '1', 'sell_date': '2022-01-01', 'sell_price': '1.5'},
        {'id': '2', 'product_name': 'apple', 'amount': '2.0', 'buy_id': '1', 'sell_date': '2022-01-01', 'sell_price': '1.5'}
        ]
    assert main.csvreader('inventory.csv') == [
        {'id': '1', 'product_name': 'apple', 'amount': '1.0', 'buy_id': '1', 'buy_date': '2022-01-01', 'buy_price': '0.5', 'expiration_date': '2023-01-01'},
        {'id': '2', 'product_name': 'apple', 'amount': '2.0', 'buy_id': '2', 'buy_date': '2022-01-01', 'buy_price': '0.5', 'expiration_date': '2023-01-01'}
        ]


def test_sold3():
    # Demonstrates it selling from different lots of product
    assert main.sold('apple', '2', '1.5') == 'done'
    assert main.csvreader('sold.csv') == [
        {'id': '1', 'product_name': 'apple', 'amount': '2.0', 'buy_id': '1', 'sell_date': '2022-01-01', 'sell_price': '1.5'},
        {'id': '2', 'product_name': 'apple', 'amount': '2.0', 'buy_id': '1', 'sell_date': '2022-01-01', 'sell_price': '1.5'},
        {'id': '3', 'product_name': 'apple', 'amount': '1.0', 'buy_id': '1', 'sell_date': '2022-01-01', 'sell_price': '1.5'},
        {'id': '4', 'product_name': 'apple', 'amount': '1.0', 'buy_id': '2', 'sell_date': '2022-01-01', 'sell_price': '1.5'}
        ]
    
    assert main.csvreader('inventory.csv') == [
        {'id': '2', 'product_name': 'apple', 'amount': '1.0', 'buy_id': '2', 'buy_date': '2022-01-01', 'buy_price': '0.5', 'expiration_date': '2023-01-01'}
        ]


def test_sold_errormsg():
    # Demonstrates error message
    assert main.sold('apple', '2', '1.5') == 'Not enough inventory, there are 1.0 of apple.'


def test_find_product():
    assert main.find_product('apple') == [
        {'id': '2', 'product_name': 'apple', 'amount': '1.0', 'buy_id': '2', 'buy_date': '2022-01-01', 'buy_price': '0.5', 'expiration_date': '2023-01-01'}
        ]
    assert main.find_product('nothing') == []


def test_sum_inventory():
    assert main.sum_inventory('apple') == 1.0
    main.buy('apple', '2023-01-02', '2')
    assert main.sum_inventory('apple') == 3.0


def test_update_inventory():
    main.csvwriter(testfile, ['id', 'update'])
    main.csvwriter(testfile, ['1', 'not'])
    main.update_inventory('1', 'update', 'done', testfile)
    assert main.csvreader(testfile) == [{'id': '1', 'update': 'done'}]


def test_remove_product():
    main.reset()
    main.csvwriter(testfile, ['id', 'update'])
    main.csvwriter(testfile, ['1', 'delete'])
    main.csvwriter(testfile, ['2', 'stays'])
    main.remove_product('1', testfile)
    assert main.csvreader(testfile) == [{'id': '2', 'update': 'stays'}]


def test_report_product_inventory():
    main.reset()
    main.buy('apple', '2023-01-01', '2')
    main.buy('pear', '2023-01-01', '2')
    assert main.report_product('apple') == [{'amount': '2.0', 'buy_date': '2022-01-01', 'buy_id': '1', 'buy_price': '1.0', 'expiration_date': '2023-01-01', 'id': '1', 'product_name': 'apple'}]
    date.advance_time(2)
    main.buy('apple', '2023-01-01', '2')
    main.buy('pear', '2023-01-01', '2')
    assert main.report_product('apple', begin_date='2022-01-03') == [{'amount': '2.0', 'buy_date': '2022-01-03', 'buy_id': '3', 'buy_price': '1.0', 'expiration_date': '2023-01-01', 'id': '3', 'product_name': 'apple'}]
    assert main.report_product('apple', end_date='2022-01-01') == [{'amount': '2.0', 'buy_date': '2022-01-01', 'buy_id': '1', 'buy_price': '1.0', 'expiration_date': '2023-01-01', 'id': '1', 'product_name': 'apple'}]
    date.advance_time(2)
    main.buy('apple', '2023-01-01', '2')
    main.buy('pear', '2023-01-01', '2')
    assert main.report_product(begin_date='2022-01-02', end_date='2022-01-03') == [{'amount': '2.0', 'buy_date': '2022-01-03', 'buy_id': '3', 'buy_price': '1.0', 'expiration_date': '2023-01-01', 'id': '3', 'product_name': 'apple'},{'amount': '2.0', 'buy_date': '2022-01-03', 'buy_id': '4', 'buy_price': '1.0', 'expiration_date': '2023-01-01', 'id': '4', 'product_name': 'pear'}]


def test_report_product_sold_apple():
    date.advance_time(2)
    main.sold('apple', '2', '1.5')
    main.sold('pear', '2', '2')
    assert main.report_product('apple', mode='sell') == [{'id': '1', 'product_name': 'apple', 'amount': '2.0', 'buy_id': '1', 'sell_date': '2022-01-07', 'sell_price': '1.5'}]


def test_report_product_buy():
    demo.execute(1)
    assert main.report_product(mode='buy') == main.csvreader('bought.csv')


def test_report_product_sold():
    demo.execute(1)
    assert main.report_product(mode='sell') == main.csvreader('sold.csv')


def test_report_product_expired():
    demo.execute(1)
    assert main.report_product(mode='expired') == main.csvreader('expired.csv')


def test_report_product_revenue():
    demo.execute(1)
    assert main.report_product(mode='revenue') == main.csvreader('revenue.csv')


def test_expiration_date():
    demo.execute(1)
    assert main.expired_products('2021-02-02') == []
    assert main.expired_products('2023-02-02') == [{'id': '2', 'product_name': 'apple', 'amount': '3.0', 'buy_id': '2', 'buy_date': '2022-01-01', 'buy_price': '1.5', 'expiration_date': '2022-02-01'}]
    assert main.expired_products('9999-02-02') == [{'id': '3', 'product_name': 'biscuits', 'amount': '4.0', 'buy_id': '3', 'buy_date': '2022-01-01', 'buy_price': '3.0', 'expiration_date': '2024-01-01'}, {'id': '4', 'product_name': 'detergent', 'amount': '19.0', 'buy_id': '4', 'buy_date': '2022-01-01', 'buy_price': '10.0', 'expiration_date': '2030-12-31'}]


def test_expired_log():
    main.reset()
    main.buy('apple', '2022-01-03', '2')
    main.buy('pear', '2022-01-05', '2')
    assert main.csvreader('expired.csv') == []
    assert main.csvreader('inventory.csv') == [{'id': '1', 'product_name': 'apple', 'amount': '2.0', 'buy_id': '1', 'buy_date': '2022-01-01', 'buy_price': '1.0', 'expiration_date': '2022-01-03'}, {'id': '2', 'product_name': 'pear', 'amount': '2.0', 'buy_id': '2', 'buy_date': '2022-01-01', 'buy_price': '1.0', 'expiration_date': '2022-01-05'}]
    date.advance_time(2)
    assert main.csvreader('expired.csv') == []
    assert main.csvreader('inventory.csv') == [{'id': '1', 'product_name': 'apple', 'amount': '2.0', 'buy_id': '1', 'buy_date': '2022-01-01', 'buy_price': '1.0', 'expiration_date': '2022-01-03'}, {'id': '2', 'product_name': 'pear', 'amount': '2.0', 'buy_id': '2', 'buy_date': '2022-01-01', 'buy_price': '1.0', 'expiration_date': '2022-01-05'}]
    date.advance_time(1)
    assert main.csvreader('expired.csv') == [{'id': '1', 'product_name': 'apple', 'amount': '2.0', 'buy_id': '1', 'buy_date': '2022-01-01', 'buy_price': '1.0', 'expiration_date': '2022-01-03'}]
    assert main.csvreader('inventory.csv') == [{'id': '2', 'product_name': 'pear', 'amount': '2.0', 'buy_id': '2', 'buy_date': '2022-01-01', 'buy_price': '1.0', 'expiration_date': '2022-01-05'}]
    date.advance_time(2)
    assert main.csvreader('expired.csv') == [{'id': '1', 'product_name': 'apple', 'amount': '2.0', 'buy_id': '1', 'buy_date': '2022-01-01', 'buy_price': '1.0', 'expiration_date': '2022-01-03'}, {'id': '2', 'product_name': 'pear', 'amount': '2.0', 'buy_id': '2', 'buy_date': '2022-01-01', 'buy_price': '1.0', 'expiration_date': '2022-01-05'}]
    assert main.csvreader('inventory.csv') == []
