import constants
from database.query_eso_raid_table import QueryEsoRaidTable
from modes.eso import constants as c
from utils.api_helper import GmManagerApiHelper as h


class TestEsoRaidApi:

    def test_eso_query_get_raid_runs(self):
        """
        Test eso get raid runs endpoint
        Note that this test will always fail if the database is empty!
        """
        response = h.api_get_request(constants.FLASK_BACKEND_URL + constants.API_ESO_GET_RAID_RUNS)

        assert response is not None
        assert response.status_code == 200

        data = response.json()[c.ESO_KEY_QUERY_RESULT][0]
        assert type(data[c.ESO_KEY_ID]) == int
        assert data[c.ESO_KEY_RAID_NAME] in c.LIST_ESO_RAIDS
        assert type(data[c.ESO_KEY_PLAYER_COUNT]) == int
        assert type(data[c.ESO_KEY_TIME_NEEDED]) == int
        assert type(data[c.ESO_KEY_HARDMODE]) == bool
        assert type(data[c.ESO_KEY_FLAWLESS]) == bool
        assert type(data[c.ESO_KEY_WIPES]) == int
        assert data[c.ESO_KEY_CLASS_ONE] in c.LIST_ESO_CLASSES
        assert data[c.ESO_KEY_CLASS_TWO] in c.LIST_ESO_CLASSES
        assert data[c.ESO_KEY_CLASS_THREE] in c.LIST_ESO_CLASSES
        assert data[c.ESO_KEY_CLASS_FOUR] in c.LIST_ESO_CLASSES
        assert data[c.ESO_KEY_CLASS_FIVE] in c.LIST_ESO_CLASSES
        assert data[c.ESO_KEY_CLASS_SIX] in c.LIST_ESO_CLASSES
        assert data[c.ESO_KEY_CLASS_SEVEN] in c.LIST_ESO_CLASSES
        assert data[c.ESO_KEY_CLASS_EIGHT] in c.LIST_ESO_CLASSES
        assert data[c.ESO_KEY_CLASS_NINE] in c.LIST_ESO_CLASSES
        assert data[c.ESO_KEY_CLASS_TEN] in c.LIST_ESO_CLASSES
        assert data[c.ESO_KEY_CLASS_ELEVEN] in c.LIST_ESO_CLASSES
        assert data[c.ESO_KEY_CLASS_TWELVE] in c.LIST_ESO_CLASSES
        assert type(data[c.ESO_KEY_NUM_TANKS]) == int
        assert type(data[c.ESO_KEY_NUM_DPS]) == int
        assert type(data[c.ESO_KEY_NUM_HEALS]) == int
        assert type(data[c.ESO_KEY_TOTAL_PARTY_DPS]) == int
        assert type(data[c.ESO_KEY_TOTAL_PARTY_HPS]) == int

    def test_eso_query_post_raid_run(self):
        db_cursor = QueryEsoRaidTable()

        # check current highest run id:
        last_added_run_id = db_cursor.eso_get_id_of_last_added_record()

        payload = {
            c.ESO_FORM_KEY_RAID_RUN_FORM_DATA:
                {
                    c.ESO_FORM_KEY_RAID_NAME: c.RAID_SUNSPIRE,
                    c.ESO_FORM_KEY_PLAYER_COUNT: 12,
                    c.ESO_FORM_KEY_TIME_NEEDED: 60,
                    c.ESO_FORM_KEY_HARDMODE: c.ESO_YES,
                    c.ESO_FORM_KEY_FLAWLESS: c.ESO_NO,
                    c.ESO_FORM_KEY_WIPES: 0,
                    c.ESO_FORM_KEY_CLASS_ONE: c.CLASS_DRAGONKNIGHT,
                    c.ESO_FORM_KEY_CLASS_TWO: c.CLASS_DRAGONKNIGHT,
                    c.ESO_FORM_KEY_CLASS_THREE: c.CLASS_DRAGONKNIGHT,
                    c.ESO_FORM_KEY_CLASS_FOUR: c.CLASS_SORCERER,
                    c.ESO_FORM_KEY_CLASS_FIVE: c.CLASS_SORCERER,
                    c.ESO_FORM_KEY_CLASS_SIX: c.CLASS_SORCERER,
                    c.ESO_FORM_KEY_CLASS_SEVEN: c.CLASS_NIGHTBLADE,
                    c.ESO_FORM_KEY_CLASS_EIGHT: c.CLASS_NIGHTBLADE,
                    c.ESO_FORM_KEY_CLASS_NINE: c.CLASS_NIGHTBLADE,
                    c.ESO_FORM_KEY_CLASS_TEN: c.CLASS_TEMPLAR,
                    c.ESO_FORM_KEY_CLASS_ELEVEN: c.CLASS_TEMPLAR,
                    c.ESO_FORM_KEY_CLASS_TWELVE: c.CLASS_TEMPLAR,
                    c.ESO_FORM_KEY_NUM_TANKS: 2,
                    c.ESO_FORM_KEY_NUM_DPS: 7,
                    c.ESO_FORM_KEY_NUM_HEALS: 3,
                    c.ESO_FORM_KEY_TOTAL_PARTY_DPS: 750000,
                    c.ESO_FORM_KEY_TOTAL_PARTY_HPS: 120000
                }
        }
        response = h.api_post_request(constants.FLASK_BACKEND_URL + constants.API_ESO_POST_RAID_RUN, payload)

        assert response is not None
        assert response.status_code == 200

        # now a new id must have been created (autoincrement of DB)
        new_last_added_run_id = db_cursor.eso_get_id_of_last_added_record()

        assert new_last_added_run_id != last_added_run_id

        # delete added run
        status = db_cursor.eso_delete_last_added_record_query()
        assert status == 200
