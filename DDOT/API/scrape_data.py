import requests
import json
import time
from config import Constants

def generate_url(offset=0, record_count=10, budget_year_value=2023, returnGeometry="false"):
    result_string = f"resultOffset={offset}&resultRecordCount={record_count}&"
    where_clause = f"where=(BudgetYear%3D{budget_year_value})&" 
    ORDER_BY = "orderByFields=RouteName%20ASC&" 
    returnGeometry = f"returnGeometry={returnGeometry}&" 
    return Constants.API_URL_PREFIX + result_string + where_clause + ORDER_BY + Constants.OUTFIELDS + returnGeometry + Constants.REMAINDER

# Write records to a JSON file
def write_file(records,file_name="../data/records.json"):
    with open(file_name, "w") as file:
        json.dump(records, file)

# Keep making API calls until all records have been retrieved
def get_all_records_for_year(budget_year_value,records):
    # Initialize variables for pagination
    offset = 0
    print(f"Collecting records for {budget_year_value}")
    while True:
        try:
            # Make API call with current offset and record count
            url=generate_url(offset,Constants.RECORD_COUNT,budget_year_value)
            data = requests.get(url).json()
            # Append records to the list
            records.extend(data['features'])
            # Check if there are more records
            if 'exceededTransferLimit' not in data:
                print("Finished collecting records.")
                break
            offset += Constants.RECORD_COUNT
            print(f"Finished getting record {offset}")
            time.sleep(Constants.SLEEP_TIME)
        except Exception as e:
                print("An error occurred:", e)
    return records

def get_records():
    records=[]
    budget_year_list=[2023,2022,2021,2020]
    for budget_year in budget_year_list:
        get_all_records_for_year(budget_year,records)
    write_file(records=records)

get_records()