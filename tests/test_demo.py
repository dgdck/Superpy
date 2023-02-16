import demo


def test_execute():
    assert demo.execute(1) == 'done'


def test_buyloop():
    assert demo.buyloop() == 'done'


def test_selloop():
    assert demo.selloop() == 'done'
