import polars as pl


def drop(df, cnameArray):
    return df.drop(columns=cnameArray)


def groupby(df, cname):
    return df.group_by(cname).count()


## do we want to do count?? -- doesn't do the same thing as pandas?


def merge(df1:pl.DataFrame, df2, on=None):
    return df1.join(df2, how='cross')


def sort(df, cname):
    return df.sort(cname)


def concat_dataframes(df1, df2):
    return pl.concat([df1, df2])

def RowColumnDAT(output_files, data_file):
    # # Row Column Operations

    df = pl.read_csv(data_file)
    df_samp = pl.read_csv(data_file)

    # print(drop(df, cnameArray=['Professional', 'Unemployment']))
    # groupby(df, cname='State')


    SAMPLE_SIZE = 20000
    df_samp = df.sample(SAMPLE_SIZE)
    concat_dataframes(df, df_samp)
    sort(df, 'VotingAgeCitizen')
    merge(df, df_samp)


for i in range(10):
    output_files = './examples/pandas-polars/Code/DAT/Polars/Big_Dataset_Size/OUTPUT_FILES'
    big_data_files = './examples/pandas-polars/Data/final_big_dataset.csv'
    RowColumnDAT(output_files, big_data_files)

