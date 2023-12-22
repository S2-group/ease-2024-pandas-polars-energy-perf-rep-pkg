import polars as pl



# Define a function to count missing values
def count(df: pl.DataFrame):
    return df.select(pl.all().is_not_null().sum())


# Define a function to calculate the sum of a column
def sum(df: pl.DataFrame):
    return df.sum()

# Define a function to calculate the mean of all columns
def mean(df: pl.DataFrame):
    return df.mean()

def StatisticalAggregationSumMeanDAT(output_files, data_file):
    # Load the CSV data into a Polars DataFrame
    df = pl.read_csv(data_file)
    # Perform statistical operations
    dfCount = count(df)
    summedIncome = sum(df['Income'])
    MeanIncome = mean(df['Income'])


    # Print the results
    print(f"{dfCount}\nsummedIncome: {summedIncome},\n MeanIncome: {MeanIncome}")


for i in range(10):
    output_files = './examples/pandas-polars/Code/DAT/Polars/Big_Dataset_Size/OUTPUT_FILES'
    big_data_files = './examples/pandas-polars/Data/final_big_dataset.csv'
    StatisticalAggregationSumMeanDAT(output_files, big_data_files)