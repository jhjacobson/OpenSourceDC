from process import main
import pandas as pd
import os
from config import Constants

def set_outputs():
    return [
        ("percentage", True, "without_flum_percentage.csv"),
        ("percentage", False, "with_flum_percentage.csv"),
        ("area", True, "without_flum_area.csv"),
        ("area", False, "with_flum_area.csv"),
    ]

def get_batch_outputs():
    output_types = set_outputs()
    for output_type, subtract_flum_area, output_file in output_types:
        print(f"Running with output type: {output_type}, output file: {output_file}, subtract FLUM area: {subtract_flum_area}")
        main(output_type=output_type, subtract_flum_area=subtract_flum_area, output_file=output_file)
    print("All runs completed.")
    return True

def subtract_csvs(file1, file2, output_filename):
    df1 = pd.read_csv(f'{Constants.OUTPUT_DIRECTORY}{file1}', index_col=0)
    df2 = pd.read_csv(f'{Constants.OUTPUT_DIRECTORY}{file2}', index_col=0)
    filename1 = os.path.splitext(os.path.basename(file1))[0]
    filename2 = os.path.splitext(os.path.basename(file2))[0]
    result_df = df1 - df2
    with pd.ExcelWriter(f'{Constants.OUTPUT_DIRECTORY}{output_filename}') as writer:
        df1.to_excel(writer, sheet_name=filename1)
        df2.to_excel(writer, sheet_name=filename2)
        result_df.to_excel(writer, sheet_name="Difference")

def final_process():
    if get_batch_outputs() == True:
        subtract_csvs('with_flum_area.csv', 'without_flum_area.csv', 'areas.xlsx')
        subtract_csvs('with_flum_percentage.csv', 'without_flum_percentage.csv', 'percentages.xlsx')
        print("Processing complete")
        return True
    else:
        print("Processing failed")
        return False

final_process()