import random

from modes.misc import constants as misc_constants


class MiscBrainstorm:

    def __init__(self):
        self.num_a = None
        self.num_b = None
        self.math_symbol = None

    def get_easy_exercise(self) -> str:
        self.num_a, self.num_b = random.randint(0, 10), random.randint(0, 10)
        self.math_symbol = random.randint(0, 3)

        return str(self.num_a) + misc_constants.LIST_MATH_SYMBOLS[self.math_symbol] + str(self.num_b)

    def get_medium_exercise(self) -> str:
        self.num_a, self.num_b = random.randint(0, 10), random.randint(0, 100)
        self.math_symbol = random.randint(0, 3)

        return str(self.num_a) + misc_constants.LIST_MATH_SYMBOLS[self.math_symbol] + str(self.num_b)

    def get_hard_exercise(self) -> str:
        self.num_a, self.num_b = random.randint(10, 100), random.randint(10, 100)
        self.math_symbol = random.randint(0, 3)

        return str(self.num_a) + misc_constants.LIST_MATH_SYMBOLS[self.math_symbol] + str(self.num_b)

    def get_exercise_list(self, difficulty: int, length: int) -> list:
        exercises = []
        if difficulty == 0:
            for i in range(length):
                exercises.append(self.get_easy_exercise())
        elif difficulty == 1:
            for i in range(length):
                exercises.append(self.get_medium_exercise())
        elif difficulty == 2:
            for i in range(length):
                exercises.append(self.get_hard_exercise())
        else:
            print("Error: difficulty must be 0, 1 or 2")
            raise ValueError

        return exercises
