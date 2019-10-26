from typing import List

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from database import constants as db_constants
from database.table_schemas import SurvrunTable
from modes.survrim import constants as survrim_constants


class SurvrunTableQuerys:

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
            msg = "Bad request:" + player_class + " is not a valid class name"
            return 400, msg
        elif target_a not in survrim_constants.LIST_SURVRUN_TARGET_LOCATIONS \
                or target_b not in survrim_constants.LIST_SURVRUN_TARGET_LOCATIONS:
            msg = "Bad request:" + target_a + target_b + ": one or more are no valid target location names"
            return 400, msg
        elif completed is not "yes" and completed is not "no":
            msg = "Bad request: completed must be either \"yes\" or \"no\""
            return 400, msg
        elif target_a == target_b:
            msg = "Bad request: target locations cannot be equal"
            return 400, msg

        run_query = SurvrunTable(player_class=player_class, target_a=target_a, target_b=target_b, timebox=timebox,
                                 completed=completed, time_needed=time_needed, r_count=r_count)

        sess = self._session()
        try:
            sess.add(run_query)
            sess.commit()
            msg = "query completed"
            return 200, msg
        except IntegrityError:  # thrown if duplicate PK (id)
            msg = "PK already exists, skipping"
            return 400, msg

    def survrun_select_query(self) -> List[List]:
        """
        Return all rows from survrun_runs table
        :return:
        """
        sess = self._session()
        data = sess.query(SurvrunTable)

        return data
