from modes.misc.brainstorm import MiscBrainstorm
from modes.misc import constants as misc_constants


class TestMiscBrainstorm:

    def test_calc_exercise(self):
        mock = MiscBrainstorm()
        test_returns = []

        for math_symbol in misc_constants.LIST_MATH_SYMBOLS:
            test_returns.append(mock.calc_exercise(misc_constants.LIST_DIFFICULTIES[0], math_symbol))

        for exercise in test_returns:
            if exercise[0][1] == "+":
                assert exercise[0][0] + exercise[0][2] == exercise[1]
            elif exercise[0][1] == "*":
                assert exercise[0][0] * exercise[0][2] == exercise[1]

    def test_get_exercise_list(self):
        mock = MiscBrainstorm()

        for difficulty in misc_constants.LIST_DIFFICULTIES:
            exercises = mock.get_exercise_list(difficulty, 10)
            assert exercises is not None
            assert len(exercises[0]['exercise']) == 3
            assert isinstance(exercises[0]['solution'], int)
