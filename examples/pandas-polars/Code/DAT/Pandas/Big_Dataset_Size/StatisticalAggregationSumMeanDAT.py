
import pandas as pd

def StatisticalAggregationSumMeanDAT(output_files, data_file):
    df = pd.read_csv(data_file)

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
    output_files = './examples/pandas-polars/Code/DAT/Pandas/Big_Dataset_Size/OUTPUT_FILES'
    big_data_files = './examples/pandas-polars/Data/final_big_dataset.csv'
    StatisticalAggregationSumMeanDAT(output_files, big_data_files)