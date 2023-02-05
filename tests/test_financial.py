import financial
import demo


def test_income():
    demo.execute(2)
    assert financial.income() == 37.8


def test_investments():
    demo.execute(2)
    assert financial.investments() == 460


def test_revenue():
    demo.execute(2)
    assert financial.revenue() == -422.2