import polars as pl

def StatisticalAggregationMinMaxUnique(output_files, data_file):
    # Load the CSV data into a Polars DataFrame
    df = pl.read_csv(data_file)


    # Define a function to find the minimum value of all columns
    def min(df: pl.DataFrame):
        return df.min()

    # Define a function to find the maximum value of all columns
    def max(df: pl.DataFrame):
        return df.max()

    # Define a function to find unique values in a column
    def unique(df: pl.DataFrame):
        return df.unique(maintain_order=True)

    # Perform statistical operations

    MinIncome = min(df['Income'])
    MaxIncome = max(df['Income'])
    States = unique(df['State'])

    # Print the results
    print(f" MinIncome: {MinIncome},\n MaxIncome: {MaxIncome},\n States: {States}")


for i in range(10):
    output_files = './examples/pandas-polars/Code/DAT/Polars/Small_Dataset_Size/OUTPUT_FILES'
    small_data_files = './examples/pandas-polars/Data/final_small_dataset.csv'
    StatisticalAggregationMinMaxUnique(output_files, small_data_files)