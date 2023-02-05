# voter_turnout
This was a project to generate turnout by Single Member District in DC by utilizing data found in the voter file.

Step 1:
Request voter file from DC Board of Elections by filling out the "Request for Voter Registration Data & Masps"  (https://www.dcboe.org/FOIA-Info/FOIA-Requests) and include in your request that you would like the voter history. I am not sure if they take snapshots that are stored indefinitely, so you might not be able to recreate this for the 2022 election.

Step 2:
Download the [GeoJSON file of the Single Member Districts from OpenDataDC](https://opendata.dc.gov/datasets/single-member-district-from-2023). Add that to the `data` folder.

Step 3:
Place the file in the `data` folder and make sure it is named `general_election_2022_voter_file.xlsx` and is an XLSX file.

Step 4:
At the command line, run `python3 plot.py`, and you will see the figure generated under `SMDs.png`. 

# Ideas for additional projects
1. If DC stores snapshots of the voter file, request it for the 2020 general and compare turnout changes over time. Since the SMDs changed (and the number increased) starting with the 2022 General Election, you will need to create some way to determine which SMD an address would be in during a particular year.

# Notes
* DC does not regularly purge voter files (as far as I'm aware). This is a good thing - it makes it less likely that someone will lose the ability to vote by being removed from the voter roll. However, this does mean that very transient areas will likely have lower turnout by default.
* Here is a mapping of what the abbreviation for a voting column means in the voter file means:

| Abbreviation | Meaning |
| ------------- | ------------- |
| A	| Voted absentee (includes referred ballots that were accepted) |
| B	| Absentee ballot not counted (rejected) |
| E	| Early voted |
| F	| Early voted by special ballot (Ballot was accepted) |
| N	| Did not vote |
| P	| Special ballot rejected by Board |
| X	| Ineligible to vote (e.g. independents cannot vote in primaries) |
| Y	| Voted at the polls |
| Z	| Voted at the polls by special ballot (ballot was accepted) |
