from modes.misc.brainstorm import MiscBrainstorm
from modes.misc import constants as c


class TestMiscBrainstorm:

    def test_calc_exercise(self):
        mock = MiscBrainstorm()
        test_returns = []

        for math_symbol in c.LIST_MATH_SYMBOLS:
            test_returns.append(mock.calc_exercise(c.LIST_DIFFICULTIES[2], math_symbol))

        for exercise in test_returns:
            if exercise[0][1] == c.LIST_MATH_SYMBOLS[0]:
                assert exercise[0][0] + exercise[0][2] == exercise[1]
            elif exercise[0][1] == c.LIST_MATH_SYMBOLS[1]:
                assert exercise[0][0] * exercise[0][2] == exercise[1]
            elif exercise[0][1] == c.LIST_MATH_SYMBOLS[2]:
                assert exercise[0][0] - exercise[0][2] == exercise[1]
            elif exercise[0][1] == c.LIST_MATH_SYMBOLS[3]:
                assert exercise[0][0] / exercise[0][2] == exercise[1]

    def test_get_exercise_list(self):
        mock = MiscBrainstorm()

        for difficulty in c.LIST_DIFFICULTIES:
            exercises = mock.get_exercise_list(difficulty, 10)
            assert exercises is not None
            assert len(exercises[0][c.MISC_KEY_EXERCISE]) == 3
            assert exercises[0][c.MISC_KEY_SOLUTION] is not None
