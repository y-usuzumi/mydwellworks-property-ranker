import requests
from .conf import get_config


class MyDwellworksPropertiesExtractor:
    _base_url = 'https://mydwellworks.com/v2/relocations/rel_Ia0orTc/properties'

    def __init__(self):
        conf = get_config()
        conf_auth = conf['auth']
        self._cookies = {
            'remember_user_token': conf_auth['rememberUserToken'],
            '_relocation_session': conf_auth['relocationSession']
        }

    def extract_properties(self):
        resp = requests.get(self._base_url, cookies=self._cookies)
        return resp.json()['data']
