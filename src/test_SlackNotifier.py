import responses
import unittest

from SlackNotifier import SlackNotifier


class TestSlackNotifier(unittest.TestCase):
    @responses.activate
    def test_sendSlackNotification(self):

        test_slack_url = "http://test_slack_url"
        test_env_name = "test_env_name"

        responses.add(responses.POST, test_slack_url,
                      json={'response': 'fake_response'}, status=200)

        test_SlackNotifier = SlackNotifier(env_name=test_env_name, slack_webhook_url=test_slack_url)

        actual_response = test_SlackNotifier.send_slack_notification("test_message")

        assert actual_response.status_code == 200
