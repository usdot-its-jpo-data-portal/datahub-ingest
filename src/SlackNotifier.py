import requests


class SlackNotifier:
    def __init__(self, env_name=None, slack_webhook_url=None):
        self.env_name = env_name
        self.slack_webhook_url = slack_webhook_url

    def sendSlack_Notification(self, message):
        header = {'Content-type': 'application/json'}
        payload = '{"text":"' + self.env_name + ' | ' + message + '"}'
        return requests.post(
            self.slack_webhook_url, data=payload, headers=header)
