# Import modules
import date
import datetime
from main import read_txtfile
from demo import execute


def test_validate_time():
        assert date.validate_time('2022-01-01') == True
        assert date.validate_time('2022-1-1') == True
        assert date.validate_time('2022-01-1') == True
        assert date.validate_time('2022-01-32') == 'Error: Please use dateformat [YYYY-MM-DD]'
        assert date.validate_time('2024-02-29') == True
        assert date.validate_time('2022-02-29') == 'Error: Please use dateformat [YYYY-MM-DD]'
        assert date.validate_time('2022-13-01') == 'Error: Please use dateformat [YYYY-MM-DD]'
        assert date.validate_time('13-01-22') == 'Error: Please use dateformat [YYYY-MM-DD]'
        assert date.validate_time('13-01-2022') == 'Error: Please use dateformat [YYYY-MM-DD]'
        assert date.validate_time('13-jan-2022') == 'Error: Please use dateformat [YYYY-MM-DD]'
        assert date.validate_time('2022-jan-13') == 'Error: Please use dateformat [YYYY-MM-DD]'


def test_set_time():
        assert date.set_time() == 'Time is set as: 2022-01-01'
        assert date.set_time('invalid') == 'Error: Please use dateformat [YYYY-MM-DD]'


def test_current_time():
        date.set_time()
        assert read_txtfile('date.txt') == '2022-01-01'


def test_advance_time():
        date.set_time()
        assert date.advance_time(2) == 'Today is: 2022-01-03'
        assert read_txtfile('date.txt') == '2022-01-03'


def test_find_date():
        date.set_time()
        assert date.find_date() == datetime.datetime(2022, 1, 1, 0, 0)


def test_convert_time():
        assert date.convert_time('2022-01-02') == datetime.datetime(2022, 1, 2, 0, 0)


def test_expiration_date():
        execute(1)
        assert date.expired_products('2021-02-02') == []
        assert date.expired_products('2023-02-02') == [{'id': '1', 'product_name': 'apple', 'amount': '3.0', 'buy_id': '1', 'buy_date': '2022-01-01', 'buy_price': '1.5', 'expiration_date': '2023-02-01'}]
        assert date.expired_products('9999-02-02') == [{'id': '2', 'product_name': 'biscuits', 'amount': '4.0', 'buy_id': '2', 'buy_date': '2022-01-01', 'buy_price': '3.0', 'expiration_date': '2024-01-01'}, {'id': '3', 'product_name': 'detergent', 'amount': '19.0', 'buy_id': '3', 'buy_date': '2022-01-01', 'buy_price': '10.0', 'expiration_date': '2030-12-31'}]
