import json
import base64


class Token:

    def __init__(self):
       pass

    @staticmethod
    def get_user(token):
        # print(token)
        if not token:
            user = None
        else:
            token_info = json.loads(base64.b64decode(token.split(".")[1] + "=="))
            user = {
                "uname": token_info.get('username'),
                "uid": token_info.get('user_id')
            }
        return user
