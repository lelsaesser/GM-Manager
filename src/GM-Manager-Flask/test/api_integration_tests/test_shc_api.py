import constants as c
from modes.stronghold import constants as shc_c
from utils.api_helper import GmManagerApiHelper as h


class TestShcApi:

    def test_get_ai_battle_data_with_ai_count(self):
        for ai_count in range(2, 9):
            payload = {shc_c.SHC_KEY_AI_BATTLE_PLAYER_COUNT: ai_count}
            response = h.api_post_request(c.FLASK_BACKEND_URL + c.API_STRONGHOLD_GET_AI_BATTLE, payload)

            assert response is not None
            assert response.status_code == 200
