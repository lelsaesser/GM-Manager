from modes.misc import constants as c
from modes.misc.misc_return_constants import MiscReturnConstants


class TestMiscGetConstants:

    def test_misc_get_constants(self):
        return_value = MiscReturnConstants.misc_get_constants()

        assert return_value is not None
        assert return_value[c.MISC_KEY_MISC_CONSTANTS][0][c.MISC_KEY_LIST_MATH_SYMBOLS] == c.LIST_MATH_SYMBOLS
        assert return_value[c.MISC_KEY_MISC_CONSTANTS][0][c.MISC_KEY_LIST_DIFFICULTIES] == c.LIST_DIFFICULTIES
