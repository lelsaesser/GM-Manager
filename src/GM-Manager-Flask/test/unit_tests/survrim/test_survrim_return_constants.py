from modes.survrim import constants as c
from modes.survrim.survrim_return_constants import SurvrimReturnConstants


class TestSurvrimReturnConstants:

    def test_survrim_get_constants(self):
        target_location_list_sorted = sorted(c.LIST_SURVRUN_TARGET_LOCATIONS)

        return_value = SurvrimReturnConstants.survrim_get_constants()[c.SR_KEY_SURVRIM_CONSTANTS][0]

        assert return_value is not None
        assert return_value[c.SR_KEY_LIST_SURVRUN_TARGET_LOCATIONS] == target_location_list_sorted
        assert return_value[c.SR_KEY_LIST_SURVRIM_SKILLS] == c.LIST_SURVRIM_SKILLS
        assert return_value[c.SR_KEY_LIST_SURVRIM_CLASSES] == c.LIST_SURVRIM_CLASSES
        assert return_value[c.SR_KEY_LIST_SURVRUN_DIFFICULTIES] == c.LIST_SURVRUN_DIFFICULTIES
