import requests

# localhost and the defined port + endpoint
url = 'http://127.0.0.1:1088/predict'
body = {
    "campaign_id": 10,
    "coupon_id": 12,
    "customer_id": 600,
}
response = requests.post(url, data=body)
response.json()