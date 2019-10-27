# Postgre connection data
POSTGRE_HOST = '127.0.0.1'
POSTGRE_PORT = '5432'
POSTGRE_USER = 'postgres'
POSTGRE_DB = 'gm-manager-db'
POSTGRE_PW = 'root'

# Postgre table names
TABLE_SURVRUN_RUNS = "survrun_runs"

# Error messages
BAD_REQUEST_INVALID_CLASS_NAME = "Bad request: not a valid class name"
BAD_REQUEST_INVALID_LOCATION_NAME = "Bad request: one or more unvalid target location names"
BAD_REQUEST_INVALID_ATTRIBUTE_COMPLETED = "Bad request: attribute completed must be either \"yes\" or \"no\""
BAD_REQUEST_TARGET_LOCATIONS_EQUAL = "Bad request: target locations cannot be equal"
BAD_REQUEST_DUPLICATE_PRIMARY_KEY = "Bad request: Primary key already exists in table"
BAD_REQUEST_TABLE_IS_EMPTY = "Bad request: requested operation could not be executed: target table is empty"
BAD_REQUEST_ID_NOT_FOUND = "Bad request: given PK (id) was not found in this table"

# Success messages
SUCCESS_QUERY_COMPLETED = "query completed"
