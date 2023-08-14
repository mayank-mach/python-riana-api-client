#!/usr/bin/env python3

import os
import sys
import time


import requests
import requests_http_signature


now = lambda: int(round(time.time() * 1000))


if __name__ == '__main__':
    RIANA_API_URL = os.getenv('RIANA_API_URL')
    try:
        private_key_file_path = sys.argv[1]
    except:
        print("USAGE: get_token.py <private_key_file_path> <RIANA_API_service_account_name>")
        sys.exit(1)
    try:
        private_key_id = sys.argv[2]
    except:
        print("USAGE: get_token.py <private_key_file_path> <RIANA_API_service_account_name>")
        sys.exit(1)
    try:
        private_key_file_handle = open(private_key_file_path, 'rb')
    except Exception as inst:
        print("Exception occurred: " + str(inst))
        sys.exit(1)
    try:
        response = requests.post(
            RIANA_API_URL + '/user-management/service-login',
            auth=requests_http_signature.HTTPSignatureAuth(
                #This code did not work with the latest version of the requests_http_signature libary!
                #signature_algorithm=requests_http_signature.algorithms.RSA_V1_5_SHA256,
                #Code for using version 0.2.0 of the requests_http_signature library
                algorithm='rsa-sha256',
                key=private_key_file_handle.read(),
                key_id=private_key_id),
            headers={
                'Date': str(now())
            })
    except Exception as inst:
        print("Exception occurred: " + str(inst))
        sys.exit(1)
    if response.status_code == requests.codes.ok:
        print(response.text)
        sys.exit(0)
    else:
        print("ERROR: RIANA API response was not OK: " + str(response.text))
        sys.exit(1)
