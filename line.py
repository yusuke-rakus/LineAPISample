import requests


class LINEBot:
    def __init__(self, token):
        self.url = 'https://notify-api.line.me/api/notify'
        access_token = token
        self.headers = {'Authorization': 'Bearer ' + access_token}

    def send(self, message):
        payload = {'message': message}
        requests.post(self.url, headers=self.headers, params=payload)


line_bot = LINEBot('AfICVbtQ8rRnPQe9gfau1els5InLkNzFYHHPoKH6Wx0')
line_bot.send('hej')
