import constants
from modes.misc import constants as misc_constants
from utils.api_helper import GmManagerApiHelper as h


class TestBrainstormApi:

    def test_misc_get_constants(self):
        response = h.api_get_request(constants.FLASK_BACKEND_URL + constants.API_MISC_GET_CONSTANTS)

        assert response is not None
        assert response.status_code == 200

        data = response.json()['misc_constants'][0]
        assert data['LIST_MATH_SYMBOLS'] == misc_constants.LIST_MATH_SYMBOLS
        assert data['LIST_DIFFICULTIES'] == misc_constants.LIST_DIFFICULTIES

    def test_misc_brainstorm_get_exercise_list(self):
        payload = {
            'data': {
                'formBrainstormDifficulty': misc_constants.LIST_DIFFICULTIES[0]
            }
        }
        response = h.api_post_request(constants.FLASK_BACKEND_URL + constants.API_MISC_BRAINSTORM_GET_EXERCISE_LIST,
                                      payload)

        assert response is not None
        assert response.status_code == 200

        data = response.json()['exercises'][0]
        assert len(data['exercise']) == 3
        assert data['solution'] is not None
