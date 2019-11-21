# Flask backend server
FLASK_BACKEND_URL = "http://localhost:5000"

# Api endpoints
# Survrim/Survrun
API_SURVRIM_GET_CLASS_DATA = "/api/survrim/class"
API_SURVRUN_GET_ALL_DB_RUN_DATA = "/api/survrun/getalldata"
API_SURVRUN_POST_RUN = "/api/survrun/submit-run"
API_SURVRUN_GET_CONSTANTS = "/api/survrun/constants"
API_SURVRUN_GET_TARGET_LOCATION = "/api/survrun/targets"
API_SURVRUN_DELETE_RUN = "/api/survrun/delete"
API_SURVRUN_GET_STATISTICS = "/api/survrun/statistics"

# Stronghold
API_STRONGHOLD_GET_AI_BATTLE = "/api/shc"

# Eso
API_ESO_GET_CONSTANTS = "/api/eso/constants"
API_ESO_GET_DUNGEON_RUNS = "/api/eso/dungeons"
API_ESO_POST_DUNGEON_RUN = "/api/eso/submit-run"

# Errors
# General
ERROR_GEN_DB_NOT_REACHABLE = "Error: could not query database"
ERROR_GEN_DB_TABLE_EMPTY = "Error: could not fetch data from DB - table empty?"

# Survrim
ERROR_SURVRIM_LOCATION_MISSING = "Error: invalid location name."