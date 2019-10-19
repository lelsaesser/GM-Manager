from ..stronghold import constants
import random


class StrongholdAiPicker:

    @staticmethod
    def pick_random_ai(num_of_ai: int) -> list:
        """
        Calculate random AI characters.
        @:argument number of AIs to choose. Must be int 2-8 (both included)
        @:returns string list containing the full name of each chosen ai
        @:raises ValueError, if the argument is not an int in range 2-8 (both included)
        """
        if num_of_ai <= 1:
            raise ValueError
        if num_of_ai > 8:
            raise ValueError
        ai_list = []
        while len(ai_list) < num_of_ai:
            ai_idx = random.randint(0, len(constants.AI_CHAR_LIST) - 1)
            if constants.AI_CHAR_LIST[ai_idx] not in ai_list:
                ai_list.append(constants.AI_CHAR_LIST[ai_idx])

        return ai_list
