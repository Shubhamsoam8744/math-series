from math_series.series import fibonacci,lucas,sum_series


####################################
# Testing fibonacci
def test_negative_value():
    actual= fibonacci(-4)
    expected= "Invalid Input"
    assert actual==expected

def test_zero():
    actual= fibonacci(0)
    expected= 0
    assert actual==expected

def test_1st_num():
    actual= fibonacci(1)
    expected= 1
    assert actual==expected

def test_5th_num():
    actual= fibonacci(5)
    expected= 5
    assert actual==expected

def test_7th_num():
    actual= fibonacci(7)
    expected= 13
    assert actual==expected

##################################



####################################
# Testing lucas
def test_negative_value_lucas():
    actual= lucas(-4)
    expected= "Invalid Input"
    assert actual==expected

def test_zero_lucas():
    actual= lucas(0)
    expected= 2
    assert actual==expected

def test_1st_num_lucas():
    actual= lucas(1)
    expected= 1
    assert actual==expected

def test_5th_num_lucas():
    actual= lucas(5)
    expected= 11
    assert actual==expected

def test_7th_num_lucas():
    actual= lucas(7)
    expected= 29
    assert actual==expected

##################################



####################################
# Testing sum_series
def test_negative_value_sum_series():
    actual= sum_series(-4)
    expected= "Invalid Input"
    assert actual==expected

def test_zero_sum_series():
    actual= sum_series(0)
    expected= 0
    assert actual==expected

def test_1st_num_sum_series():
    actual= sum_series(1)
    expected= 1
    assert actual==expected

def test_5th_num_sum_series_with_defaults():
    actual= sum_series(5)
    expected= 5
    assert actual==expected

def test_5th_num_sum_series_without_defaults():
    actual= sum_series(5,10,10)
    expected= 80
    assert actual==expected

##################################