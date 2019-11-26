import requests
import constants
from modes.eso import constants as eso_constants
from database.query_eso_dungeon_table import QueryEsoTable


class TestEsoApi:

    def test_eso_get_constants(self):
        response = requests.get(constants.FLASK_BACKEND_URL + constants.API_ESO_GET_CONSTANTS)

        assert response is not None
        assert response.status_code == 200

        data = response.json()['eso_constants'][0]
        assert data["LIST_ESO_CLASSES"] == eso_constants.LIST_ESO_CLASSES
        assert data["LIST_ESO_DUNGEONS"] == eso_constants.LIST_ESO_DUNGEONS
        assert data["LIST_ESO_RAIDS"] == eso_constants.LIST_ESO_RAIDS

    def test_eso_query_get_dungeon_runs(self):
        response = requests.get(constants.FLASK_BACKEND_URL + constants.API_ESO_GET_DUNGEON_RUNS)

        assert response is not None
        assert response.status_code == 200

        data = response.json()['queryResult'][0]
        assert type(data['id']) == int
        assert type(data['dungeon_name']) == str
        assert type(data['player_count']) == int
        assert type(data['time_needed']) == int
        assert type(data['hardmode']) == bool
        assert type(data['flawless']) == bool
        assert type(data['wipes']) == int
        assert type(data['class_one']) == str
        assert type(data['class_two']) == str
        assert type(data['class_three']) == str
        assert type(data['class_four']) == str

    def test_eso_query_post_dungeon_run(self):
        db_cursor = QueryEsoTable()

        # check current highest run id:
        last_added_run_id = db_cursor.eso_get_id_of_last_added_record()

        payload = {
            'submitDungeonRunFormData':
                {
                    'formClassFour': eso_constants.CLASS_DRAGONKNIGHT,
                    'formClassOne': eso_constants.CLASS_NECRO,
                    'formClassThree': eso_constants.CLASS_WARDEN,
                    'formClassTwo': eso_constants.CLASS_SORCERER,
                    'formDungeonName': eso_constants.DUNGEON_ARX_CORINIUM,
                    'formFlawless': "no",
                    'formHardmode': "no",
                    'formPlayerCount': 4,
                    'formTimeNeeded': 20,
                    'formWipes': 0
                }
        }
        response = requests.post(constants.FLASK_BACKEND_URL + constants.API_ESO_POST_DUNGEON_RUN, json=payload)

        assert response is not None
        assert response.status_code == 200

        # now a new id must have been created (autoincrement of DB)
        new_last_added_run_id = db_cursor.eso_get_id_of_last_added_record()

        assert new_last_added_run_id != last_added_run_id

        # delete added run
        status = db_cursor.eso_delete_last_added_record_query()
        assert status == 200
