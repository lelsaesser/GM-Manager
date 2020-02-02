# Flask backend server
FLASK_BACKEND_URL = "http://localhost:5000"

# Api endpoints
# Health check
API_HEALTH_CHECK = "/api/healthcheck"

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
API_ESO_POST_DUNGEON_RUN = "/api/eso/submit/dungeon"
API_ESO_DELETE_DUNGEON_RUN = "/api/eso/delete/dungeon"

API_ESO_GET_RAID_RUNS = "/api/eso/raids"
API_ESO_POST_RAID_RUN = "/api/eso/submit/raid"
API_ESO_DELETE_RAID_RUN = "/api/eso/delete/raid"

# Misc
API_MISC_GET_CONSTANTS = "/api/misc/constants"
API_MISC_BRAINSTORM_GET_EXERCISE_LIST = "/api/misc/brainstorm/exercise"

# Errors
# General
ERROR_GEN_DB_NOT_REACHABLE = "Error: could not query database"
ERROR_GEN_DB_TABLE_EMPTY = "Error: could not fetch data from DB - table empty?"

# Survrim
ERROR_SURVRIM_LOCATION_MISSING = "Error: invalid location name."

# Messages
# Health check success
MSG_HEALTH_CHECK_SUCCESS = "Api is healthy and running!"
MSG_HEALTH_CHECK_FAILURE = "Health check failed - bad payload"
MSG_QUERY_EMPTY_TABLE = 'No data to fetch, table is empty'

# Dict keys
KEY_HEALTH_CHECK_RESPONSE = 'health_check_response'
KEY_HEALTH_CHECK_PAYLOAD = 'health_check_payload'
KEY_RECEIVED_PAYLOAD = 'received_payload'
KEY_STATUS = 'status'
KEY_MESSAGE = 'message'
KEY_INFO = 'info'
KEY_QUERY_RESULT = 'queryResult'

# Response codes
RESP_OK = 200
RESP_BAD_REQUEST = 400
RESP_INTERNAL_SERVER_ERROR = 500
RESP_RESOURCE_NOT_FOUND = 404


