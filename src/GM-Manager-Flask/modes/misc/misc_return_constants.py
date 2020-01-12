from modes.misc import constants


class MiscReturnConstants:

    @staticmethod
    def misc_get_constants():
        """
        expose misc constants to frontend
        :return: Json structure containing constants
        """
        json_model = {
            'misc_constants': [
                {
                    'LIST_MATH_SYMBOLS': constants.LIST_MATH_SYMBOLS,
                    'LIST_DIFFICULTIES': constants.LIST_DIFFICULTIES
                }
            ]
        }

        return json_model
