import constants
from modes.misc import constants as c
from utils.api_helper import GmManagerApiHelper as h


class TestBrainstormApi:

    def test_misc_get_constants(self):
        response = h.api_get_request(constants.FLASK_BACKEND_URL + constants.API_MISC_GET_CONSTANTS)

        assert response is not None
        assert response.status_code == 200

        data = response.json()[c.MISC_KEY_MISC_CONSTANTS][0]
        assert data[c.MISC_KEY_LIST_MATH_SYMBOLS] == c.LIST_MATH_SYMBOLS
        assert data[c.MISC_KEY_LIST_DIFFICULTIES] == c.LIST_DIFFICULTIES

    def test_misc_brainstorm_get_exercise_list(self):
        payload = {
            c.MISC_KEY_DATA: {
                c.MISC_KEY_FORM_BRAINSTROM_DIFFICULTY: c.LIST_DIFFICULTIES[0]
            }
        }
        response = h.api_post_request(constants.FLASK_BACKEND_URL + constants.API_MISC_BRAINSTORM_GET_EXERCISE_LIST,
                                      payload)

        assert response is not None
        assert response.status_code == 200

        data = response.json()[c.MISC_KEY_EXERCISES][0]
        assert len(data[c.MISC_KEY_EXERCISE]) == 3
        assert data[c.MISC_KEY_SOLUTION] is not None
