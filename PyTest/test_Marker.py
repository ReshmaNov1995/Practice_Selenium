import pytest

a = 200


@pytest.mark.kr
def test_method1():
    print("Am a method 1")


@pytest.mark.skip
def test_method2():
    print("Am a method 2")


@pytest.mark.skip(reason="rr")
def test_method3():
    print("Am a method 3")


@pytest.mark.skipif(condition=a == 100, reason="condition is skipped")
def test_method4():
    print("Am a method 4")


@pytest.mark.xfail
def test_method5():
    print("Am a method 5")
    raise Exception


@pytest.mark.xfail(raises=NameError, reason="condition is failed")
def test_method6():
    print("Am a method 6")
    print(kk)
    raise Exception

@pytest.mark.xfail(condition=a == 200, reason="condition is failed")
def test_method6():
    print("Am a method 6")
    print(kk)
    raise Exception