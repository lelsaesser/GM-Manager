from modes.survrim import constants as c
from modes.survrim.survrun_goal_location_calculator import SurvrunGoalLocationCalculator


class TestSurvrunGoalLocationCalculator:

    def test_calc_goal_locations(self):
        mock = SurvrunGoalLocationCalculator()
        test_locations = mock.calc_goal_locations()

        assert test_locations is not None
        assert len(test_locations) == 2
        assert type(test_locations[0]) == str
        assert type(test_locations[1]) == str

    def test_calc_time_limit(self):
        mock = SurvrunGoalLocationCalculator()
        test_time = mock.calc_time_limit(c.CITY_RIFTEN, c.CITY_MARKARTH)

        assert test_time is not None
        assert test_time == c.TIME_SURVRUN_MAX_TIMEBOX

        test_time = mock.calc_time_limit(c.CITY_WINTERHOLD, c.CITY_WINDHELM)

        assert test_time is not None
        assert test_time == c.TIME_SURVRUN_MIN_TIMEBOX

    def test_calc_time_limit_with_randomness(self):
        mock = SurvrunGoalLocationCalculator()
        test_time, test_rating = mock.calc_time_limit_with_randomness(c.CITY_RIFTEN, c.CITY_MARKARTH)

        assert test_time is not None
        assert test_rating is not None
        assert type(test_time) == int
        assert type(test_rating) == str
