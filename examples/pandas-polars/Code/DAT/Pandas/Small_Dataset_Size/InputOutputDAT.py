import os
import pandas as pd


def InputOutputDAT(output_files, data_file):

    # Read csv dataset
    def load_csv(path):
        return pd.read_csv(path, nrows=200000)


    # Read parquet dataset
    def load_parquet(path):
        return pd.read_parquet(path, engine='pyarrow')


    # Read json dataset
    def load_json(path):
        return pd.read_json(path)

    # Save to csv
    def save_csv(df, path):
        return df.to_csv(path)

    # Save to json
    def save_json(df, path):
        return df.to_json(path)

    # Save to parquet
    def save_parquet(df, path):
        return df.to_parquet(path)

    PandasSmall_json = os.path.join(output_files, "Pandas_Small.json")
    PandasSmall_parquet = os.path.join(output_files, "Pandas_Small.parquet")
    # # Read operations
    df = load_json(PandasSmall_json)

    df = load_csv(data_file)

    df = load_parquet(PandasSmall_parquet)

    new_Csv = os.path.join(output_files, "df_adult_pandas_1.csv")
    new_JSON = os.path.join(output_files, "df_adult_pandas_1.json")
    new_parque = os.path.join(output_files, "df_adult_pandas_1.parquet")

    save_csv(df, new_Csv)
    save_json(df, new_JSON)
    save_parquet(df, new_parque)

# generating the outputfiles

for i in range(10):
    output_files = './examples/pandas-polars/Code/DAT/Pandas/Small_Dataset_Size/OUTPUT_FILES'
    small_data_files = './examples/pandas-polars/Data/final_small_dataset.csv'
    InputOutputDAT(output_files, small_data_files)
