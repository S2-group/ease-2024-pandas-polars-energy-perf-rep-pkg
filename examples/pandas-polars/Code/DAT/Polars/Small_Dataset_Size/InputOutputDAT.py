import os
import polars as pl

def InputOutputDAT(output_files, data_file):
    # Read csv dataset
    def load_csv(path):
        return pl.read_csv(path, n_rows=200000)


    # Read parquet dataset
    def load_parquet(path):
        return pl.read_parquet(path)


    # Read json dataset
    def load_json(path):
        return pl.read_json(path)


    def save_csv(df, path):
        return df.write_csv(path)


    def save_json(df, path):
        return df.write_json(path)


    def save_parquet(df, path):
        return df.write_parquet(path)

    PolarsSmall_json = os.path.join(output_files, "Polars_Small.json")
    PolarsSmall_parquet = os.path.join(output_files, "Polars_Small.parquet")

    # # Read operations
    df = load_csv(data_file)
    df = load_json(PolarsSmall_json)
    df = load_parquet(PolarsSmall_parquet)

    new_Csv = os.path.join(output_files, "df_adult_polars_1.csv")
    new_JSON = os.path.join(output_files, "df_adult_polars_1.json")
    new_parque = os.path.join(output_files, "df_adult_polars_1.parquet")

    save_csv(df, new_Csv)
    save_json(df, new_JSON)
    save_parquet(df, new_parque)


for i in range(10):
    output_files = './examples/pandas-polars/Code/DAT/Polars/Small_Dataset_Size/OUTPUT_FILES'
    small_data_files = './examples/pandas-polars/Data/final_small_dataset.csv'
    InputOutputDAT(output_files, small_data_files)
