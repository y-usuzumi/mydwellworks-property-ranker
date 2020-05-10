import requests


class MyDwellworksPropertiesExtractor:
    _base_url = 'https://mydwellworks.com/v2/relocations/rel_Ia0orTc/properties'

    def __init__(self):
        self._cookies = {
            'remember_user_token': 'BAhbCFsGaQP6JwFJIiIkMmEkMTAkYTJwcjNnbndPRWcyUTR6aGF0MDcxTwY6BkVUSSIWMTU4OTA3MzM5MS4wMjE3MjQGOwBG--67899140e672662494a2e6b0295d10004318d757',
            '_relocation_session': 'QW8xOTRSenNuU200aFVlVURLRTFGK1hVdGhLM1Z4Y3Jzd20xODZrVlVwNVp5TU85Y2JRSXB3TXhsQkVqb2JzSnN5amVhNC9vWktqczI5SmtEVzB6Um51TnJybGd0U1pjaHpjNEt6aUJoMlhXM1NSdlo5NGpWOHVVY2FNT3pjUlRYRnpwQzFqMDRVY0JRa2lUSUNGeUxKQjBraUV0ckJXRVd0bkpCQVlLYWppS1dYQ2dWQnI1UGR4cjdTOUR2a2RqdUtsaXFiaEFkbjY1ZlZXWXh5enVsOFFNa1llV2poWDVQaENES25BdkJiczhYa1lKdHJ1RVk0L1hNOE43M2xVY0pFc2pMZm93RnZMTjRjVHdYZEFFc0FveG8xblhIak1kVEFGVWhBRGZtcHo0dTMrNXZRVnJjU1FGc3d1MEFEeEFybW95enRRclpwV3hxQWtPdmFvRStROUQ5ZVVSdDhiSmdYRkV3NFp5cGpoQ0VPWWJrcytIblNWTXliYzdZZEVPQzBIQis0MjdJeXRyeUpGRTlzYUZ1SzhUUi8waytzakpoVG9wdlliempBcUFSYTBESWxUTWplYTBJZTVWSnU5cG14ZkR2bHBxdzRtWitCVlBONHZKNFE9PS0tRk5oa1NaR2xVbG5ZNkk3allycDJiQT09--b49b2bb45b2374c306eca0b8613e13e28023a211'
        }

    def extract_properties(self):
        resp = requests.get(self._base_url, cookies=self._cookies)
        return resp.json()['data']
