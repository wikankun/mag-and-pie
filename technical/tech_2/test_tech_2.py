from .main import smallest_less_five

def test_case_1_result():
    result = smallest_less_five('12345')
    assert result == 1234

def test_case_1_type():
    result = smallest_less_five('12345')
    assert type(result) == int

def test_case_2():
    assert smallest_less_five('5005') == 5

def test_case_3():
    assert smallest_less_five('5115') == 115

def test_case_4():
    assert smallest_less_five('-4565') == -465

def test_case_5():
    assert smallest_less_five('-6545') == -654

def test_case_6():
    assert smallest_less_five('5') == 0

def test_case_7():
    assert smallest_less_five('15') == 1

def test_case_8():
    assert smallest_less_five('-5') == 0

def test_case_9():
    assert smallest_less_five('-15') == -1

def test_case_9():
    assert smallest_less_five('-6005') == -600

def test_case_9():
    assert smallest_less_five('-5004') == -4