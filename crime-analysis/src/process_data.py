import pandas as pd
from datetime import datetime, timedelta, date
from config import Constants

################ DATA CLEANING #####################

data = pd.read_csv(f"{Constants.CRIME_DATA_FILE}")
data.columns = data.columns.str.lower()
data[Constants.DATE_COLUMN] = pd.to_datetime(data[Constants.DATE_COLUMN], format='%m/%d/%Y, %I:%M:%S %p') # convert date column to a datetime data type
data['month'] = data[Constants.DATE_COLUMN].dt.month # extract the month

##################################################

def get_pivot(data,group_by_column,month_year_or_both,remove_partial_year=True):
    """
    Returns a pivot table of grouped data.

    Parameters:
        data (pandas.DataFrame): The data to be grouped and pivoted. Uses crime data.
        group_by_column (str): The column to group the data by.
        month_year_or_both (str): Specifies whether to group by month, year, or both.
        remove_partial_year (boolean): Specifies whether or not to remove the current year from the data when summarizing by month

    Returns:
        pandas.DataFrame: A pivot table of grouped data.
    """
    time_group_columns=get_time_group_columns(month_year_or_both)
    if month_year_or_both == 'month' and remove_partial_year:
        data = remove_data_from_partial_year(data)
    group = data.groupby(time_group_columns+[group_by_column])[group_by_column].count().reset_index(name='count')
    # create a pivot table with offenses as rows, years as columns, and counts as values
    group_pivot = pd.pivot_table(group, values='count', index=group_by_column, columns=time_group_columns, fill_value=0)
    if month_year_or_both == 'both':
        # Get a list of the current column labels
        columns = group_pivot.columns.tolist()
        new_columns = sorted([date(year, month, 1).strftime('%Y-%m') for (month, year) in columns])
        group_pivot = group_pivot.set_axis(new_columns,axis=1)
    if group_by_column == 'offense':
        group_pivot = sort_offenses(group_pivot)
    return group_pivot

def store_results(dataframe,filename):
    """Stores the input Pandas DataFrame as a CSV file in the results folder with the specified file name. """
    dataframe.to_csv(f"{Constants.RESULTS_FOLDER}{filename}",index=True)
    return 1

def get_winter_data(data):
    """Get data from November to January for every year"""
    filtered_data = data[data['month'].isin([11,12,1])]
    filtered_data['group'] = filtered_data.apply(assign_winter_group,axis=1)
    winter_df = get_pivot(data,'offense','month',False)
    return winter_df

######## HELPER FUNCTIONS ################

def sort_offenses(df):
    return df.reindex(Constants.CRIME_ORDER)

def get_time_group_columns(month_year_or_both):
    options = ['month','year','both']
    if month_year_or_both not in options:
        raise ValueError(f"Invalid value '{month_year_or_both}' for 'month_year_or_both'. Options are: {options}")
    if month_year_or_both == 'month':
        return ['month']
    elif month_year_or_both == 'year':
        return ['year']
    elif month_year_or_both == 'both':
        return ['month', 'year']

def remove_data_from_partial_year(df):
    current_year = datetime.now().year
    filtered_df = df.loc[data['year'] != current_year]
    return filtered_df

def get_most_recent_date_in_data(df):
    return df[Constants.DATE_COLUMN].max()-timedelta(days=1)

def assign_winter_group(row):
    group=row['year']
    if row['month'] in [11,12]:
        return group
    else:
        return (group-1)

######### STORING SUMMARIES #########################

store_results(get_pivot(data,'offense','both'),'offense_both_summary.csv')
store_results(get_pivot(data,'offense','year'),'offense_year_summary.csv')
store_results(get_pivot(data,'offense','month'),'offense_month_summary.csv')
store_results(get_pivot(data,'method','both'),'method_both_summary.csv')
store_results(get_pivot(data,'method','year'),'method_year_summary.csv')
store_results(get_pivot(data,'method','month'),'method_month_summary.csv')
store_results(get_winter_data(data),'winter-data.csv')

######################################################