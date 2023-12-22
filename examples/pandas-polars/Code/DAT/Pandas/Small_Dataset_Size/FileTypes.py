# Converting different filetypes
import os, shutil
import pandas as pd


def FileTypes(output_files, data_file):

    # Load the CSV file into a Pandas DataFrame
    df = pd.read_csv(data_file)

    PandasSmall_json = os.path.join(output_files, "Pandas_Small.json")
    PandasSmall_parquet = os.path.join(output_files, "Pandas_Small.parquet")

    # Convert the DataFrame to JSON format
    # Converts first 10% of rows to a JSON object
    df.head(200000).to_json(PandasSmall_json)  # Converts each row to a JSON object

    # Convert the DataFrame to parquet format
     # Converts first 10% of rows to a parquet object
    df.head(200000).to_parquet(PandasSmall_parquet)


for i in range(10):
    output_files = './examples/pandas-polars/Code/DAT/Pandas/Small_Dataset_Size/OUTPUT_FILES'
    small_data_files = './examples/pandas-polars/Data/final_small_dataset.csv'
    FileTypes(output_files, small_data_files)

