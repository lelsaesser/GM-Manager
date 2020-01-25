from modes.misc.misc_return_constants import MiscReturnConstants
from modes.misc import constants as misc_constants


class TestMiscGetConstants:

    def test_misc_get_constants(self):
        return_value = MiscReturnConstants.misc_get_constants()

        assert return_value is not None
        assert return_value['misc_constants'][0]['LIST_MATH_SYMBOLS'] == misc_constants.LIST_MATH_SYMBOLS
        assert return_value['misc_constants'][0]['LIST_DIFFICULTIES'] == misc_constants.LIST_DIFFICULTIES
