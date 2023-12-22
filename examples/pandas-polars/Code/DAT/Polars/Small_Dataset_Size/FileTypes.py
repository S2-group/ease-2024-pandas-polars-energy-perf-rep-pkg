# Converting different filetypes
import os, shutil
import polars as pl

def FileTypes(output_files, data_file):

    # Load the CSV file into a Polars DataFrame
    df = pl.read_csv(data_file)

    PolarsSmall_json = os.path.join(output_files, "Polars_Small.json")
    PolarsSmall_parquet = os.path.join(output_files, "Polars_Small.parquet")

    # Convert the DataFrame to JSON format
    df.head(200000).write_json(PolarsSmall_json)  # Converts each row to a JSON object

    df.head(200000).write_parquet(PolarsSmall_parquet)  # Converts each row to a JSON object



for i in range(10):
    output_files = './examples/pandas-polars/Code/DAT/Polars/Small_Dataset_Size/OUTPUT_FILES'
    small_data_files = './examples/pandas-polars/Data/final_small_dataset.csv'
    FileTypes(output_files, small_data_files)

