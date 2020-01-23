// Flask backend url
export const API_URL = 'http://localhost:5000';

// Flask backend api endpoints
// Survrim/Survrun
export const API_SURVRIM_GET_CLASS_DATA = '/api/survrim/class';
export const API_SURVRUN_GET_ALL_DB_RUN_DATA = "/api/survrun/getalldata";
export const API_SURVRUN_POST_RUN = "/api/survrun/submit-run";
export const API_SURVRUN_GET_CONSTANTS = "/api/survrun/constants";
export const API_SURVRUN_GET_TARGET_LOCATION = '/api/survrun/targets';
export const API_SURVRUN_DELETE_RUN = "/api/survrun/delete";
export const API_SURVRUN_GET_STATISTICS = "/api/survrun/statistics";

// Stronghold
export const SHC_API = '/api/shc';

// ESO
export const API_ESO_GET_CONSTANTS = "/api/eso/constants";
export const API_ESO_GET_DUNGEON_RUNS = "/api/eso/dungeons";
export const API_ESO_POST_DUNGEON_RUN = "/api/eso/submit/dungeon";
export const API_ESO_DELETE_DUNGEON_RUN = "/api/eso/delete/dungeon";

export const API_ESO_GET_RAID_RUNS = "/api/eso/raids"
export const API_ESO_POST_RAID_RUN = "/api/eso/submit/raid"
export const API_ESO_DELETE_RAID_RUN = "/api/eso/delete/raid"

// Misc
export const API_MISC_GET_CONSTANTS = "/api/misc/constants"
export const API_MISC_BRAINSTORM_GET_EXERCISE_LIST = "/api/misc/brainstorm/exercise"
