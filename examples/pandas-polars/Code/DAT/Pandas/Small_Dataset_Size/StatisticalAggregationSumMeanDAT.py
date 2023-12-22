
import pandas as pd

def StatisticalAggregationSumMeanDAT(output_files,data_files):
    df = pd.read_csv(data_files)

    def count(df:pd.DataFrame):
        return df.count(axis=0)

    # sum
    def sum(df:pd.DataFrame):
        return df.sum()

    # mean
    def mean(df:pd.DataFrame):
        return df.mean()



    ### Statistical Operations
    dfCount = count(df)
    summedIncome = sum(df['Income'])
    MeanIncome = mean(df['Income'])


    print(f"{dfCount}\nsummedIncome: {summedIncome},\n MeanIncome: {MeanIncome}")


for i in range(10):
    output_files = './examples/pandas-polars/Code/DAT/Pandas/Small_Dataset_Size/OUTPUT_FILES'
    small_data_files = './examples/pandas-polars/Data/final_small_dataset.csv'
    StatisticalAggregationSumMeanDAT(output_files, small_data_files)