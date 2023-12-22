import polars as pl

# Define a function to find the minimum value of all columns
def min(df: pl.DataFrame):
    return df.min()

# Define a function to find the maximum value of all columns
def max(df: pl.DataFrame):
    return df.max()

# Define a function to find unique values in a column
def unique(df: pl.DataFrame):
    return df.unique(maintain_order=True)

def StatisticalAggregationMinMaxUnique(output_files, data_file):
    # Perform statistical operations
    df = pl.read_csv(data_file)
    MinIncome = min(df['Income'])
    MaxIncome = max(df['Income'])
    States = unique(df['State'])

    # Print the results
    print(f" MinIncome: {MinIncome},\n MaxIncome: {MaxIncome},\n States: {States}")

for i in range(10):
    output_files = './examples/pandas-polars/Code/DAT/Polars/Big_Dataset_Size/OUTPUT_FILES'
    big_data_files = './examples/pandas-polars/Data/final_big_dataset.csv'
    StatisticalAggregationMinMaxUnique(output_files, big_data_files)