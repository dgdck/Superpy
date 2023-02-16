import financial
import demo
from main import csvreader


def test_income():
    demo.execute(2)
    assert financial.income() == 37.8


def test_investments():
    demo.execute(2)
    assert financial.investments() == 460


def test_lost():
    demo.execute(2)
    assert financial.lost() == 15


def test_revenue():
    demo.execute(2)
    assert financial.revenue() == -437.2


def test_revenue_today():
    demo.execute(1)
    assert financial.revenue_today() == 18.9


def test_income_on_date():
    demo.execute(2)
    assert financial.income('2022-01-03', '2022-01-03') == 18.9


def test_investments_on_date():
    demo.execute(2)
    assert financial.investments('2022-01-01', '2022-01-01') == 230


def test_revenue_on_date():
    demo.execute(2)
    assert financial.revenue('2022-01-03', '2022-01-03') == -211.1

def test_end_of_day():
    demo.execute(1)
    assert financial.end_of_day('2022-01-03') == 'Done'
    assert csvreader('revenue.csv') == [{'date': '2022-01-01', 'costs': '230.0', 'income': '0', 'lost': '0', 'revenue': '-230.0'}, {'date': '2022-01-03', 'costs': '230.0', 'income': '18.9', 'lost': '7.5', 'revenue': '-218.6'}]
