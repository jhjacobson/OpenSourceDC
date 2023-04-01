# DC Zoning Data
The purpose of this repo is to better understand Comp Plan Planning Area information in relation to ANCs and zoning areas. 

* clean_data.py - use this to update GeoJSON files to have unique feature names
* config.py - contains configuration variables used in other scripts
* process.py - does the processing of the data. Currently, this will output the percentage of each Planning Area contained in each ANC.
* troubleshooting.py - misc Python snippets that might be helpful in troubleshooting code issues.

## Data Sources
All data can be found on [OpenDataDC](https://opendata.dc.gov/). Here are links to the relevant data sources and their last download date:
| Dataset | Last Access |
| ------- | ----------- |
| [Advisory Neighborhood Commissions from 2023](https://opendata.dc.gov/datasets/DCGIS::advisory-neighborhood-commissions-from-2023/about) | March 31, 2023 |
| [Comprehensive Plan Planning Areas](https://opendata.dc.gov/datasets/203c2342b36240949e0ad95d75a5bdca/about) | March 31, 2023 |
| [Zoning Regulation of 2016](https://opendata.dc.gov/datasets/DCGIS::zoning-regulations-of-2016/about) | March 27, 2023 |
| [Comprehensive Plan in 2021 (FLUM)](https://opendata.dc.gov/datasets/DCGIS::comprehensive-plan-in-2021/about?layer=0) | April 1, 2023 |

## Improvement ideas
* Write tests for the following: 
    * Check that CRS are equal to each other
* Write functions for the following:
    * Add a column for total ANC area and a row for total Planning Area area