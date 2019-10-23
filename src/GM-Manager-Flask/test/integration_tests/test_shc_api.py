import requests
import constants


class TestShcApi:

    def test_get_ai_battle_data(self):
        response = requests.get(constants.FLASK_BACKEND_URL + constants.API_STRONGHOLD_GET_AI_BATTLE)

        assert response is not None
        assert response.status_code == 200

    def test_get_ai_battle_data_with_ai_count(self):
        for ai_count in range(2, 9):
            payload = {'shc_ai_battle_player_count': ai_count}
            response = requests.post(constants.FLASK_BACKEND_URL + constants.API_STRONGHOLD_GET_AI_BATTLE, json=payload)

            assert response is not None
            assert response.status_code == 200
