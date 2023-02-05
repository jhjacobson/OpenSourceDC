# Use cases
DDOT_API - uses the API from OpenData to grab DDOT data from ProTrack+.

# DC OpenData APIs
This is my attempt to document various APIs and show use cases for DC OpenData APIs. I have found two locations for APIs:
# DCGIS
*[Base URL for DCGIS](https://maps2.dcgis.dc.gov/dcgis/rest/services)
This has a lot of services available under [this link](https://services.arcgis.com/neT9SoYxizqTHZPH/ArcGIS/rest/services). I have spent a lot of time looking at the DDOT/PTP REST service [located here](https://maps2.dcgis.dc.gov/dcgis/rest/services/DDOT/PTP/MapServer). PTP is a reference to [ProTrack+](https://protrackplus.ddot.dc.gov/), a DDOT Project Management Tool. 

[This link is a sample query](https://maps2.dcgis.dc.gov/dcgis/rest/services/DDOT/PTP/MapServer/3/query?f=json&cacheHint=true&resultOffset=0&resultRecordCount=10&where=(BudgetYear%3D2023)&orderByFields=RouteName%20ASC&outFields=*&returnGeometry=false&spatialRel=esriSpatialRelIntersects) that returns 10 records from Budget Year 2023 and orders by the Route Name. Here is my attempt to explain the URL:
* https://maps2.dcgis.dc.gov/dcgis/rest/services/DDOT/PTP/MapServer/3/query?f=json& - this is the endpoint with a query request and asks for the results in JSON. You can swap out JSON for PBF to get a protobuf return.
* cacheHint=true - I have no idea what this does. I've set it to both true and false, and I get the same results
* resultOffset=0&resultRecordCount=10 - resultOffset is what record to start searching at. In this case, we are starting at record 0. resultRecordCount is the number of records to return. Different endpoints have different max records. I'm avoiding hitting these endpoints with too many requests at once to not cause issues.
* where=(BudgetYear%3D2023) - this is the filtering mechanism. %3D is unicode for =, and you can also search for null years.
* orderByFields=RouteName%20ASC - how to sort the results - in this case, sort by the RouteName ascending (DESC for descending).
* outFields=* - this filters which fields are returned. Using an asterisk will return all fields.
* returnGeometry=false - this allows you to choose whether or not to return the specific points for the feature. Set this to true if you want to receive coordinates to map the features.
* spatialRel=esriSpatialRelIntersects - not sure what this parameter does.

# ARCGIS
*[Base URL for ARCGIS](https://services.arcgis.com/neT9SoYxizqTHZPH/ArcGIS/rest/services)

