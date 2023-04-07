import requests
import json
import timeit

# Replace with the actual URL, method, and headers
url = "https://resolutions.anc.dc.gov/WSMethods_Documents.aspx/GetDocuments"
method = "POST"
headers = {
    "Content-Type": "application/json; charset=UTF-8"
}

payload_for_one_month = {
    "wardsIds": "",
    "ancIds": "",
    "searchFromDate": "3/7/2023",
    "searchToDate": "4/7/2023"
}

default_payload = {
    "wardsIds": "",
    "ancIds": "",
    "searchFromDate": "",
    "searchToDate": ""
}

# Test the timing for a particular run
def get_timing(payload, runs):
    stmt = lambda: requests.request(method, url, headers=headers, data=json.dumps(payload))
    elapsed_time = timeit.timeit(stmt, number=runs)
    return elapsed_time / runs

runs = 20
default = get_timing(default_payload,runs)
print("Completed with the default timings")
proposed = get_timing(payload_for_one_month, runs)

print("Switching to proposed query would reduce load time by {:1f} seconds from {:1f} seconds in the current setup to {:1f} seconds in the future setup".format(default-proposed,default,proposed))