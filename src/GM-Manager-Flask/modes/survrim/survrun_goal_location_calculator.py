from ..survrim import constants
import random


class SurvrunGoalLocationCalculator:
    """
    calculate goal/target locations for survivalrun
    """
    def __init__(self):
        self._locations = [
            constants.ERROR_LOCATION_MISSING,
            constants.CITY_WINDHELM,
            constants.CITY_FALKREATH,
            constants.CITY_SOLITUDE,
            constants.CITY_MORTHAL,
            constants.CITY_DAWNSTAR,
            constants.CITY_MARKARTH,
            constants.CITY_RIFTEN,
            constants.CITY_WHITERUN,
            constants.CITY_WINTERHOLD,
            constants.LOC_HIGH_HROTHGAR,
            constants.LOC_STAUBMANSGRAB,
            constants.LOC_HEXENFELSENSCHANZE
        ]
        self._loc_idx_a = 0
        self._loc_idx_b = 0

    def calc_goal_locations(self) -> str:
        while self._loc_idx_a == self._loc_idx_b:
            self._loc_idx_a = random.randint(1, len(self._locations) - 1)
            self._loc_idx_b = random.randint(1, len(self._locations) - 1)

        return self._locations[self._loc_idx_a], self._locations[self._loc_idx_b]
