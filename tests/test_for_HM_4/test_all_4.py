import logging


class Date:
    short_days = [4, 6, 9, 11]

    def get_next_day_imp(self, some_date: tuple):
        if some_date[2] % 4 == 0 and some_date[1] == 2 and some_date[0] == 29:
            return 1, 3, some_date[2]

        if (not some_date[2] % 4 == 0) and some_date[1] == 2 and some_date[0] == 28:
            return 1, 3, some_date[2]

        if (some_date[1] in self.short_days and some_date[0] == 30) or (some_date[1] not in self.short_days and
                                                                        some_date[0] == 31 and not some_date[1] == 12):
            return 1, some_date[1] + 1, some_date[2]

        if some_date[1] == 12 and some_date[0] == 31:
            return 1, 1, some_date[2] + 1

        return some_date[0] + 1, some_date[1], some_date[2]

    def __init__(self, day: int, month: int, year: int):
        """
        the format is day.month.year
        :param day:
        :param month:
        :param year:
        """
        self.day = day
        self.month = month
        self.year = year
        if not self.is_valid():
            raise TypeError(f"{day, month, year} date not valid !")

    def __str__(self) -> str:
        """
        :return: data of the class
        """
        return f"\nDate(day = {self.day} ,month = {self.month} , year = {self.year}\n"

    def is_valid(self) -> bool:
        """
        :return:true if the date is valid date else false
        """

        ret_val = True

        if not isinstance(self.day, int) and isinstance(self.month, int) and isinstance(self.year, int):
            ret_val = False

        if self.day == 0 or self.month == 0 or self.year == 0:
            ret_val = False

        if self.day < 1 or self.day > 31:
            ret_val = False

        if self.month < 1 or self.month > 12:
            ret_val = False

        if len(str(self.year)) != 4:
            ret_val = False

        if self.month in self.short_days and self.day > 30:
            ret_val = False

        if self.year % 4 == 0 and self.month == 2 and self.day > 29:
            ret_val = False
        elif (not self.year % 4 == 0) and self.month == 2 and self.day > 28:
            ret_val = False

        return ret_val

    def get_date(self) -> tuple:
        """
        :return: our date
        """
        return self.day, self.month, self.year

    def is_bigger(self, date_a: tuple, date_b: tuple) -> bool:
        """
        for example 22.2.1998 bigger from 23.4.1996
        :param date_a: date that we check if is the big one
        :param date_b: date that date a is big from
        :return: true if date a is bigger else false
        """
        if date_a[2] > date_b[2]:
            return True
        elif date_a[2] == date_b[2] and date_a[1] > date_b[1]:
            return True
        elif date_a[2] == date_b[2] and date_a[1] == date_b[1] and date_a[0] > date_b[0]:
            return True

        return False

    def get_next_day(self) -> object:
        """
        :return:the next day after the date
        """
        date = self.get_next_day_imp((self.day, self.month, self.year))
        return Date(date[0], date[1], date[2])

    def get_next_days(self, days_to_add: int) -> object:
        """
        :param days_to_add: num of days to add to our date
        :return: the date after this days
        """
        date = (self.day, self.month, self.year)

        while not days_to_add == 0:
            date = self.get_next_day_imp(date)
            days_to_add -= 1

        return Date(date[0], date[1], date[2])

    def __lt__(self, other: tuple) -> bool:
        """
        check if our date is the smaller (closer)
        :param other: anther date
        :return: true if our date is the small one else false
        """

        return (not self.is_bigger((self.day, self.month, self.year), other)) and self.__ne__(other)

    def __sub__(self, other: tuple) -> int:
        """
        get the difference between the dates in days
        :param other: some date
        :return: The difference between the dates in the days
        """
        days = 0

        if self.__gt__(other):
            bigger = self.get_date()
            smaller = other
        else:
            bigger = other
            smaller = self.get_date()

        while self.is_bigger(bigger, smaller):
            smaller = self.get_next_day_imp(smaller)
            days += 1

        return days

    def __eq__(self, other: tuple) -> bool:
        """
        :param other: some date
        :return: true is the other date == to our date else false
        """
        return other == (self.day, self.month, self.year)

    def __gt__(self, other: tuple) -> bool:
        """
        :param other: some date
        :return: true if our date is bigger else false
        """
        return self.is_bigger((self.day, self.month, self.year), other)

    def __ne__(self, other: tuple) -> bool:
        """
        :param other: some date
        :return: true if it's not equal else false
        """
        return not other == (self.day, self.month, self.year)

    def __ge__(self, other: tuple) -> bool:
        """
        :param other: other date
        :return: true if our date is bigger or equal to other date
        """
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other: tuple) -> bool:
        """
        :param other: some date
        :return: true if our date in smaller or equal to the other date
        """
        return self.__lt__(other) or self.__eq__(other)


# val's to test with
d1 = Date(29, 2, 2016)
d2 = Date(1, 3, 2017)
d3 = Date(28, 2, 2017)
d4 = Date(31, 12, 9998)
d6 = Date(19, 4, 2016)

# test to __str__
print(d1)

# test to isValid valid date
try:
    d4.is_valid()
    print("is_valid SUCCESS")
except:
    print("is_valid FAIL")


def test_to_get_next_day():
    # test to get_next_day()
    assert d3.get_next_day() == d2
    logging.info("test to get next day")

#
#
# # test to get_next_days
# assert d1.get_next_days(50) == d6.get_date()
#
# # test to __lt__
# assert d3.get_date() < (20, 2, 2018)
#
# # test to __gt__
# assert d3.get_date() > (3, 7, 1956)
#
# assert d3.__sub__((28, 3, 2017)) == 28
#
# # test for __eq__
# assert d3.__eq__((28, 2, 2017))
#
# # test for __ne__
# assert d3.__ne__((29, 2, 2017))
#
# # test for __ge__
# assert d3.__ge__((28, 2, 2015))
#
# # test to __le__
# assert d3.__le__((31, 12, 9998))
