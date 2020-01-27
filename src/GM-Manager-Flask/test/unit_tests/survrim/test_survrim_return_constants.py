from modes.survrim import constants as survrim_constants
from modes.survrim.survrim_return_constants import SurvrimReturnConstants


class TestSurvrimReturnConstants:

    def test_survrim_get_constants(self):
        target_location_list_sorted = sorted(survrim_constants.LIST_SURVRUN_TARGET_LOCATIONS)

        return_value = SurvrimReturnConstants.survrim_get_constants()['survrim_constants'][0]

        assert return_value is not None
        assert return_value['LIST_SURVRUN_TARGET_LOCATIONS'] == target_location_list_sorted
        assert return_value['LIST_SURVRIM_SKILLS'] == survrim_constants.LIST_SURVRIM_SKILLS
        assert return_value['LIST_SURVRIM_CLASSES'] == survrim_constants.LIST_SURVRIM_CLASSES
        assert return_value['LIST_SURVRUN_DIFFICULTIES'] == survrim_constants.LIST_SURVRUN_DIFFICULTIES
