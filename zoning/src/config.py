class Constants:
    ANC_GEOJSON = '../data/Advisory_Neighborhood_Commissions_from_2023.geojson'
    COMP_PLAN_GEOJSON_DIRTY = '../data/Comprehensive_Plan_Planning_Areas.geojson'
    COMP_PLAN_GEOJSON_CLEAN = '../data/Comprehensive_Plan_Planning_Areas_clean.geojson'
    FLUM_GEOJSON = '../data/Comprehensive_Plan_in_2021.geojson'
    FLUM_EXCLUDE_TYPES = ['WATER', 'FED', 'PROS']
    OUTPUT_FILE = '../data/output.csv'
    KEEP_GEOM_TYPE_DEFAULT = True
    PROJECTED_CRS = 'EPSG:3857'