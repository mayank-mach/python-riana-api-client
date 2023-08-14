
## Installation from source
```
git clone https://gitlab.dx1.lseg.com/250063/python-riana-api-client.git
python3 -m venv venv
pip install -r requirements.txt
pip install -e ./
```

## Using the RIANA API library
```
import riana_api.v1
RIANA_API_URL = "https://manage.riana.refinitiv.com/v1"
RIANA_API_AUTHORIZATION_TOKEN = "Bearer ..."
riana_client = riana_api.v1.RIANA(RIANA_API_URL, RIANA_API_AUTHORIZATION_TOKEN, proxies=http_proxies)
riana_client.get_network_info_by_ip('159.42.100.1')
riana_client.get_datacenter_network_info(network_address='159.42.100.0/23')
```

## Using the `riana-api` CLI
The CLI will use your personal RIANA API token for authentication and requries that the following environment variables be set:
* RIANA_API_URL
* RIANA_API_AUTHORIZATION_TOKEN

Linux\MacOS:
```
export RIANA_API_URL=https://manage.riana.refinitiv.com/v1
export RIANA_API_AUTHORIZATION_TOKEN="Bearer ...."
```

Windows PowerShell 7.x:
```
$Env:RIANA_API_URL = "https://manage.riana.refinitiv.com/v1"
$Env:RIANA_API_AUTHORIZATION_TOKEN = "Bearer ...."
```

To get additional usage help for the CLI:
`riana-api --help`


## Using the `get_token.py` script
This is an example Python script that may be used to obtain a RIANA API token to authenticate a service account.

Follow the RIANA API documentation here:
https://manage.riana.refinitiv.com/ui/help/user-manual/50_03_machine_to_machine_authentication.md

Perform steps to:
* Generate the private/public keypair
* Create the service account using the RIANA API

You should then be able to use the `get_token.py` script, along with the private key file, to retrieve a token from the RIANA API.

`get_token.py <path_to_private_key_file> <RIANA_service_account_name>`

The RIANA API token has a ttl of 30 minutes and a new token may be generated at any time.
