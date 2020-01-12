import random

from modes.misc import constants as misc_constants


class MiscBrainstorm:

    @staticmethod
    def return_easy_exercise() -> str:
        num_a, num_b = random.randint(0, 10), random.randint(0, 10)
        math_symbol = random.randint(0, 3)

        return str(num_a) + misc_constants.LIST_MATH_SYMBOLS[math_symbol] + str(num_b)

    @staticmethod
    def return_medium_exercise() -> str:
        num_a, num_b = random.randint(0, 10), random.randint(0, 100)
        math_symbol = random.randint(0, 3)

        return str(num_a) + misc_constants.LIST_MATH_SYMBOLS[math_symbol] + str(num_b)

    @staticmethod
    def return_hard_exercise() -> str:
        num_a, num_b = random.randint(10, 100), random.randint(10, 100)
        math_symbol = random.randint(0, 3)

        return str(num_a) + misc_constants.LIST_MATH_SYMBOLS[math_symbol] + str(num_b)
