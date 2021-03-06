import random

from ..stronghold import constants as c


class StrongholdAiPicker:

    @staticmethod
    def pick_random_ai(num_of_ai: int) -> list:
        """
        Calculate random AI characters.
        :param num_of_ai: number of AIs to choose. Must be int 2-8 (both included)
        :returns string list containing the full name of each chosen ai
        :raises ValueError, if the argument is not an int in range 2-8 (both included)
        """
        if num_of_ai < 2:
            raise ValueError
        if num_of_ai > 8:
            raise ValueError
        ai_list = []
        while len(ai_list) < num_of_ai:
            ai_idx = random.randint(0, len(c.AI_CHAR_LIST) - 1)
            if c.AI_CHAR_LIST[ai_idx] not in ai_list:
                ai_list.append(c.AI_CHAR_LIST[ai_idx])

        return ai_list

    @staticmethod
    def format_ai_list(ai_list: list) -> str:
        """
        Format the result list of pick_random_ai() in a handy string for display.
        If a uneven number of Ais is chosen, the first group will always play in disadvantage as of now.
        (A 5-man game will be turned in a 2 vs. 3 for instance)
        This makes sure that the player (who is always in team one) will be in disadvantage.
        :param ai_list: String list as created by pick_random_ai()
        :return: Single formatted string
        :raises: ValueError, if an empty list is provided or the list contains non-string values
        """
        if not ai_list:
            raise ValueError
        half = len(ai_list) // 2
        result_str = ""
        for i in range(half):
            if type(ai_list[i]) is not str:
                raise ValueError
            result_str += ai_list[i]
            if i is not half - 1:
                result_str += " | "
        result_str += " vs. "
        for i in range(len(ai_list) - half):
            if type(ai_list[i + half]) is not str:
                raise ValueError
            result_str += ai_list[i + half]
            if i is not len(ai_list) - half - 1:
                result_str += " | "

        return result_str

    @staticmethod
    def split_ai_in_teams(ai_list):
        """
        Split a list of ais in two teams
        :param ai_list: list containing string names of involved ais
        :return: list containing two string lists, representing both teams
        """
        if not ai_list:
            raise ValueError
        if len(ai_list) == 1:
            raise Exception(c.ERROR_NOT_ENOUGH_AIS)

        half = len(ai_list) // 2
        team_a = ai_list[:half]
        team_b = ai_list[half:]

        return [team_a, team_b]
