from database.query_eso_dungeon_table import QueryEsoTable
from modes.eso import constants as eso_constants
from database import constants as db_constants


class TestQueryEsoTable:

    def test_eso_insert_query(self):
        db_cursor = QueryEsoTable()
        status = db_cursor.eso_insert_dungeon_run_query(dungeon_name=eso_constants.DUNGEON_SPINDLECLUTCH_I,
                                                        player_count=4, time_needed=30, hardmode="yes", flawless="no",
                                                        wipes=1, class_one=eso_constants.CLASS_DRAGONKNIGHT,
                                                        class_two=eso_constants.CLASS_NIGHTBLADE,
                                                        class_three=eso_constants.CLASS_SORCERER,
                                                        class_four=eso_constants.CLASS_TEMPLAR)

        assert status == 200

        # remove the created table record
        status = db_cursor.eso_delete_last_added_record_query()
        assert status == 200

    def test_eso_select_query(self):
        db_cursor = QueryEsoTable()
        data = db_cursor.eso_select_dungeon_runs_query()

        assert data is not None

    def test_eso_delete_query(self):
        db_cursor = QueryEsoTable()
        status = db_cursor.eso_insert_dungeon_run_query(dungeon_name=eso_constants.DUNGEON_SPINDLECLUTCH_I,
                                                        player_count=4, time_needed=30, hardmode="yes", flawless="no",
                                                        wipes=1, class_one=eso_constants.CLASS_DRAGONKNIGHT,
                                                        class_two=eso_constants.CLASS_NIGHTBLADE,
                                                        class_three=eso_constants.CLASS_SORCERER,
                                                        class_four=eso_constants.CLASS_TEMPLAR)

        last_id = db_cursor.eso_get_id_of_last_added_record()
        assert last_id > -1

        status = db_cursor.eso_delete_dungeon_run_by_id(last_id)
        assert status == 200
