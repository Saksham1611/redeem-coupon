import requests

# localhost and the defined port + endpoint
url = 'http://127.0.0.1:1080/predict'
body = {
    "campaign_id": 2,
    "coupon_id": 2,
    "customer_id": 0.5,
}
response = requests.post(url, data=body)
response.json()