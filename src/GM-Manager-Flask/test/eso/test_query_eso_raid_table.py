from database.query_eso_raid_table import QueryEsoRaidTable
from modes.eso import constants as c


class TestQueryEsoRaidTable:

    def test_eso_insert_raid_query(self):
        db_cursor = QueryEsoRaidTable()
        status = db_cursor.eso_insert_raid_run_query(raid_name=c.RAID_CLOUDREST, player_count=12,
                                                     time_needed=50, wipes=1, hardmode=c.ESO_YES, flawless=c.ESO_NO,
                                                     class_one=c.CLASS_DRAGONKNIGHT,
                                                     class_two=c.CLASS_DRAGONKNIGHT,
                                                     class_three=c.CLASS_DRAGONKNIGHT,
                                                     class_four=c.CLASS_SORCERER,
                                                     class_five=c.CLASS_SORCERER,
                                                     class_six=c.CLASS_SORCERER,
                                                     class_seven=c.CLASS_NIGHTBLADE,
                                                     class_eight=c.CLASS_NIGHTBLADE,
                                                     class_nine=c.CLASS_NIGHTBLADE,
                                                     class_ten=c.CLASS_TEMPLAR,
                                                     class_eleven=c.CLASS_TEMPLAR,
                                                     class_twelve=c.CLASS_TEMPLAR,
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
        status = db_cursor.eso_insert_raid_run_query(raid_name=c.RAID_CLOUDREST, player_count=12,
                                                     time_needed=50, wipes=1, hardmode=c.ESO_YES, flawless=c.ESO_NO,
                                                     class_one=c.CLASS_DRAGONKNIGHT,
                                                     class_two=c.CLASS_DRAGONKNIGHT,
                                                     class_three=c.CLASS_DRAGONKNIGHT,
                                                     class_four=c.CLASS_SORCERER,
                                                     class_five=c.CLASS_SORCERER,
                                                     class_six=c.CLASS_SORCERER,
                                                     class_seven=c.CLASS_NIGHTBLADE,
                                                     class_eight=c.CLASS_NIGHTBLADE,
                                                     class_nine=c.CLASS_NIGHTBLADE,
                                                     class_ten=c.CLASS_TEMPLAR,
                                                     class_eleven=c.CLASS_TEMPLAR,
                                                     class_twelve=c.CLASS_TEMPLAR,
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
