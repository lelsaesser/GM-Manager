from modes.survrim import constants
import random


class SurvrunGoalLocationCalculator:
    """
    calculate goal/target locations for survivalrun
    """
    def __init__(self):
        self._locations = constants.LIST_SURVRUN_TARGET_LOCATIONS
        self._loc_idx_a = 0
        self._loc_idx_b = 0

    def calc_goal_locations(self):
        """
        Calculate two random target locations for Survialrun
        :return: string tuple of length 2, which contains the full names of both chosen locations
        """
        while self._loc_idx_a == self._loc_idx_b:
            self._loc_idx_a = random.randint(1, len(self._locations) - 1)
            self._loc_idx_b = random.randint(1, len(self._locations) - 1)

        return self._locations[self._loc_idx_a], self._locations[self._loc_idx_b]
