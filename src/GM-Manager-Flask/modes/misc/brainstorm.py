import random

from modes.misc import constants as c


class MiscBrainstorm:

    def __init__(self):
        self.num_a = 0
        self.num_b = 0

    def calc_exercise(self, difficulty: str, math_symbol: str):
        # + or * exercise
        if math_symbol == c.LIST_MATH_SYMBOLS[0] or math_symbol == c.LIST_MATH_SYMBOLS[1]:
            if difficulty == c.LIST_DIFFICULTIES[0]:
                self.num_a, self.num_b = random.randint(2, 10), random.randint(2, 10)
            elif difficulty == c.LIST_DIFFICULTIES[1]:
                self.num_a, self.num_b = random.randint(2, 10), random.randint(2, 100)
            elif difficulty == c.LIST_DIFFICULTIES[2]:
                self.num_a, self.num_b = random.randint(10, 100), random.randint(10, 100)
            else:
                raise Exception(c.MISC_ERROR_INVALID_MATH_SYMBOL)
            if math_symbol == c.LIST_MATH_SYMBOLS[0]:
                return [self.num_a, math_symbol, self.num_b], self.num_a + self.num_b
            else:
                return [self.num_a, math_symbol, self.num_b], self.num_a * self.num_b

        # - exercise
        elif math_symbol == c.LIST_MATH_SYMBOLS[2]:
            if difficulty == c.LIST_DIFFICULTIES[0]:
                while self.num_a == self.num_b:
                    self.num_a, self.num_b = random.randint(2, 10), random.randint(2, 10)
            elif difficulty == c.LIST_DIFFICULTIES[1]:
                while self.num_a == self.num_b:
                    self.num_a, self.num_b = random.randint(2, 10), random.randint(2, 100)
            elif difficulty == c.LIST_DIFFICULTIES[2]:
                while self.num_a == self.num_b:
                    self.num_a, self.num_b = random.randint(10, 100), random.randint(10, 100)
            else:
                raise Exception(c.MISC_ERROR_INVALID_MATH_SYMBOL)
            return [self.num_a, math_symbol, self.num_b], self.num_a - self.num_b

        # / exercise
        elif math_symbol == c.LIST_MATH_SYMBOLS[3]:
            if difficulty == c.LIST_DIFFICULTIES[0]:
                self.num_b = random.randint(2, 10)
                random_mult = random.randint(2, 10)
            elif difficulty == c.LIST_DIFFICULTIES[1]:
                self.num_b = random.randint(10, 100)
                random_mult = random.randint(2, 10)
            elif difficulty == c.LIST_DIFFICULTIES[2]:
                self.num_b = random.randint(10, 100)
                random_mult = random.randint(10, 20)
            else:
                raise Exception(c.MISC_ERROR_INVALID_MATH_SYMBOL)
            self.num_a = self.num_b * random_mult
            return [self.num_a, math_symbol, self.num_b], self.num_a / self.num_b

    def get_exercise_list(self, difficulty: str, length: int) -> list:
        exercises = []
        math_symbol = random.randint(0, 3)

        while len(exercises) != length:
            exercise, solution = self.calc_exercise(difficulty, c.LIST_MATH_SYMBOLS[math_symbol])
            if exercise not in exercises:
                exercises.append(
                    {
                        c.MISC_KEY_EXERCISE: exercise,
                        c.MISC_KEY_SOLUTION: solution
                    }
                )
            return exercises
