from modes.eso import constants


class EsoReturnConstants:

    @staticmethod
    def eso_get_constants():
        """
        expose eso constants to frontend
        :return: Json structure containing constants
        """
        json_model = {
            'eso_constants': [
                {
                    'LIST_ESO_CLASSES': constants.LIST_ESO_CLASSES,
                    'LIST_ESO_DUNGEONS': constants.LIST_ESO_DUNGEONS,
                    'LIST_ESO_RAIDS': constants.LIST_ESO_RAIDS
                }
            ]
        }

        return json_model
