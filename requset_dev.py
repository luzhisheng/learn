import requests

url = "https://www.sunstar.com.ph/"

headers = {
    'cookie': "_chartbeat4=t=BD62l0CB5UP8Dr7StXB9v6u9C2aR4E&E=0&x=0&c=3.6&y=20358&w=959; sucuri_cloudproxy_uuid_e891b8b83=9f5df20021640b83e3d2eac5ed1c6698",
    'Cache-Control': "no-cache",
    'Postman-Token': "4bd11b57-5dea-4373-9a47-baea243733d0"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)