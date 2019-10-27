import json

import requests

import constants
import modes.survrim.constants as survrim_constants
from database import constants as db_constants


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

    def test_survrun_query_get_runs(self):
        """
        Test survrun get all data query. This tests fails if the survrun_runs table is empty.
        """
        response = requests.get(constants.FLASK_BACKEND_URL + constants.API_SURVRUN_GET_ALL_DB_RUN_DATA)
        data = json.loads(response.content)["queryResult"][0]

        assert response is not None
        assert response.status_code == 200
        assert type(data["id"]) == int
        assert data["player_class"] in survrim_constants.LIST_SURVRIM_CLASSES
        assert data["target_a"] in survrim_constants.LIST_SURVRUN_TARGET_LOCATIONS
        assert data["target_b"] in survrim_constants.LIST_SURVRUN_TARGET_LOCATIONS
        assert type(data["timebox"]) == int
        assert data["completed"] == "yes" or data["completed"] == "no"
        assert type(data["time_needed"]) == int
        assert type(data["r_count"]) == int

    def test_survrun_get_constants(self):
        response = requests.get(constants.FLASK_BACKEND_URL + constants.API_SURVRUN_GET_CONSTANTS)
        data = json.loads(response.content)["survrim_constants"][0]

        assert response.status_code == 200
        assert data is not None
