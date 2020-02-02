from typing import List

from sqlalchemy import create_engine, desc
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from database import constants as c_db
from database.table_schemas import EsoRaidRunsTable
from modes.eso import constants as c_eso


class QueryEsoRaidTable:

    def __init__(self):
        self._db_string = c_db.POSTGRE_FULL_DB_STRING
        self._db = _db = create_engine(self._db_string)
        self._session = sessionmaker(self._db)

    def eso_insert_raid_run_query(self, raid_name: str, player_count: int, time_needed: int, hardmode: str,
                                  flawless: str, wipes: int, class_one: str, class_two: str, class_three: str,
                                  class_four: str, class_five: str, class_six: str, class_seven: str, class_eight: str,
                                  class_nine: str, class_ten: str, class_eleven: str, class_twelve: str,
                                  num_tanks: int, num_dps: int, num_heals: int, total_party_dps: int,
                                  total_party_hps: int) -> int:
        """
        Insert a raid run to the database
        :param total_party_hps: total average party heals per second
        :param total_party_dps: total average party damage per second
        :param num_heals: int, number of healers in party
        :param num_dps: int, number of dps roles in party
        :param num_tanks: int, number of tanks in party
        :param raid_name: valid eso raid (trial) name
        :param player_count: integer 1-12
        :param time_needed: integer representing time in minutes (1-999 allowed)
        :param hardmode: boolean, was hardmode completed?
        :param flawless: boolean, was the raid completed without a single group member death?
        :param wipes: integer, representing wipe count (times full party faints and battle resets)
        :param class_one: valid eso classname
        :param class_two: valid eso classname
        :param class_three: valid eso classname
        :param class_four: valid eso classname
        :param class_five: valid eso classname
        :param class_six: valid eso classname
        :param class_seven: valid eso classname
        :param class_eight: valid eso classname
        :param class_nine: valid eso classname
        :param class_ten: valid eso classname
        :param class_eleven: valid eso classname
        :param class_twelve: valid eso classname
        """
        if raid_name not in c_eso.LIST_ESO_RAIDS:
            return 400
        if player_count < 1 or player_count > 12:
            return 400
        if time_needed < 1 or time_needed > 999:
            return 400
        if hardmode is None or hardmode == c_eso.ESO_NO:
            hardmode = False
        elif hardmode == c_eso.ESO_YES:
            hardmode = True
        else:
            return 400
        if flawless is None or flawless == c_eso.ESO_NO:
            flawless = False
        elif flawless == c_eso.ESO_YES:
            flawless = True
        else:
            return 400
        if wipes < 0 or wipes > 999:
            return 400
        if class_one not in c_eso.LIST_ESO_CLASSES:
            return 400
        if class_two not in c_eso.LIST_ESO_CLASSES:
            return 400
        if class_three not in c_eso.LIST_ESO_CLASSES:
            return 400
        if class_four not in c_eso.LIST_ESO_CLASSES:
            return 400
        if class_five not in c_eso.LIST_ESO_CLASSES:
            return 400
        if class_six not in c_eso.LIST_ESO_CLASSES:
            return 400
        if class_seven not in c_eso.LIST_ESO_CLASSES:
            return 400
        if class_eight not in c_eso.LIST_ESO_CLASSES:
            return 400
        if class_nine not in c_eso.LIST_ESO_CLASSES:
            return 400
        if class_ten not in c_eso.LIST_ESO_CLASSES:
            return 400
        if class_eleven not in c_eso.LIST_ESO_CLASSES:
            return 400
        if class_twelve not in c_eso.LIST_ESO_CLASSES:
            return 400
        if num_tanks < 0 or num_tanks > 12:
            return 400
        if num_dps < 0 or num_dps > 12:
            return 400
        if num_heals < 0 or num_heals > 12:
            return 400
        if total_party_dps < 0 or total_party_dps > 9999999:
            return 400
        if total_party_hps < 0 or total_party_hps > 9999999:
            return 400
        if num_tanks + num_dps + num_heals == 0:
            return 400
        if num_tanks + num_dps + num_heals > 12:
            return 400

        run_query = EsoRaidRunsTable(raid_name=raid_name, player_count=player_count, time_needed=time_needed,
                                     hardmode=hardmode, flawless=flawless, wipes=wipes, class_one=class_one,
                                     class_two=class_two, class_three=class_three, class_four=class_four,
                                     class_five=class_five, class_six=class_six, class_seven=class_seven,
                                     class_eight=class_eight, class_nine=class_nine, class_ten=class_ten,
                                     class_eleven=class_eleven, class_twelve=class_twelve, num_tanks=num_tanks,
                                     num_dps=num_dps, num_heals=num_heals, total_party_dps=total_party_dps,
                                     total_party_hps=total_party_hps)

        sess = self._session()
        try:
            sess.add(run_query)
            sess.commit()
            return 200
        except IntegrityError:
            return 500

    def eso_select_raid_runs_query(self) -> List[List]:
        """
        Return all rows from eso raid runs table
        :return: fetched DB data
        """
        sess = self._session()
        data = sess.query(EsoRaidRunsTable)

        return data

    def eso_delete_raid_run_by_id(self, run_id) -> int:
        """
        Delete the record with the given run_id
        :param run_id: id of the record to delete
        :return: 200 if operation was successful, 400 if requested run_id does not exist
        """
        sess = self._session()
        row = sess.query(EsoRaidRunsTable).filter(EsoRaidRunsTable.id == run_id).first()

        if not row:
            return 400

        sess.delete(row)
        sess.commit()
        return 200

    def eso_delete_last_added_record_query(self) -> int:
        """
        Delete the last added table record. This is handy for unit/integration tests that create a record to test
        the insert functionality or for undo/revert functionality in frontend.
        Important: this is id based. The record with the highest id is interpreted as last added record. Only works
        with autoincrement.
        """
        sess = self._session()
        data = sess.query(EsoRaidRunsTable).order_by(desc(EsoRaidRunsTable.id)).limit(1)

        for row in data:
            sess.delete(row)
            sess.commit()
            return 200
        return 400

    def eso_get_id_of_last_added_record(self):
        """
        Returns the id (int) of the last added record
        Important: expects auto increment of id in database. This just returns the highest id of all rows.
        :return: id of last added record or -1 on failure
        """
        sess = self._session()
        data = sess.query(EsoRaidRunsTable).order_by(desc(EsoRaidRunsTable.id)).limit(1)

        for row in data:
            return row.id
        return -1
