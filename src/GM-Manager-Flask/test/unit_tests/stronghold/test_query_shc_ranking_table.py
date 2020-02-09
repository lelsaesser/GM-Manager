from database.query_shc_ranking_table import QueryShcRankingTable
from modes.stronghold import constants as c


class TestShcRankingTable:

    def test_fetch_all_ranking_data(self):
        cursor = QueryShcRankingTable()
        data = cursor.fetch_all_ranking_data()

        assert data is not None, "Fetch failed, is the SHC ranking table empty?"
        for row in data:
            assert row[c.SHC_KEY_AI_NAME] in c.AI_CHAR_LIST
            assert row[c.SHC_KEY_RATING] is not None
            assert row[c.SHC_KEY_PLAYED_GAMES] >= 0

    def test_insert_update_ranking(self):
        cursor = QueryShcRankingTable()

        assert cursor.insert_update_ranking("abc", 1) == 400
        assert cursor.insert_update_ranking(c.AI_ABBOT, None) == 400
        assert cursor.insert_update_ranking(c.AI_ABBOT, 0) == 200
        assert cursor.insert_update_ranking(c.AI_ABBOT, c.RANKING_UPDATE_ON_WIN) == 200
        assert cursor.insert_update_ranking(c.AI_ABBOT, c.RANKING_UPDATE_ON_LOSE) == 200
        # remove the two additional added played games from above two lines
        assert cursor.edit_played_games(c.AI_ABBOT, -2) == 200
