import json
import base64


class TokenGetUser:

    def __init__(self, token):
        print(token)
        if not token:
            self.user = None
        else:
            self.token_info = json.loads(base64.b64decode(token.split(" ")[1].split(".")[1] + "=="))
            self.user = {
                "uname": self.token_info.get('username'),
                "uid": self.token_info.get('user_id')
            }

    def info(self):
        return self.user
