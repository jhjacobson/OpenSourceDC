import json
from config import Constants

# Read in the GeoJSON data
with open(Constants.COMP_PLAN_GEOJSON_DIRTY) as f:
    data = json.load(f)

# Iterate over the features and change the field name
for feature in data['features']:
    feature['properties']['PLAN_NAME'] = feature['properties'].pop('NAME')

# Write the updated GeoJSON data to a new file
with open(Constants.COMP_PLAN_GEOJSON_CLEAN, 'w') as f:
    json.dump(data, f)