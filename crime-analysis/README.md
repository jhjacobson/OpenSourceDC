# Analysis
This is some rough analysis of Ward 1 crime trends. Goal is to have a bit more flexibility than what can currently be done with crime cards.

# Some notes on the available columns:
METHOD - three values - gun, knife, and others
YEAR
month
OFFENSE - theft/other, theft f/auto, robbery, motor vehicle theft, burglary, assault w/dangerous weapon, sex abuse, homicide, arson
offensegroup - property crime or violent crime

# Data availability
You can download all crime data from https://crimecards.dc.gov/ .

# Categories:
These are considered violent crimes:
Homicide
Sex Abuse
Assault w/ dang. weapon
Robbery

These are considered property crimes:
Burglary
Theft/Auto
Theft/Other
Motor Vehicle Theft
Arson

# Potential improvements
* Create 90 day lookback periods so you can see quarterly trends over the years
* Show a YTD metric. This is generally a poor metric though given some [concerns documented here](https://www.jratcliffe.net/post/year-to-date-comparisons-and-why-we-should-stop-doing-them)
* Allow mapping of the data