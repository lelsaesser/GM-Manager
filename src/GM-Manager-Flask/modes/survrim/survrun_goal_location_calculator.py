from typing import Union, Tuple, Any

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

    def calc_time_limit(self, location_a: str, location_b: str) -> int:
        """
        Calculate time limit for a survrun game based on the distance of both targets
        :param location_a: first target location (expects a CITY_* constant)
        :param location_b: second target location (expects a CITY_* constant)
        :return: integer which represents the time in minutes
        :raises: ValueError, if either of the params are not a CITY constant
        """
        if location_a not in constants.LIST_SURVRUN_TARGET_LOCATIONS:
            raise ValueError
        if location_b not in constants.LIST_SURVRUN_TARGET_LOCATIONS:
            raise ValueError

        sector_a = constants.LIST_SURVRUN_SECTOR_A
        sector_b = constants.LIST_SURVRUN_SECTOR_B
        sector_c = constants.LIST_SURVRUN_SECTOR_C
        sector_d = constants.LIST_SURVRUN_SECTOR_D
        sector_e = constants.LIST_SURVRUN_SECTOR_E

        time_factor = 0
        sectors = []
        time_factors_per_sector = {
            "sector_a": 1,
            "sector_b": 2,
            "sector_c": 3,
            "sector_d": 4,
            "sector_e": 5,
        }

        if location_a in sector_a or location_b in sector_a:
            sectors.append("sector_a")
        if location_a in sector_b or location_b in sector_b:
            sectors.append("sector_b")
        if location_a in sector_c or location_b in sector_c:
            sectors.append("sector_c")
        if location_a in sector_d or location_b in sector_d:
            sectors.append("sector_d")
        if location_a in sector_e or location_b in sector_e:
            sectors.append("sector_e")

        if len(sectors) == 1:
            return constants.TIME_SURVRUN_MIN_TIMEBOX
        elif len(sectors) == 2:
            time_factor = abs(time_factors_per_sector.get(sectors[0]) - time_factors_per_sector.get(sectors[1]))
        else:
            raise Exception("len(sectors) is expected to be 1 or 2. Actual: ", len(sectors))

        if time_factor == 1:
            return constants.TIME_SURVRUN_MIN_TIMEBOX + 10
        elif time_factor == 2:
            return constants.TIME_SURVRUN_MIN_TIMEBOX + 20
        elif time_factor == 3:
            return constants.TIME_SURVRUN_MIN_TIMEBOX + 30
        elif time_factor == 4:
            return constants.TIME_SURVRUN_MAX_TIMEBOX
        else:
            raise Exception("time_factor is expected to be in range(0, 5). Actual: ", time_factor)

    def calc_time_limit_with_randomness(self, location_a: str, location_b: str) -> Tuple[Union[int, Any], str]:
        """
        Calculate survrun timebox with some randomness (+- 10min)
        :param location_a: first target location (expects a CITY_* constant)
        :param location_b: second target location (expects a CITY_* constant)
        :return: integer which represents the time in minutes, string containing the difficulty rating
        """
        time_mod = random.randint(-15, 25)
        if time_mod < -10:
            difficulty_rating = "Hardcore Extreme"
        elif -10 <= time_mod < -5:
            difficulty_rating = "Extreme"
        elif -5 <= time_mod < 0:
            difficulty_rating = "Difficult"
        elif 0 <= time_mod < 6:
            difficulty_rating = "Harsh"
        elif 6 <= time_mod < 15:
            difficulty_rating = "Normal"
        elif 15 <= time_mod < 21:
            difficulty_rating = "Promising"
        elif 21 <= time_mod <= 25:
            difficulty_rating = "Easy"
        else:
            raise Exception("Error: time_mod is expected to be in range(-15, 26). Actual: ", time_mod)

        return self.calc_time_limit(location_a, location_b) + time_mod, difficulty_rating
