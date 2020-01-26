import requests


class GmManagerApiHelper:
    """
    requests module wrapper
    """

    @staticmethod
    def api_get_request(target_url: str):
        """
        send a GET request to the target location
        :param target_url: target url string
        :return: full unedited response of the request
        """
        response = requests.get(target_url)
        return response

    @staticmethod
    def api_post_request(target_url: str, payload):
        """
        send a POST request to the target location
        :param target_url: target url string
        :param payload: payload to send
        :return: full unedited response of the request
        """
        response = requests.post(target_url, json=payload)
        return response

