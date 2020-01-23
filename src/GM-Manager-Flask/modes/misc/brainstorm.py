import random

from modes.misc import constants as misc_constants


class MiscBrainstorm:

    def __init__(self):
        self.num_a = 0
        self.num_b = 0
        self.math_symbol = None

    def calc_exercise(self, difficulty: str):
        self.math_symbol = random.randint(0, 1)  # TODO: fix this, enable - and / exercises

        # + or * exercise
        if -1 < self.math_symbol < 2:
            if difficulty == misc_constants.LIST_DIFFICULTIES[0]:
                self.num_a, self.num_b = random.randint(2, 10), random.randint(2, 10)
            elif difficulty == misc_constants.LIST_DIFFICULTIES[1]:
                self.num_a, self.num_b = random.randint(2, 10), random.randint(2, 100)
            elif difficulty == misc_constants.LIST_DIFFICULTIES[2]:
                self.num_a, self.num_b = random.randint(10, 100), random.randint(10, 100)
            else:
                print("Error: difficulty must be 0, 1, 2 or 3")
                raise ValueError
            if self.math_symbol == 0:
                return [self.num_a, self.math_symbol, self.num_b], self.num_a + self.num_b
            else:
                return [self.num_a, self.math_symbol, self.num_b], self.num_a * self.num_b

        # - exercise
        elif self.math_symbol == 2:
            if difficulty == misc_constants.LIST_DIFFICULTIES[0]:
                while self.num_a == self.num_b or self.num_a < self.num_b:
                    self.num_a, self.num_b = random.randint(2, 10), random.randint(2, 10)
            elif difficulty == misc_constants.LIST_DIFFICULTIES[1]:
                while self.num_a == self.num_b or self.num_a < self.num_b:
                    self.num_a, self.num_b = random.randint(2, 10), random.randint(2, 100)
            elif difficulty == misc_constants.LIST_DIFFICULTIES[2]:
                while self.num_a == self.num_b or self.num_a < self.num_b:
                    self.num_a, self.num_b = random.randint(10, 100), random.randint(10, 100)
            else:
                print("Error: difficulty must be 0, 1, 2 or 3")
                raise ValueError
            return [self.num_a, self.math_symbol, self.num_b], self.num_a - self.num_b

        # / exercise
        elif self.math_symbol == 3:
            if difficulty == misc_constants.LIST_DIFFICULTIES[0]:
                while self.num_a == self.num_b or self.num_a < self.num_b or isinstance(self.num_a / self.num_b, float):
                    self.num_a, self.num_b = random.randint(2, 10), random.randint(2, 10)
            elif difficulty == misc_constants.LIST_DIFFICULTIES[1]:
                while self.num_a == self.num_b or self.num_a < self.num_b or self.num_a / self.num_b % 1 != 0:
                    self.num_a, self.num_b = random.randint(2, 10), random.randint(2, 100)
            elif difficulty == misc_constants.LIST_DIFFICULTIES[2]:
                while self.num_a == self.num_b or self.num_a < self.num_b or self.num_a / self.num_b % 1 != 0:
                    self.num_a, self.num_b = random.randint(10, 100), random.randint(10, 100)
            else:
                print("Error: difficulty must be 0, 1, 2 or 3")
                raise ValueError
            return [self.num_a, self.math_symbol, self.num_b], self.num_a / self.num_b

    def get_exercise_list(self, difficulty: str, length: int) -> list:
        exercises = []

        while len(exercises) != length:
            exercise, solution = self.calc_exercise(difficulty)
            if exercise not in exercises:
                exercises.append(
                    {
                        'exercise': exercise,
                        'solution': solution
                    }
                )
            return exercises

