import requests

# localhost and the defined port + endpoint
url = 'http://127.0.0.1:1088/predict'
body = {
    "campaign_id": 9,
    "coupon_id": 691,
    "customer_id": 455,
}
response = requests.post(url, data=body)
response.raise_for_status()  # raises exception when not a 2xx response
if response.status_code != 204:
    print("ERROR")
else:
    response.json()