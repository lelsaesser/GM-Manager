from sqlalchemy import create_engine, desc
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from database import constants as c_db
from database.table_schemas import ShcRankingTable
from modes.stronghold import constants as c


class QueryShcRankingTable:

    def __init__(self):
        self._db_string = c_db.POSTGRE_FULL_DB_STRING
        self._db = _db = create_engine(self._db_string)
        self._session = sessionmaker(self._db)

    def fetch_all_ranking_data(self):
        """
        Fetch and return ranking data for each AI as list
        :return: list containing fetched ranking data
        """
        sess = self._session()
        data = sess.query(ShcRankingTable).order_by(desc(ShcRankingTable.rating))

        json = []
        for row in data:
            json.append(
                {
                    c.SHC_KEY_AI_NAME: row.ai_name,
                    c.SHC_KEY_RATING: row.rating,
                    c.SHC_KEY_PLAYED_GAMES: row.played_games
                }
            )

        return json

    def insert_update_ranking(self, ai_name: str, rating_update: int) -> int:
        """
        Update the rating of an ai or insert it if not present
        :return: 200 on success, 400 if bad request, 500 on internal server error
        """
        if ai_name not in c.AI_CHAR_LIST:
            return 400
        if rating_update is None:
            return 400
        if rating_update == 0:
            return 200

        sess = self._session()
        try:
            # get current rating for requested ai and update it
            ai = sess.query(ShcRankingTable).filter(ShcRankingTable.ai_name == ai_name).one()
            ai.rating += rating_update
            ai.played_games += 1
            sess.commit()
            return 200

        except Exception:
            # create if not present
            try:
                query = ShcRankingTable(ai_name=ai_name, rating=rating_update, played_games=1)
                sess.add(query)
                sess.commit()
                return 200
            except IntegrityError:
                return 500

    def edit_played_games(self, ai_name: str, played_games_edit: int) -> int:
        """
        Edit played games property of requested AI. Useful for tests which call insert_update_ranking() and therefore
        increase the played games count of AIs
        :return: 200 on success, 400 on bad request, 500 on internal server error
        """
        sess = self._session()
        try:
            ai = sess.query(ShcRankingTable).filter(ShcRankingTable.ai_name == ai_name).one()
            ai.played_games += played_games_edit
            if ai.played_games < 0:
                ai.played_games = 0
            sess.commit()
            return 200
        except Exception:
            return 500
