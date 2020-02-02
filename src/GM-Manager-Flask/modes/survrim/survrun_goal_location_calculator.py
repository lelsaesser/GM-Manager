from typing import Union, Tuple, Any

from modes.survrim import constants as c
import random


class SurvrunGoalLocationCalculator:
    """
    calculate goal/target locations for survivalrun
    """
    def __init__(self):
        self._locations = c.LIST_SURVRUN_TARGET_LOCATIONS
        self._loc_idx_a = 0
        self._loc_idx_b = 0

    def calc_goal_locations(self):
        """
        Calculate two random target locations for Survialrun
        :return: string tuple of length 2, which contains the full names of both chosen locations
        """
        while self._loc_idx_a == self._loc_idx_b:
            self._loc_idx_a = random.randint(0, len(self._locations) - 1)
            self._loc_idx_b = random.randint(0, len(self._locations) - 1)

        return self._locations[self._loc_idx_a], self._locations[self._loc_idx_b]

    def calc_time_limit(self, location_a: str, location_b: str) -> int:
        """
        Calculate time limit for a survrun game based on the distance of both targets
        :param location_a: first target location (expects a CITY_* constant)
        :param location_b: second target location (expects a CITY_* constant)
        :return: integer which represents the time in minutes
        :raises: ValueError, if either of the params are not a CITY constant
        """
        if location_a not in c.LIST_SURVRUN_TARGET_LOCATIONS:
            raise ValueError
        if location_b not in c.LIST_SURVRUN_TARGET_LOCATIONS:
            raise ValueError

        sector_a = c.LIST_SURVRUN_SECTOR_A
        sector_b = c.LIST_SURVRUN_SECTOR_B
        sector_c = c.LIST_SURVRUN_SECTOR_C
        sector_d = c.LIST_SURVRUN_SECTOR_D
        sector_e = c.LIST_SURVRUN_SECTOR_E

        time_factor = 0
        sectors = []
        time_factors_per_sector = {
            c.SR_KEY_SECTOR_A: 1,
            c.SR_KEY_SECTOR_B: 2,
            c.SR_KEY_SECTOR_C: 3,
            c.SR_KEY_SECTOR_D: 4,
            c.SR_KEY_SECTOR_E: 5,
        }

        if location_a in sector_a or location_b in sector_a:
            sectors.append(c.SR_KEY_SECTOR_A)
        if location_a in sector_b or location_b in sector_b:
            sectors.append(c.SR_KEY_SECTOR_B)
        if location_a in sector_c or location_b in sector_c:
            sectors.append(c.SR_KEY_SECTOR_C)
        if location_a in sector_d or location_b in sector_d:
            sectors.append(c.SR_KEY_SECTOR_D)
        if location_a in sector_e or location_b in sector_e:
            sectors.append(c.SR_KEY_SECTOR_E)

        if len(sectors) == 1:
            return c.TIME_SURVRUN_MIN_TIMEBOX
        elif len(sectors) == 2:
            time_factor = abs(time_factors_per_sector.get(sectors[0]) - time_factors_per_sector.get(sectors[1]))
        else:
            raise Exception(c.SR_ERROR_INVALID_SECTOR_LENGTH, len(sectors))

        if time_factor == 1:
            return c.TIME_SURVRUN_MIN_TIMEBOX + 10
        elif time_factor == 2:
            return c.TIME_SURVRUN_MIN_TIMEBOX + 20
        elif time_factor == 3:
            return c.TIME_SURVRUN_MIN_TIMEBOX + 30
        elif time_factor == 4:
            return c.TIME_SURVRUN_MAX_TIMEBOX
        else:
            raise Exception(c.SR_ERROR_INVALID_TIME_FACTOR, time_factor)

    def calc_time_limit_with_randomness(self, location_a: str, location_b: str) -> Tuple[Union[int, Any], str]:
        """
        Calculate survrun timebox with some randomness (+- 10min)
        :param location_a: first target location (expects a CITY_* constant)
        :param location_b: second target location (expects a CITY_* constant)
        :return: integer which represents the time in minutes, string containing the difficulty rating
        """
        time_mod = random.randint(-15, 25)
        if time_mod < -10:
            difficulty_rating = c.DIFFICULTY_HARDCORE
        elif -10 <= time_mod < -5:
            difficulty_rating = c.DIFFICULTY_EXTREME
        elif -5 <= time_mod < 0:
            difficulty_rating = c.DIFFICULTY_DIFFICULT
        elif 0 <= time_mod < 6:
            difficulty_rating = c.DIFFICULTY_HARSH
        elif 6 <= time_mod < 15:
            difficulty_rating = c.DIFFICULTY_NORMAL
        elif 15 <= time_mod < 21:
            difficulty_rating = c.DIFFICULTY_PROMISING
        elif 21 <= time_mod <= 25:
            difficulty_rating = c.DIFFICULTY_EASY
        else:
            raise Exception(c.SR_ERROR_INVALID_TIME_MOD, time_mod)

        return self.calc_time_limit(location_a, location_b) + time_mod, difficulty_rating
