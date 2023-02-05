class Constants:
    API_URL_PREFIX="https://maps2.dcgis.dc.gov/dcgis/rest/services/DDOT/PTP/MapServer/3/query?f=json&cacheHint=true&"
    OUTFIELDS="outFields=*&"
    REMAINDER="spatialRel=esriSpatialRelIntersects"
    SLEEP_TIME=60
    RECORD_COUNT=100
    DATA_FOLDER="../data/"
    DDOT_RECORDS_JSON=f"{DATA_FOLDER}ddot_records.json"
    DDOT_RECORDS_CSV=f"{DATA_FOLDER}ddot_records.csv"
    DATE_FORMAT="%m/%d/%Y"
