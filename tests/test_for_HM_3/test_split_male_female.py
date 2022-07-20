def ChaeckValIMP(some_dict: dict):
    """
    if it is not a dict msg the user
    :param some_dict: to chaeck if it is a dictuionary
    :return: NON
    """
    if not isinstance(some_dict, dict):
        raise Exception('it is not a dictunery !!!')
    if len(some_dict) < 3:
        raise Exception('dictunery not valid !!!')

data_set = {
        3322117: {
            "name": "Tal",
            "gender": "male",
            "height": 1.90,
            "age": 22
        },
        176864301: {
            "gender": "female",
            "age": 57,
            "height": 1.65,
            "name": "Anat"
        },
        176756301: {
            "gender": "female",
            "age": 80,
            "height": 1.30,
            "name": "branch"
        },
        176654301: {
            "gender": "female",
            "age": 30,
            "height": 1.65,
            "name": "hna"
        },
        176867301: {
            "gender": "male",
            "age": 37,
            "height": 1.80,
            "name": "fafu"
        },
        176826401: {
            "gender": "female",
            "age": 19,
            "height": 1.65,
            "name": "roza"
        },
        176864551: {
            "gender": "male",
            "age": 25,
            "height": 1.85,
            "name": "victor"
        },
        165864651: {
            "gender": "female",
            "age": 41,
            "height": 1.68,
            "name": "banana"
        },
        176436301: {
            "gender": "male",
            "age": 15,
            "height": 1.65,
            "name": "banani"
        }
    }

def split_male_female(data: dict) -> list:
    """
    splet the data to two dict's for male and female
    :param data - dict of all the data male and female
    :return - list of dict's that one is all the male and the second female
    """
    # check valid param
    ChaeckValIMP(data)

    male_dict = {}
    female_dict = {}

    for item in data:
        if data[item]["gender"] == "male":
            male_dict[item] = data[item]
        else:
            female_dict[item] = data[item]

    return [male_dict, female_dict]


def test_answer():
    a = split_male_female(data_set)
    assert isinstance(a, list)
    assert isinstance(a[0], dict)
    assert isinstance(a[1], dict)
