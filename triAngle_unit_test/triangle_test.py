import pytest
from triangle import triAngle_check, triAngle
def test_in_valid_inpit():
    t1 = triAngle(0, 5, 5)
    assert triAngle_check(t1) == "Invalid Input"
    t2 = triAngle(101, 5, 5)
    assert triAngle_check(t2) == "Invalid Input"
    t3 = triAngle(-1, 5, 5)
    assert triAngle_check(t3) == "Invalid Input"
    t4 = triAngle(1.5, 9, 100)
    assert triAngle_check(t4) == "Invalid Input"
    t5 = triAngle(0.5, 9, 100.5)
    assert triAngle_check(t5) == "Invalid Input"
def test_isosceles():
    t1 = triAngle(5, 5, 3)
    assert triAngle_check(t1) == "Isosceles"
    t2 = triAngle(99, 100, 100)
    assert triAngle_check(t2) == "Isosceles"
    t3 = triAngle(1, 5, 5)
    assert triAngle_check(t3) == "Isosceles"
def test_triangle():
    t1 = triAngle(1, 1, 2)
    assert triAngle_check(t1) == "Not a Triangle"
    t2 = triAngle(2, 3, 5)
    assert triAngle_check(t2) == "Not a Triangle"
def test_equilateral():
    t1 = triAngle(100, 100, 100)
    assert triAngle_check(t1) == "Equilateral"
    t2 = triAngle(5, 5, 5)
    assert triAngle_check(t2) == "Equilateral"
def test_scalene():
    t1 = triAngle(98, 99, 100)
    assert triAngle_check(t1) == "Scalene"
    t2 = triAngle(4, 5, 6)
    assert triAngle_check(t2) == "Scalene"