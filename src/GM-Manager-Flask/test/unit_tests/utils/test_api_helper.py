from utils.api_helper import GmManagerApiHelper as h
import constants as c


class TestGmManagerApiHelper():

    def test_api_get_request(self):
        resp = h.api_get_request(c.FLASK_BACKEND_URL + c.API_HEALTH_CHECK)
        assert resp is not None
        assert resp.status_code == 200

        msg = resp.json()['health_check_response']
        assert msg['status'] == 200
        assert msg['message'] == c.MSG_HEALTH_CHECK_SUCCESS

    def test_api_post_request(self):
        test_json_payload = {
            'health_check_payload': {
                'test1': 123,
                'test2': "abc"
            }
        }
        resp = h.api_post_request(c.FLASK_BACKEND_URL + c.API_HEALTH_CHECK, test_json_payload)
        assert resp is not None
        assert resp.status_code == 200

        msg = resp.json()['health_check_response']
        assert msg['status'] == 200
        assert msg['message'] == c.MSG_HEALTH_CHECK_SUCCESS
        assert msg['received_payload'] == test_json_payload
