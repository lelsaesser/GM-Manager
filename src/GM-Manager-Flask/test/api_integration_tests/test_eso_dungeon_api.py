import constants
from database.query_eso_dungeon_table import QueryEsoDungeonTable
from modes.eso import constants as c
from utils.api_helper import GmManagerApiHelper as h


class TestEsoDungeonApi:

    def test_eso_get_constants(self):
        response = h.api_get_request(constants.FLASK_BACKEND_URL + constants.API_ESO_GET_CONSTANTS)

        assert response is not None
        assert response.status_code == 200

        data = response.json()[c.ESO_KEY_ESO_CONSTANTS][0]
        assert data[c.ESO_KEY_LIST_ESO_CLASSES] == c.LIST_ESO_CLASSES
        assert data[c.ESO_KEY_LIST_ESO_DUNGEONS] == c.LIST_ESO_DUNGEONS
        assert data[c.ESO_KEY_LIST_ESO_RAIDS] == c.LIST_ESO_RAIDS

    def test_eso_query_get_dungeon_runs(self):
        """
        Test eso get dungeon runs endpoint
        Note that this test will always fail if the database is empty!
        """
        response = h.api_get_request(constants.FLASK_BACKEND_URL + constants.API_ESO_GET_DUNGEON_RUNS)

        assert response is not None
        assert response.status_code == 200

        data = response.json()[c.ESO_KEY_QUERY_RESULT][0]
        assert type(data[c.ESO_KEY_ID]) == int
        assert data[c.ESO_KEY_DUNGEON_NAME] in c.LIST_ESO_DUNGEONS
        assert type(data[c.ESO_KEY_PLAYER_COUNT]) == int
        assert type(data[c.ESO_KEY_TIME_NEEDED]) == int
        assert type(data[c.ESO_KEY_HARDMODE]) == bool
        assert type(data[c.ESO_KEY_FLAWLESS]) == bool
        assert type(data[c.ESO_KEY_WIPES]) == int
        assert data[c.ESO_KEY_CLASS_ONE] in c.LIST_ESO_CLASSES
        assert data[c.ESO_KEY_CLASS_TWO] in c.LIST_ESO_CLASSES
        assert data[c.ESO_KEY_CLASS_THREE] in c.LIST_ESO_CLASSES
        assert data[c.ESO_KEY_CLASS_FOUR] in c.LIST_ESO_CLASSES

    def test_eso_query_post_dungeon_run(self):
        db_cursor = QueryEsoDungeonTable()

        # check current highest run id:
        last_added_run_id = db_cursor.eso_get_id_of_last_added_record()

        payload = {
            c.ESO_FORM_KEY_SUBMIT_DUNGEON_RUN_DATA:
                {
                    c.ESO_FORM_KEY_CLASS_FOUR: c.CLASS_DRAGONKNIGHT,
                    c.ESO_FORM_KEY_CLASS_ONE: c.CLASS_NECRO,
                    c.ESO_FORM_KEY_CLASS_THREE: c.CLASS_WARDEN,
                    c.ESO_FORM_KEY_CLASS_TWO: c.CLASS_SORCERER,
                    c.ESO_FORM_KEY_DUNGEON_NAME: c.DUNGEON_ARX_CORINIUM,
                    c.ESO_FORM_KEY_FLAWLESS: c.ESO_NO,
                    c.ESO_FORM_KEY_HARDMODE: c.ESO_NO,
                    c.ESO_FORM_KEY_PLAYER_COUNT: 4,
                    c.ESO_FORM_KEY_TIME_NEEDED: 20,
                    c.ESO_FORM_KEY_WIPES: 0
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
