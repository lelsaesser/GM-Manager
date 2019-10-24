from modes.survrim.survrun_goal_location_calculator import SurvrunGoalLocationCalculator
from modes.survrim import constants


class TestSurvrunGoalLocationCalculator:

    def test_calc_goal_locations(self):
        obj = SurvrunGoalLocationCalculator()
        test_locations = obj.calc_goal_locations()

        assert test_locations is not None
        assert len(test_locations) == 2
        assert type(test_locations[0]) == str
        assert type(test_locations[1]) == str

    def test_calc_time(self):
        obj = SurvrunGoalLocationCalculator()
        test_time = obj.calc_time_limit(constants.CITY_RIFTEN, constants.CITY_MARKARTH)

        assert test_time is not None
        assert test_time == 60

        test_time = obj.calc_time_limit(constants.CITY_WINTERHOLD, constants.CITY_WINDHELM)

        assert test_time is not None
        assert test_time == 20
