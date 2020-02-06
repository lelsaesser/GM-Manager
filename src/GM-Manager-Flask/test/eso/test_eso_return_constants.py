from modes.eso import constants as c
from modes.eso.eso_return_constants import EsoReturnConstants


class TestEsoReturnConstants:

    def test_eso_get_constants(self):
        result = EsoReturnConstants.eso_get_constants()

        assert result[c.ESO_KEY_ESO_CONSTANTS][0][c.ESO_KEY_LIST_ESO_CLASSES] == c.LIST_ESO_CLASSES
        assert result[c.ESO_KEY_ESO_CONSTANTS][0][c.ESO_KEY_LIST_ESO_DUNGEONS] == c.LIST_ESO_DUNGEONS
        assert result[c.ESO_KEY_ESO_CONSTANTS][0][c.ESO_KEY_LIST_ESO_RAIDS] == c.LIST_ESO_RAIDS
