import json

import requests

import constants
import modes.survrim.constants as survrim_constants


class TestSurvrunApi:

    def test_get_target_location_data(self):
        response = requests.get(constants.FLASK_BACKEND_URL + constants.API_SURVRUN_GET_TARGET_LOCATION)

        assert response is not None
        assert response.status_code == 200

        unique_locations_in_response = 0
        for location in survrim_constants.LIST_SURVRUN_TARGET_LOCATIONS:
            if unique_locations_in_response == 2:
                break
            if location in response.text:
                unique_locations_in_response += 1
        assert unique_locations_in_response == 2

        data = json.loads(response.text)
        assert type(data["survrunData"][0]["target_location_one"]) == str
        assert type(data["survrunData"][0]["target_location_two"]) == str
        assert data["survrunData"][0]["timebox"] is not None
        assert type(data["survrunData"][0]["timebox"]) == int
