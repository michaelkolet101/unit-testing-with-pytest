def averageIMP(my_list: list) -> float:
    """
    :param my_list: list of numbers
    :return: the avrage
    """
    return sum(my_list) / len(my_list)


def test_answer():
    assert averageIMP([1, 2, 3, 4, 5]) == 3
