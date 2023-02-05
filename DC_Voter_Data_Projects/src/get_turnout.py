import pandas as pd
from string import ascii_letters
import datetime

VOTER_FILE_NAME = r'../data/gen_elect_2022.xlsx'
OUTPUT_FILE = '../results/SMD_turnout.csv'

df = pd.read_excel(VOTER_FILE_NAME)
reg_voters_per_smd = df['SMD'].value_counts()
vote_types_2022 = df['2022 GENERAL ELECTION(Nov/08/2022)'].value_counts()
print(vote_types_2022)

mapping = {'A':'Yes', 'B':'Attempt', 'E':'Yes', 'F':'Yes', 'N':'No', 'P':'Attempt', 'X': 'No', 'Y': 'Yes', 'Z': 'Yes'}
df['votes_2022'] = df['2022 GENERAL ELECTION(Nov/08/2022)'].map(mapping)
print(df['votes_2022'].value_counts())

print(reg_voters_per_smd)
total_voters=df.shape[0]

vote_summaries_per_smd=df.groupby('SMD')['votes_2022'].value_counts()

# Define a function to compute the turnout percentage
def turnout_perc(x):
    yes = (x == "Yes").sum()
    total = x.size
    return 100*yes/total

turnout = df.groupby("SMD")["votes_2022"].apply(turnout_perc)

turnout.to_csv(OUTPUT_FILE,index=True)