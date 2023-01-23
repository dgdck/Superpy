import super

# Test main options
def test_parser_reset(capsys):
    super.parse_args(['--reset'])
    captured = capsys.readouterr()
    assert captured.out == 'reset done\n'

# Test commands: date
def test_parser_current_time_short(capsys):
    super.parse_args(['date', '-c'])
    captured = capsys.readouterr()
    assert 'Today is:' in captured.out


def test_parser_current_time(capsys):
    super.parse_args(['date', '--current'])
    captured = capsys.readouterr()
    assert 'Today is:' in captured.out


def test_parser_advance_time_short(capsys):
    super.parse_args(['date', '-ad', '3'])
    captured = capsys.readouterr()
    assert 'Today is:' in captured.out


def test_parser_advance_time(capsys):
    super.parse_args(['date', '--advance', '3'])
    captured = capsys.readouterr()
    assert 'Today is:' in captured.out


def test_parser_set_time_short(capsys):
    super.parse_args(['date', '-st'])
    captured = capsys.readouterr()
    assert 'Time is set as:' in captured.out


def test_parser_set_time(capsys):
    super.parse_args(['date', '--set-time'])
    captured = capsys.readouterr()
    assert 'Time is set as:' in captured.out

# Test commands: buy
def test_parser_buy_short(capsys):
    super.parse_args(['buy', '-pn', 'apple', '-exp', '9999-01-01', '-a', '5', '-p', '1.5'])
    captured = capsys.readouterr()
    assert 'done' in captured.out

def test_parser_buy(capsys):
    super.parse_args(['buy', '--product-name', 'apple', '--expiration-date', '9999-01-01', '--amount', '5', '--price', '1.5'])
    captured = capsys.readouterr()
    assert 'done' in captured.out

# Test commands: sell
def test_parser_sell_short(capsys):
    super.parse_args(['sell', '-pn', 'apple', '-a', '2', '-p', '1.7'])
    captured = capsys.readouterr()
    assert 'done' in captured.out


def test_parser_sell(capsys):
    super.parse_args(['sell', '--product-name', 'apple', '--amount', '2', '--price', '1.7'])
    captured = capsys.readouterr()
    assert 'done' in captured.out

# Test commands: report
def test_parser_report_short(capsys):
    super.parse_args(['report', '-m', 'buy', '-ds', '0001-01-01', '-u', '9999-12-31'])
    captured = capsys.readouterr()
    assert '\nbuy' in captured.out


def test_parser_report(capsys):
    super.parse_args(['report', '--mode', 'buy', '--date-search', '0001-01-01', '--until', '9999-12-31'])
    captured = capsys.readouterr()
    assert '\nbuy' in captured.out


def test_parser_report_inventory(capsys):
    super.parse_args(['report', '-m', 'inventory', '-ds', '0001-01-01', '-u', '9999-12-31'])
    captured = capsys.readouterr()
    assert '\ninventory' in captured.out


def test_parser_report_sell(capsys):
    super.parse_args(['report', '-m', 'sell', '-ds', '0001-01-01', '-u', '9999-12-31'])
    captured = capsys.readouterr()
    assert '\nsell' in captured.out
