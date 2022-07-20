def averageIMP(my_list: list) -> float:
    """
    :param my_list: list of numbers
    :return: the avrage
    """
    return sum(my_list) / len(my_list)


def medianIMP(my_list: list) -> float:
    """
    :param my_list: list of age's
    :return: the median value from the list
    """
    # sort the val's in list
    my_list.sort()
    # If the length is even then we return the average of the two mean values
    if len(my_list) % 2 == 0:
        return (averageIMP([my_list[len(my_list) // 2], my_list[len(my_list) // 2 - 1]]))

    # length is not even and there is one middle value
    return (my_list[len(my_list) // 2])


def test_answer():
    assert medianIMP([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5