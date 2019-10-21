from modes.survrim.survrun_goal_location_calculator import SurvrunGoalLocationCalculator


class TestSurvrunGoalLocationCalculator:

    def test_calc_goal_locations(self):
        obj = SurvrunGoalLocationCalculator()
        test_locations = obj.calc_goal_locations()
        assert test_locations is not None
        assert len(test_locations) == 2
        assert type(test_locations[0]) == str
        assert type(test_locations[1]) == str
