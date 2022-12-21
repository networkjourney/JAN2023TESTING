import requests

url = "https://172.16.29.213:443/restapi/v10.0/Objects/Addresses?location=vsys&vsys=vsys1&name=TEST_NET1_SAGAR"

payload={}
headers = {
  'Accept': 'application/json',
  'X-PAN-KEY': 'LUFRPT1YenJlY2xYOThOSFBSM3N0N0swby82bHFTTUk9b0FHUmtNbXZzY0VNMTZrU3JHeGpUdEpoRGFjS3dXWVdjbE9uQmMrR3BLQWg5R0xrUVJNaTFBejJiRnJlSEdSSw=='
}

response = requests.request("DELETE", url, headers=headers, data=payload, verify=False)

print(response.text)
.........