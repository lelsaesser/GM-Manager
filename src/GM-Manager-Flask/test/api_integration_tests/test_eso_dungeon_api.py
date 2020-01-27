import constants
from database.query_eso_dungeon_table import QueryEsoDungeonTable
from modes.eso import constants as eso_constants
from utils.api_helper import GmManagerApiHelper as h


class TestEsoDungeonApi:

    def test_eso_get_constants(self):
        response = h.api_get_request(constants.FLASK_BACKEND_URL + constants.API_ESO_GET_CONSTANTS)

        assert response is not None
        assert response.status_code == 200

        data = response.json()['eso_constants'][0]
        assert data["LIST_ESO_CLASSES"] == eso_constants.LIST_ESO_CLASSES
        assert data["LIST_ESO_DUNGEONS"] == eso_constants.LIST_ESO_DUNGEONS
        assert data["LIST_ESO_RAIDS"] == eso_constants.LIST_ESO_RAIDS

    def test_eso_query_get_dungeon_runs(self):
        """
        Test eso get dungeon runs endpoint
        Note that this test will always fail if the database is empty!
        """
        response = h.api_get_request(constants.FLASK_BACKEND_URL + constants.API_ESO_GET_DUNGEON_RUNS)

        assert response is not None
        assert response.status_code == 200

        data = response.json()['queryResult'][0]
        assert type(data['id']) == int
        assert data['dungeon_name'] in eso_constants.LIST_ESO_DUNGEONS
        assert type(data['player_count']) == int
        assert type(data['time_needed']) == int
        assert type(data['hardmode']) == bool
        assert type(data['flawless']) == bool
        assert type(data['wipes']) == int
        assert data['class_one'] in eso_constants.LIST_ESO_CLASSES
        assert data['class_two'] in eso_constants.LIST_ESO_CLASSES
        assert data['class_three'] in eso_constants.LIST_ESO_CLASSES
        assert data['class_four'] in eso_constants.LIST_ESO_CLASSES

    def test_eso_query_post_dungeon_run(self):
        db_cursor = QueryEsoDungeonTable()

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
        response = h.api_post_request(constants.FLASK_BACKEND_URL + constants.API_ESO_POST_DUNGEON_RUN, payload)

        assert response is not None
        assert response.status_code == 200

        # now a new id must have been created (autoincrement of DB)
        new_last_added_run_id = db_cursor.eso_get_id_of_last_added_record()

        assert new_last_added_run_id != last_added_run_id

        # delete added run
        status = db_cursor.eso_delete_last_added_record_query()
        assert status == 200
