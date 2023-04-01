import geopandas as gpd
import pandas as pd
import argparse
from config import Constants

# Reads the ANC and Comprehensive Plan GeoJSON files
def read_geojson_files(anc_geojson, comp_plan_geojson):
    ancs = gpd.read_file(anc_geojson)
    planning_areas = gpd.read_file(comp_plan_geojson)
    return ancs, planning_areas

# Converts the GeoDataFrames to a projected CRS
def project_geodataframes(ancs, planning_areas):
    ancs = ancs.to_crs(Constants.PROJECTED_CRS)
    planning_areas = planning_areas.to_crs(Constants.PROJECTED_CRS)
    return ancs, planning_areas

# Calculates the intersections between the ANCs and Planning Areas
def calculate_intersections(ancs, planning_areas):
    return gpd.overlay(ancs, planning_areas, how='intersection', keep_geom_type=False)

# Calculates the area percentages for each intersection
def calculate_area_percentages(intersections, planning_areas):
    intersections['intersection_area'] = intersections.geometry.area
    planning_areas['total_area'] = planning_areas.area
    merged_data = intersections.merge(planning_areas[['PLAN_NAME', 'total_area']], on='PLAN_NAME')
    merged_data['percentage'] = (merged_data['intersection_area'] / merged_data['total_area']) * 100
    return merged_data

# Creates a table with ANCs as rows, Planning Areas as columns, and percentages as values
def create_table(merged_data, output_type='percentage'):
    if output_type == 'percentage':
        result_table = pd.pivot_table(merged_data, values='percentage', index='ANC_ID', columns='PLAN_NAME', fill_value=0, aggfunc=sum)
        result_table = result_table.div(result_table.sum(axis=0), axis=1) * 100
        result_table = result_table.round(1)
    elif output_type == 'area':
        result_table = pd.pivot_table(merged_data, values='intersection_area', index='ANC_ID', columns='PLAN_NAME', fill_value=0, aggfunc=sum)
    else:
        raise ValueError("Invalid output_type. Choose either 'percentage' or 'area'.")
    return result_table

# Saves the result table as a CSV file
def save_table_to_csv(result_table, output_file):
    result_table.to_csv(output_file)

def main(output_type):
    ancs, planning_areas = read_geojson_files(Constants.ANC_GEOJSON, Constants.COMP_PLAN_GEOJSON_CLEAN)
    ancs, planning_areas = project_geodataframes(ancs, planning_areas)
    intersections = calculate_intersections(ancs, planning_areas)
    merged_data = calculate_area_percentages(intersections, planning_areas)
    result_table = create_table(merged_data, output_type)
    save_table_to_csv(result_table, Constants.OUTPUT_FILE)

if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Calculate the percentage or area of each Planning Area within each ANC.')

    # Add the output_type argument
    parser.add_argument('-t', '--type', type=str, choices=['percentage', 'area'], default='percentage',
                        help='Output type: "percentage" or "area". Defaults to "percentage".')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the main function with the output_type argument
    main(output_type=args.type)