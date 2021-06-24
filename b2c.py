import requests
import base64
from requests.auth import HTTPBasicAuth
from datetime import datetime


unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
#print(formatted_time)

shortcode = "3017263"
password = "BONKANJA19"

data_to_encode = shortcode + password
encoded = base64.b64encode(data_to_encode.encode())

SecurityCredential = encoded.decode("utf-8")





consumer_key = "VUESzKs16vIJG8hqZOEiXwpnOlYWhIcp"
consumer_secret = "3FIJ6mcNwrSQUXrR"
api_URL = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))



json_response = r.json()

my_access_token = json_response['access_token']

phone = 254745685152

amount = 15
  
def lipa_na_mpesa():

    
    access_token = my_access_token
    api_url = "https://api.safaricom.co.ke/mpesa/b2c/v1/paymentrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
        "InitiatorName": "EDUH",
        "SecurityCredential":SecurityCredential,
        "CommandID": "PromotionPayment",
        "Amount": "60",
        "PartyA": shortcode,
        "PartyB": "254745685152",
        "Remarks": "Sent money",
        "QueueTimeOutURL": "https://milanwriters.com/register",
        "ResultURL": "https://milanwriters.com/login",
        "Occasion": " "
    }
    
    response = requests.post(api_url, json = request, headers=headers)
    
    print (response.text)

lipa_na_mpesa()
    
    
    
 
