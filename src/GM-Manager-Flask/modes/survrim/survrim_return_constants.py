from modes.survrim import constants as c


class SurvrimReturnConstants:

    @staticmethod
    def survrim_get_constants():
        """
        Return important survrim/survrun constants as Json structure.
        Used to expose these constants to frontend and other services.
        :return: Json structure containing constants
        """
        target_location_list_sorted = sorted(c.LIST_SURVRUN_TARGET_LOCATIONS)
        json_model = {
            c.SR_KEY_SURVRIM_CONSTANTS: [
                {
                    c.SR_KEY_LIST_SURVRUN_TARGET_LOCATIONS: target_location_list_sorted,
                    c.SR_KEY_LIST_SURVRIM_SKILLS: c.LIST_SURVRIM_SKILLS,
                    c.SR_KEY_LIST_SURVRIM_CLASSES: c.LIST_SURVRIM_CLASSES,
                    c.SR_KEY_LIST_SURVRUN_DIFFICULTIES: c.LIST_SURVRUN_DIFFICULTIES
                }
            ]
        }

        return json_model
