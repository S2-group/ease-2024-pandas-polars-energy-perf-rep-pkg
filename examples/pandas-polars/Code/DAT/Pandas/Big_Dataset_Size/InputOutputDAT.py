import os
import pandas as pd

def InputOutputDAT(output_files, data_file):
    # Read csv dataset
    def load_csv(path):
        return pd.read_csv(path, nrows=1500000)


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

    # Save to json
    def save_parquet(df, path):
        return df.to_parquet(path)

    # # Read operations
    PandasBig_json = os.path.join(output_files, "Pandas_Big.json")
    PandasBig_parquet = os.path.join(output_files, "Pandas_Big.parquet")

    jdf = load_json(path=PandasBig_json)

    cdf = load_csv(path=data_file)

    pdf = load_parquet(path=PandasBig_parquet)


    new_Csv = os.path.join(output_files, "df_adult_pandas_1.csv")
    new_JSON = os.path.join(output_files, "df_adult_pandas_1.json")
    new_parque = os.path.join(output_files, "df_adult_pandas_1.parquet")

    save_csv(cdf, new_Csv)
    save_json(jdf, new_JSON)
    save_parquet(pdf, new_parque)

# generating the outputfiles

for i in range(10):
    output_files = './examples/pandas-polars/Code/DAT/Pandas/Big_Dataset_Size/OUTPUT_FILES'
    big_data_files = './examples/pandas-polars/Data/final_big_dataset.csv'
    InputOutputDAT(output_files, big_data_files)
