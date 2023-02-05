import pandas as pd
import json
from config import Constants
from datetime import datetime


# Read in the JSON file
with open(Constants.DDOT_RECORDS_JSON, "r") as json_file:
    json_data = json.load(json_file)

ddot_records_df = pd.json_normalize(json_data)
ddot_records_df.columns = ddot_records_df.columns.str.removeprefix('attributes.') #remove "attributes." prefix from column names

def clean_project_status():
    # create function that cleans the maps the projectStatus column from an int to a string 
    return ""

# Process all date columns from unix timestamps to MM/DD/YY format.
# Date columns are currently in UTC and need to be in eastern time. Need to figure out how to convert to that and only show dates
def clean_dates(df=ddot_records_df):
    date_columns = df.filter(like='Date').columns
    df[date_columns] = df[date_columns] \
                    .apply(pd.to_datetime,unit='ms',errors='coerce') \
                    .applymap(lambda date: date.strftime(Constants.DATE_FORMAT) if date is not None and date is not pd.NaT else None)    
    return df

def clean_request_type():
    # create functions that maps the requestType column from an int to a string
    return ""

def clean_functional_class():
    # create function that maps the FunctionalClass from int to string
    return ""

def clean_contract_type_id():
    # create function that maps the ContractTypeID from int to string
    return ""

ddot_records_df=clean_dates()

ddot_records_df.to_csv(Constants.DDOT_RECORDS_CSV,encoding='utf-8',index=False)