import constants
from database.query_eso_raid_table import QueryEsoRaidTable
from modes.eso import constants as eso_constants
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

        data = response.json()['queryResult'][0]
        assert type(data['id']) == int
        assert data['raid_name'] in eso_constants.LIST_ESO_RAIDS
        assert type(data['player_count']) == int
        assert type(data['time_needed']) == int
        assert type(data['hardmode']) == bool
        assert type(data['flawless']) == bool
        assert type(data['wipes']) == int
        assert data['class_one'] in eso_constants.LIST_ESO_CLASSES
        assert data['class_two'] in eso_constants.LIST_ESO_CLASSES
        assert data['class_three'] in eso_constants.LIST_ESO_CLASSES
        assert data['class_four'] in eso_constants.LIST_ESO_CLASSES
        assert data['class_five'] in eso_constants.LIST_ESO_CLASSES
        assert data['class_six'] in eso_constants.LIST_ESO_CLASSES
        assert data['class_seven'] in eso_constants.LIST_ESO_CLASSES
        assert data['class_eight'] in eso_constants.LIST_ESO_CLASSES
        assert data['class_nine'] in eso_constants.LIST_ESO_CLASSES
        assert data['class_ten'] in eso_constants.LIST_ESO_CLASSES
        assert data['class_eleven'] in eso_constants.LIST_ESO_CLASSES
        assert data['class_twelve'] in eso_constants.LIST_ESO_CLASSES

    def test_eso_query_post_raid_run(self):
        db_cursor = QueryEsoRaidTable()

        # check current highest run id:
        last_added_run_id = db_cursor.eso_get_id_of_last_added_record()

        payload = {
            'submitRaidRunFormData':
                {
                    'formRaidName': eso_constants.RAID_SUNSPIRE,
                    'formPlayerCount': 12,
                    'formTimeNeeded': 60,
                    'formHardmode': "yes",
                    'formFlawless': "yes",
                    'formWipes': 0,
                    'formClassOne': eso_constants.CLASS_DRAGONKNIGHT,
                    'formClassTwo': eso_constants.CLASS_DRAGONKNIGHT,
                    'formClassThree': eso_constants.CLASS_DRAGONKNIGHT,
                    'formClassFour': eso_constants.CLASS_SORCERER,
                    'formClassFive': eso_constants.CLASS_SORCERER,
                    'formClassSix': eso_constants.CLASS_SORCERER,
                    'formClassSeven': eso_constants.CLASS_NIGHTBLADE,
                    'formClassEight': eso_constants.CLASS_NIGHTBLADE,
                    'formClassNine': eso_constants.CLASS_NIGHTBLADE,
                    'formClassTen': eso_constants.CLASS_TEMPLAR,
                    'formClassEleven': eso_constants.CLASS_TEMPLAR,
                    'formClassTwelve': eso_constants.CLASS_TEMPLAR
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
