from typing import List

from sqlalchemy import create_engine, desc
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from database import constants as db_constants
from database.table_schemas import SurvrunTable
from modes.survrim import constants as survrim_constants


class QuerySurvrunTable:

    def __init__(self):
        self._db_string = "postgres://" + db_constants.POSTGRE_USER + ":" + db_constants.POSTGRE_PW + "@" + \
                          db_constants.POSTGRE_HOST + ":" + db_constants.POSTGRE_PORT + "/" + db_constants.POSTGRE_DB

        self._db = _db = create_engine(self._db_string)
        self._session = sessionmaker(self._db)

    def survrun_insert_query(self, player_class: str, target_a: str, target_b: str, timebox: int, completed: str,
                             time_needed: int, r_count: int):
        """
        Insert a new run in survrun_runs table
        :param player_class: valid survrun class name
        :param target_a: valid survrun target location
        :param target_b: valid survrun target location
        :param timebox: integer, time in minutes
        :param completed: "yes" or "no"
        :param time_needed: integer, time in minutes
        :param r_count: integer, r_count
        :return: HTTP request status code (int) and string containing detailed explanation
        """
        msg = ""
        if player_class not in survrim_constants.LIST_SURVRIM_CLASSES:
            msg = db_constants.BAD_REQUEST_INVALID_CLASS_NAME
            return 400, msg
        if target_a not in survrim_constants.LIST_SURVRUN_TARGET_LOCATIONS \
                or target_b not in survrim_constants.LIST_SURVRUN_TARGET_LOCATIONS:
            msg = db_constants.BAD_REQUEST_INVALID_LOCATION_NAME
            return 400, msg
        if completed is not "yes" and completed is not "no":
            msg = db_constants.BAD_REQUEST_INVALID_ATTRIBUTE_COMPLETED
            return 400, msg
        if target_a == target_b:
            msg = db_constants.BAD_REQUEST_TARGET_LOCATIONS_EQUAL
            return 400, msg

        run_query = SurvrunTable(player_class=player_class, target_a=target_a, target_b=target_b, timebox=timebox,
                                 completed=completed, time_needed=time_needed, r_count=r_count)

        sess = self._session()
        try:
            sess.add(run_query)
            sess.commit()
            msg = db_constants.SUCCESS_QUERY_COMPLETED
            return 200, msg
        except IntegrityError:  # thrown if duplicate PK (id)
            msg = db_constants.BAD_REQUEST_DUPLICATE_PRIMARY_KEY
            return 400, msg

    def survrun_select_query(self) -> List[List]:
        """
        Return all rows from survrun_runs table
        :return:
        """
        sess = self._session()
        data = sess.query(SurvrunTable)

        return data

    def survrun_delete_last_added_record_query(self):
        """
        Delete the last added table record. This is handy for unit/integration tests that create a record to test
        the insert functionality or for undo/revert functionality in frontend.
        Important: this is id based. The record with the highest id is interpreted as last added record. Only works
        with autoincrement.
        """
        sess = self._session()
        data = sess.query(SurvrunTable).order_by(desc(SurvrunTable.id)).limit(1)

        for row in data:
            sess.delete(row)
            sess.commit()
            return 200, db_constants.SUCCESS_QUERY_COMPLETED
        return 400, db_constants.BAD_REQUEST_TABLE_IS_EMPTY

    def survrun_delete_record_by_id_query(self, run_id):
        sess = self._session()
        row = sess.query(SurvrunTable).filter(SurvrunTable.id == run_id).first()

        if not row:
            return 400, db_constants.BAD_REQUEST_ID_NOT_FOUND

        sess.delete(row)
        sess.commit()
        return 200, db_constants.SUCCESS_QUERY_COMPLETED
