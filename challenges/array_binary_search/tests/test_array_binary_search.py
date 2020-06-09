from array_binary_search import __version__, array_binary_search


def test_version():
    assert __version__ == "0.1.0"


def test_wiring():
    assert array_binary_search


def test_notfound_arr1():
    assert array_binary_search([11, 22, 33, 44, 55, 66, 77], 90) == -1


def test_found_arr1():
    assert array_binary_search([4, 8, 15, 16, 23, 42], 15) == 2


def test_real_big_arr():
    assert array_binary_search([i for i in range(100000)], 1) == 1


def test_real_real_real_big_arr():
    assert array_binary_search([i for i in range(100000000)], 1) ==1


def test_real_real_real_big_arr_native_method():
    assert [i for i in range(100000000)].index(1) ==1