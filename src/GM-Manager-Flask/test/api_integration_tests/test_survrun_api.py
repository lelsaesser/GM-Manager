import json

import constants
import modes.survrim.constants as c
from utils.api_helper import GmManagerApiHelper as h


class TestSurvrunApi:

    def test_get_target_location_data(self):
        response = h.api_get_request(constants.FLASK_BACKEND_URL + constants.API_SURVRUN_GET_TARGET_LOCATION)

        assert response is not None
        assert response.status_code == 200

        unique_locations_in_response = 0
        for location in c.LIST_SURVRUN_TARGET_LOCATIONS:
            if unique_locations_in_response == 2:
                break
            if location in response.text:
                unique_locations_in_response += 1
        assert unique_locations_in_response == 2

        data = json.loads(response.text)
        assert type(data[c.SR_KEY_SURVRUN_DATA][0][c.SR_KEY_TARGET_LOCATION_ONE]) == str
        assert type(data[c.SR_KEY_SURVRUN_DATA][0][c.SR_KEY_TARGET_LOCATION_TWO]) == str
        assert data[c.SR_KEY_SURVRUN_DATA][0][c.SR_KEY_TIMEBOX] is not None
        assert type(data[c.SR_KEY_SURVRUN_DATA][0][c.SR_KEY_TIMEBOX]) == int

    def test_survrun_query_get_runs(self):
        """
        Test survrun get all data query. This tests fails if the survrun_runs table is empty.
        """
        response = h.api_get_request(constants.FLASK_BACKEND_URL + constants.API_SURVRUN_GET_ALL_DB_RUN_DATA)
        data = json.loads(response.content)["queryResult"][0]

        assert response is not None
        assert response.status_code == 200
        assert type(data[c.SR_KEY_ID]) == int
        assert data[c.SR_KEY_PLAYER_CLASS] in c.LIST_SURVRIM_CLASSES
        assert data[c.SR_KEY_TARGET_A] in c.LIST_SURVRUN_TARGET_LOCATIONS
        assert data[c.SR_KEY_TARGET_B] in c.LIST_SURVRUN_TARGET_LOCATIONS
        assert type(data[c.SR_KEY_TIMEBOX]) == int
        assert data[c.SR_KEY_COMPLETED] == c.SURVRIM_YES or data[c.SR_KEY_COMPLETED] == c.SURVRIM_NO
        assert type(data[c.SR_KEY_TIME_NEEDED]) == int
        assert type(data[c.SR_KEY_R_COUNT]) == int

    def test_survrun_get_constants(self):
        response = h.api_get_request(constants.FLASK_BACKEND_URL + constants.API_SURVRUN_GET_CONSTANTS)
        data = json.loads(response.content)[c.SR_KEY_SURVRIM_CONSTANTS][0]

        assert response.status_code == 200
        assert data is not None
