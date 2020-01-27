import random

from modes.misc import constants as misc_constants


class MiscBrainstorm:

    def __init__(self):
        self.num_a = 0
        self.num_b = 0

    def calc_exercise(self, difficulty: str, math_symbol: str):
        # + or * exercise
        if math_symbol == "+" or math_symbol == "*":
            if difficulty == misc_constants.LIST_DIFFICULTIES[0]:
                self.num_a, self.num_b = random.randint(2, 10), random.randint(2, 10)
            elif difficulty == misc_constants.LIST_DIFFICULTIES[1]:
                self.num_a, self.num_b = random.randint(2, 10), random.randint(2, 100)
            elif difficulty == misc_constants.LIST_DIFFICULTIES[2]:
                self.num_a, self.num_b = random.randint(10, 100), random.randint(10, 100)
            else:
                raise Exception("Error: difficulty must be 0, 1, 2 or 3")
            if math_symbol == "+":
                return [self.num_a, math_symbol, self.num_b], self.num_a + self.num_b
            else:
                return [self.num_a, math_symbol, self.num_b], self.num_a * self.num_b

        elif math_symbol == "-":
            if difficulty == misc_constants.LIST_DIFFICULTIES[0]:
                while self.num_a == self.num_b:
                    self.num_a, self.num_b = random.randint(2, 10), random.randint(2, 10)
            elif difficulty == misc_constants.LIST_DIFFICULTIES[1]:
                while self.num_a == self.num_b:
                    self.num_a, self.num_b = random.randint(2, 10), random.randint(2, 100)
            elif difficulty == misc_constants.LIST_DIFFICULTIES[2]:
                while self.num_a == self.num_b:
                    self.num_a, self.num_b = random.randint(10, 100), random.randint(10, 100)
            else:
                raise Exception("Error: difficulty must be 0, 1, 2 or 3")
            return [self.num_a, math_symbol, self.num_b], self.num_a - self.num_b

        elif math_symbol == "/":
            if difficulty == misc_constants.LIST_DIFFICULTIES[0]:
                self.num_b = random.randint(2, 10)
                random_mult = random.randint(2, 10)
            elif difficulty == misc_constants.LIST_DIFFICULTIES[1]:
                self.num_b = random.randint(10, 100)
                random_mult = random.randint(2, 10)
            elif difficulty == misc_constants.LIST_DIFFICULTIES[2]:
                self.num_b = random.randint(10, 100)
                random_mult = random.randint(10, 20)
            else:
                raise Exception("Error: difficulty must be 0, 1, 2 or 3")
            self.num_a = self.num_b * random_mult
            return [self.num_a, math_symbol, self.num_b], self.num_a / self.num_b

    def get_exercise_list(self, difficulty: str, length: int) -> list:
        exercises = []
        math_symbol = random.randint(0, 3)

        while len(exercises) != length:
            exercise, solution = self.calc_exercise(difficulty, misc_constants.LIST_MATH_SYMBOLS[math_symbol])
            if exercise not in exercises:
                exercises.append(
                    {
                        'exercise': exercise,
                        'solution': solution
                    }
                )
            return exercises
