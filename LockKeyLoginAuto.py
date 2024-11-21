import yaml
import requests

url = 'https://login.ruhr-uni-bochum.de/cgi-bin/laklogin'


conf = yaml.safe_load(open('loginDetails.yaml'))
myMail = conf['lock_key_user']['email']
myPassword = conf['lock_key_user']['password']
ip = conf['lock_key_user']['ipadress']

values = {'loginid' : myMail,
        'password' : myPassword,
        ##'ipaddr' : ip,
        'action': 'Login'}

r = requests.post(url, data=values)
print(r.content)

