from database.query_eso_raid_table import QueryEsoRaidTable
from modes.eso import constants as eso_constants


class TestQueryEsoRaidTable:

    def test_eso_insert_raid_query(self):
        db_cursor = QueryEsoRaidTable()
        status = db_cursor.eso_insert_raid_run_query(raid_name=eso_constants.RAID_CLOUDREST, player_count=12,
                                                     time_needed=50, wipes=1, hardmode="yes", flawless="no",
                                                     class_one=eso_constants.CLASS_DRAGONKNIGHT,
                                                     class_two=eso_constants.CLASS_DRAGONKNIGHT,
                                                     class_three=eso_constants.CLASS_DRAGONKNIGHT,
                                                     class_four=eso_constants.CLASS_SORCERER,
                                                     class_five=eso_constants.CLASS_SORCERER,
                                                     class_six=eso_constants.CLASS_SORCERER,
                                                     class_seven=eso_constants.CLASS_NIGHTBLADE,
                                                     class_eight=eso_constants.CLASS_NIGHTBLADE,
                                                     class_nine=eso_constants.CLASS_NIGHTBLADE,
                                                     class_ten=eso_constants.CLASS_TEMPLAR,
                                                     class_eleven=eso_constants.CLASS_TEMPLAR,
                                                     class_twelve=eso_constants.CLASS_TEMPLAR,
                                                     num_tanks=2,
                                                     num_dps=7,
                                                     num_heals=3,
                                                     total_party_dps=750000,
                                                     total_party_hps=120000)

        assert status == 200

        # remove the created table record
        status = db_cursor.eso_delete_last_added_record_query()
        assert status == 200

    def test_eso_select_raid_runs_query(self):
        db_cursor = QueryEsoRaidTable()
        data = db_cursor.eso_select_raid_runs_query()

        assert data is not None

    def test_eso_delete_raid_run_by_id(self):
        db_cursor = QueryEsoRaidTable()
        status = db_cursor.eso_insert_raid_run_query(raid_name=eso_constants.RAID_CLOUDREST, player_count=12,
                                                     time_needed=50, wipes=1, hardmode="yes", flawless="no",
                                                     class_one=eso_constants.CLASS_DRAGONKNIGHT,
                                                     class_two=eso_constants.CLASS_DRAGONKNIGHT,
                                                     class_three=eso_constants.CLASS_DRAGONKNIGHT,
                                                     class_four=eso_constants.CLASS_SORCERER,
                                                     class_five=eso_constants.CLASS_SORCERER,
                                                     class_six=eso_constants.CLASS_SORCERER,
                                                     class_seven=eso_constants.CLASS_NIGHTBLADE,
                                                     class_eight=eso_constants.CLASS_NIGHTBLADE,
                                                     class_nine=eso_constants.CLASS_NIGHTBLADE,
                                                     class_ten=eso_constants.CLASS_TEMPLAR,
                                                     class_eleven=eso_constants.CLASS_TEMPLAR,
                                                     class_twelve=eso_constants.CLASS_TEMPLAR,
                                                     num_tanks=2,
                                                     num_dps=7,
                                                     num_heals=3,
                                                     total_party_dps=750000,
                                                     total_party_hps=120000)

        assert status == 200

        last_id = db_cursor.eso_get_id_of_last_added_record()
        assert last_id > -1

        status = db_cursor.eso_delete_raid_run_by_id(last_id)
        assert  status == 200
