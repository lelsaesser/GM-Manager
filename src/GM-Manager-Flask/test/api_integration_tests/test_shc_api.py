import constants
from utils.api_helper import GmManagerApiHelper as h


class TestShcApi:

    def test_get_ai_battle_data_with_ai_count(self):
        for ai_count in range(2, 9):
            payload = {'shc_ai_battle_player_count': ai_count}
            response = h.api_post_request(constants.FLASK_BACKEND_URL + constants.API_STRONGHOLD_GET_AI_BATTLE, payload)

            assert response is not None
            assert response.status_code == 200
