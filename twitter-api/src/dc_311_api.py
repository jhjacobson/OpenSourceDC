DELIM="|"
import requests
from auth import API_KEY_311
from auth import BEARER_TOKEN_311
from config import API_KEY_SECTION
from config import BASE_URL
from config import REQUEST_ENDPOINT
from config import USER_INFO
from datetime import datetime

# https://dc311-api.herokuapp.com/311/v4/request/23-00012543.json?api_key=6fbc647e8ff857d5a2ef40f2a033a224cb14c2a287b28436caf4bfd0403dc0fa

#service_request_id = '23-00012543'
service_request_id='22-00589006'
#service_request_id='22-00528382'
url=BASE_URL + service_request_id + '/comments.json' + API_KEY_SECTION
test=requests.get(url,headers={"Authorization":BEARER_TOKEN_311})

all_srs="https://dc311-api.herokuapp.com/311/v4/requests.json?api_key=6fbc647e8ff857d5a2ef40f2a033a224cb14c2a287b28436caf4bfd0403dc0fa&page=0&page_size=50&status=Open,Closed,Canceled&my_service_request=true&user_id=005t0000008tApeAAE&contact_email=joshhjacobson@gmail.com"
test=requests.get(all_srs,headers={"Authorization":BEARER_TOKEN_311})

def get_all_srs_for_user(page,page_size):
    page_param=f'&page={page}'
    page_size_param=f'&page_size={page_size}'
    status='&status=Open,Closed,Canceled'
    url=REQUEST_ENDPOINT+API_KEY_SECTION+page_param+page_size_param+status+USER_INFO
    return requests.get(url,headers={"Authorization":BEARER_TOKEN_311})

def get_sr_from_311(service_request_id):
    resp = requests.get(BASE_URL + service_request_id + '.json' + API_KEY_SECTION)
    if resp.status_code == 404:
        return "Invalid Service Request ID"
    else:
        return resp.json()[0]

def get_sr_comments_from_311(service_request_id):
    return 1

def get_sr_line_headers():
    return f"{DELIM}SR Status{DELIM}Latitude{DELIM}Longitude{DELIM}Service Name{DELIM}SR Last Update Date"

def not_an_sr_datapoints():
    return f"{DELIM}{DELIM}{DELIM}{DELIM}{DELIM}"


def get_sr_datapoints(service_request_id):
    sr_data=get_sr_from_311(service_request_id)
    if sr_data == "Invalid Service Request ID":
        return f"{DELIM}{sr_data}"
    else:
        status = sr_data["status"]
        lat = sr_data["lat"]
        long = sr_data["long"]
        service_name = sr_data["service_name"]
        last_update = sr_data["additional_details"]["last_updated_datetime"]
        last_update_formatted=datetime.strptime(last_update,'%Y-%m-%dT%H:%M:%S.000Z').strftime("%m/%d/%Y")
        sr_datapoints_line = f"{DELIM}{status}{DELIM}{lat}{DELIM}{long}{DELIM}{service_name}{DELIM}{last_update_formatted}"
        return sr_datapoints_line

get_sr_from_311('22-00528382')
#6fbc647e8ff857d5a2ef40f2a033a224cb14c2a287b28436caf4bfd0403dc0fa