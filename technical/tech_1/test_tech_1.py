from .main import initiator_of_discount

def test_case_1_string():
    assert initiator_of_discount('3 3 3 3') == 0

def test_case_1_list():
    assert initiator_of_discount([3, 3, 3, 3]) == 0

def test_case_2():
    assert initiator_of_discount('3 4 3') == 0

def test_case_3():
    assert initiator_of_discount('3 4 1') == 2

def test_case_4():
    assert initiator_of_discount('5 6 7 7 4 1') == 4

def test_case_5():
    assert initiator_of_discount('5 6 7 7 6 1') == 5

def test_case_5():
    assert initiator_of_discount('5 4 7 7 6 1') == 1