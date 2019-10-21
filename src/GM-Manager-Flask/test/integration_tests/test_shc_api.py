import requests
import constants


class TestShcApi:

    def test_get_ai_battle_data(self):
        response = requests.get(constants.FLASK_BACKEND_URL + constants.API_STRONGHOLD_GET_AI_BATTLE)

        assert response is not None
        assert response.status_code == 200
