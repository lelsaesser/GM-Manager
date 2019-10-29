from modes.survrim import constants as survrim_constants


# todo add unit test
class SurvrimReturnConstants:

    @staticmethod
    def survrim_get_constants():
        """
        Return important survrim/survrun constants as Json structure.
        Used to expose these constants to frontend and other services.
        :return: Json structure containing constants
        """
        target_location_list_sorted = sorted(survrim_constants.LIST_SURVRUN_TARGET_LOCATIONS)
        json_model = {
            'survrim_constants': [
                {
                    'LIST_SURVRUN_TARGET_LOCATIONS': target_location_list_sorted,
                    'LIST_SURVRIM_SKILLS': survrim_constants.LIST_SURVRIM_SKILLS,
                    'LIST_SURVRIM_CLASSES': survrim_constants.LIST_SURVRIM_CLASSES,
                    'LIST_SURVRUN_DIFFICULTIES': survrim_constants.LIST_SURVRUN_DIFFICULTIES
                }
            ]
        }

        return json_model
