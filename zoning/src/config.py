class Constants:
    ANC_GEOJSON = '../data/input/Advisory_Neighborhood_Commissions_from_2023.geojson'
    OUTPUT_DIRECTORY = '../data/output/'
    COMP_PLAN_GEOJSON_DIRTY = '../data/input/Comprehensive_Plan_Planning_Areas.geojson'
    COMP_PLAN_GEOJSON_CLEAN = '../data/input/Comprehensive_Plan_Planning_Areas_clean.geojson'
    FLUM_GEOJSON = '../data/input/Comprehensive_Plan_in_2021.geojson'
    FLUM_EXCLUDE_TYPES = ['WATER', 'FED', 'PROS']
    DEFAULT_OUTPUT_FILE = f'{OUTPUT_DIRECTORY}output.csv'
    KEEP_GEOM_TYPE_DEFAULT = True
    PROJECTED_CRS = 'EPSG:3857'