import yaml
import requests
import os

path = os.path.dirname(__file__)
url = 'https://login.ruhr-uni-bochum.de/cgi-bin/laklogin'


conf = yaml.safe_load(open(path + '/' + 'loginDetails.yaml'))
myMail = conf['lock_key_user']['email']
myPassword = conf['lock_key_user']['password']

values = {'loginid' : myMail,
        'password' : myPassword,
        'action': 'Login'}

r = requests.post(url, data=values)
print(r.content)

