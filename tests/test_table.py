import table


testfile = r'tests\testfile_table.csv'


def test_table_header():
    assert table.table_header(testfile) == ['id', 'product_name', 'amount', 'buy_id', 'buy_date', 'buy_price', 'expiration_date']
    assert table.table_header([{'id': '1', 'product_name': 'apple', 'amount': '1.0', 'buy_id': '1', 'buy_date': '2022-01-01', 'buy_price': '1.5', 'expiration_date': '9999-01-01'}, {'id': '2', 'product_name': 'apple', 'amount': '5.0', 'buy_id': '2', 'buy_date': '2022-01-01', 'buy_price': '1.5', 'expiration_date': '9999-01-01'}]) == ['id', 'product_name', 'amount', 'buy_id', 'buy_date', 'buy_price', 'expiration_date']


def test_table_values():
    assert table.table_values(testfile) == [{'id': '1', 'product_name': 'apple', 'amount': '1.0', 'buy_id': '1', 'buy_date': '2022-01-01', 'buy_price': '1.5', 'expiration_date': '9999-01-01'}, {'id': '2', 'product_name': 'apple', 'amount': '5.0', 'buy_id': '2', 'buy_date': '2022-01-01', 'buy_price': '1.5', 'expiration_date': '9999-01-01'}]
    assert table.table_values([{'id': '1', 'product_name': 'apple', 'amount': '1.0', 'buy_id': '1', 'buy_date': '2022-01-01', 'buy_price': '1.5', 'expiration_date': '9999-01-01'}]) == [{'id': '1', 'product_name': 'apple', 'amount': '1.0', 'buy_id': '1', 'buy_date': '2022-01-01', 'buy_price': '1.5', 'expiration_date': '9999-01-01'}]
