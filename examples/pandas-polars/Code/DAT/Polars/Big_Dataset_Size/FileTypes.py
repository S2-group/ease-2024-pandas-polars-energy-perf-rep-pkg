# Converting different filetypes
import os, shutil
import polars as pl

def FileTypes(output_files, data_file):

        # Load the CSV file into a Polars DataFrame
        df = pl.read_csv(data_file)

        PolarsBig_json = os.path.join(output_files, "Polars_Big.json")
        PolarsBig_parquet = os.path.join(output_files, "Polars_Big.parquet")

        # Convert the DataFrame to JSON format
        df.head(1500000).write_json(PolarsBig_json)  # Converts each row to a JSON object

        df.head(1500000).write_parquet(PolarsBig_parquet)  # Converts each row to a JSON object



for i in range(10):
    output_files = './examples/pandas-polars/Code/DAT/Polars/Big_Dataset_Size/OUTPUT_FILES'
    big_data_files = './examples/pandas-polars/Data/final_big_dataset.csv'
    FileTypes(output_files, big_data_files)