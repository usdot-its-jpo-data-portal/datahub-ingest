import requests


class SlackNotifier:
    def __init__(self, env_name, slack_webhook_url):
        self.env_name = env_name
        self.slack_webhook_url = slack_webhook_url

    def sendSlackNotification(self, message):
        header = {'Content-type': 'application/json'}
        payload = '{"text":"' + self.env_name + ' | ' + message + '"}'
        return requests.post(
            self.slack_webhook_url, data=payload, headers=header)
