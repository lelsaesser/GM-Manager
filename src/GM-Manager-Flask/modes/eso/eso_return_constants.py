from modes.eso import constants as c


class EsoReturnConstants:

    @staticmethod
    def eso_get_constants():
        """
        expose eso constants to frontend
        :return: Json structure containing constants
        """
        json_model = {
            c.ESO_KEY_ESO_CONSTANTS: [
                {
                    c.ESO_KEY_LIST_ESO_CLASSES: c.LIST_ESO_CLASSES,
                    c.ESO_KEY_LIST_ESO_DUNGEONS: c.LIST_ESO_DUNGEONS,
                    c.ESO_KEY_LIST_ESO_RAIDS: c.LIST_ESO_RAIDS
                }
            ]
        }

        return json_model
