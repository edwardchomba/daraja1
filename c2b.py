import requests
from requests.auth import HTTPBasicAuth

#access token

consumer_key = "x4r4ZSpDmZ6oFxrSr4EEgNeknyu0xHy5"
consumer_secret = "QINABL90BdDR7uqJ"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))



json_response = r.json()

my_access_token = json_response['access_token']


#reg url
def register_url():

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % my_access_token}
    request = {
        "ShortCode": "601521",
        "ResponseType": "Completed",
        "ConfirmationURL": "https://milanwriters.com/register",
        "ValidationURL": "https://milanwriters.com/login"}

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)

#register_url()

def simulate_c2b_transaction():
   
  
    
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % my_access_token}
    request = { 
        "ShortCode":"601521",
        "CommandID":"CustomerPayBillOnline",
        "Amount":"2",
        "Msisdn":"254708374149",
        "BillRefNumber":"12345678" }
    
    response = requests.post(api_url, json = request, headers=headers)
    
    print (response.text)

simulate_c2b_transaction()
  
  