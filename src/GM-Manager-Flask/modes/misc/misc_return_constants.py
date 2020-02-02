from modes.misc import constants as c


class MiscReturnConstants:

    @staticmethod
    def misc_get_constants():
        """
        expose misc constants to frontend
        :return: Json structure containing constants
        """
        json_model = {
            c.MISC_KEY_MISC_CONSTANTS: [
                {
                    c.MISC_KEY_LIST_MATH_SYMBOLS: c.LIST_MATH_SYMBOLS,
                    c.MISC_KEY_LIST_DIFFICULTIES: c.LIST_DIFFICULTIES
                }
            ]
        }

        return json_model
