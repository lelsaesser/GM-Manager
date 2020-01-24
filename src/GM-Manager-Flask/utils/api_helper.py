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
        :raises: Exception if the request fails
        """
        try:
            response = requests.get(target_url)
            return response
        except Exception:
            print("GET request failed. Invalid target url?")
            raise Exception

    @staticmethod
    def api_post_request(target_url: str, payload, payload_is_json=True):
        """
        send a POST request to the target location
        :param target_url: target url string
        :param payload: payload to send
        :param payload_is_json: boolean, True if payload is JSON otherwise False
        :return: full unedited response of the request
        :raises Exception: if the request fails
        """
        try:
            if payload_is_json:
                response = requests.post(target_url, json=payload)
            else:
                response = requests.post(target_url, data=payload)
            return response
        except Exception:
            print("POST request failed. Invalid target url or payload?")
            raise Exception
