from sqlalchemy import create_engine, Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base

from database import constants as c

_db_string = c.POSTGRE_FULL_DB_STRING
_db = create_engine(_db_string)
_base = declarative_base()


class SurvrunTable(_base):
    __tablename__ = c.TABLE_SURVRUN_RUNS

    id = Column(Integer, primary_key=True)
    player_class = Column(String)
    target_a = Column(String)
    target_b = Column(String)
    timebox = Column(Integer)
    completed = Column(String)
    time_needed = Column(Integer)
    r_count = Column(Integer)
    difficulty = Column(String)


class EsoDungeonRunsTable(_base):
    __tablename__ = c.TABLE_ESO_DUNGEON_RUNS

    id = Column(Integer, primary_key=True)
    dungeon_name = Column(String)
    player_count = Column(Integer)
    time_needed = Column(Integer)
    hardmode = Column(Boolean)
    flawless = Column(Boolean)
    wipes = Column(Integer)
    class_one = Column(String)
    class_two = Column(String)
    class_three = Column(String)
    class_four = Column(String)


class EsoRaidRunsTable(_base):
    __tablename__ = c.TABLE_ESO_RAID_RUNS

    id = Column(Integer, primary_key=True)
    raid_name = Column(String)
    player_count = Column(Integer)
    time_needed = Column(Integer)
    hardmode = Column(Boolean)
    flawless = Column(Boolean)
    wipes = Column(Integer)
    class_one = Column(String)
    class_two = Column(String)
    class_three = Column(String)
    class_four = Column(String)
    class_five = Column(String)
    class_six = Column(String)
    class_seven = Column(String)
    class_eight = Column(String)
    class_nine = Column(String)
    class_ten = Column(String)
    class_eleven = Column(String)
    class_twelve = Column(String)
    num_tanks = Column(Integer)
    num_dps = Column(Integer)
    num_heals = Column(Integer)
    total_party_dps = Column(Integer)
    total_party_hps = Column(Integer)


class ShcRankingTable(_base):
    __tablename__ = c.TABLE_SHC_RANKING

    id = Column(Integer, primary_key=True)
    ai_name = Column(String)
    rating = Column(Integer)
    played_games = Column(Integer)


_base.metadata.create_all(_db)


