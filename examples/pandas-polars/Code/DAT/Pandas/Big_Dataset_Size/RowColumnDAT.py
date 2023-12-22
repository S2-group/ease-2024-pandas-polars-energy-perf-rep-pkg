import pandas as pd

 # drop Operations 
def drop(df, cnameArray):
    return df.drop(columns=cnameArray)

 # groupby Operations 
def groupby(df, cname):

    print(df.groupby(cname).agg('count'))
    return df.groupby(cname).agg('count')


 # merge Operations 

def merge(df1, df2, on=None):
   
    # This operation allows duplications and combines all rows from both DataFrames.
    return df1.merge(df2, how="cross")
  

#sort operations
def sort(df, cname):
    return df.sort_values(by=[cname])


#concat operations
def concat_dataframes(df1, df2):
    return pd.concat([df1, df2])


# # Row Column Operations
def RowColumnDAT(output_files, data_file):
    df = pd.read_csv(data_file)
    df_samp = pd.read_csv(data_file)
    drop(df, cnameArray=['Professional', 'Unemployment'])
    groupby(df, cname='State')
    SAMPLE_SIZE = 20000
    df_samp = df.sample(SAMPLE_SIZE)
    concat_dataframes(df, df_samp)
    sort(df, 'VotingAgeCitizen')
    merge(df, df_samp)

for i in range(10):
    output_files = './examples/pandas-polars/Code/DAT/Pandas/Big_Dataset_Size/OUTPUT_FILES'
    big_data_files = './examples/pandas-polars/Data/final_big_dataset.csv'
    RowColumnDAT(output_files, big_data_files)