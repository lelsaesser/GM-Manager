from modes.eso.eso_return_constants import EsoReturnConstants
from modes.eso import constants


class TestEsoReturnConstants:

    def test_eso_get_constants(self):
        result = EsoReturnConstants.eso_get_constants()

        assert result['eso_constants'][0]['LIST_ESO_CLASSES'] == constants.LIST_ESO_CLASSES
        assert result['eso_constants'][0]['LIST_ESO_DUNGEONS'] == constants.LIST_ESO_DUNGEONS
        assert result['eso_constants'][0]['LIST_ESO_RAIDS'] == constants.LIST_ESO_RAIDS
