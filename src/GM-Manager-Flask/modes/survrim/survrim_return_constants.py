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
        json_model = {
            'survrim_constants': [
                {
                    'LIST_SURVRUN_TARGET_LOCATIONS': survrim_constants.LIST_SURVRUN_TARGET_LOCATIONS,
                    'LIST_SURVRIM_SKILLS': survrim_constants.LIST_SURVRIM_SKILLS,
                    'LIST_SURVRIM_CLASSES': survrim_constants.LIST_SURVRIM_CLASSES,
                }
            ]
        }

        return json_model
