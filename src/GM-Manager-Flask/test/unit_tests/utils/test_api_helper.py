import constants as c
from utils.api_helper import GmManagerApiHelper as h


class TestGmManagerApiHelper:

    def test_api_get_request(self):
        resp = h.api_get_request(c.FLASK_BACKEND_URL + c.API_HEALTH_CHECK)
        assert resp is not None
        assert resp.status_code == c.RESP_OK

        msg = resp.json()[c.KEY_HEALTH_CHECK_RESPONSE]
        assert msg[c.KEY_STATUS] == c.RESP_OK
        assert msg[c.KEY_MESSAGE] == c.MSG_HEALTH_CHECK_SUCCESS

    def test_api_post_request(self):
        test_json_payload = {
            c.KEY_HEALTH_CHECK_PAYLOAD: {
                'test1': 123,
                'test2': "abc"
            }
        }
        resp = h.api_post_request(c.FLASK_BACKEND_URL + c.API_HEALTH_CHECK, test_json_payload)
        assert resp is not None
        assert resp.status_code == c.RESP_OK

        msg = resp.json()[c.KEY_HEALTH_CHECK_RESPONSE]
        assert msg[c.KEY_STATUS] == c.RESP_OK
        assert msg[c.KEY_MESSAGE] == c.MSG_HEALTH_CHECK_SUCCESS
        assert msg[c.KEY_RECEIVED_PAYLOAD] == test_json_payload
