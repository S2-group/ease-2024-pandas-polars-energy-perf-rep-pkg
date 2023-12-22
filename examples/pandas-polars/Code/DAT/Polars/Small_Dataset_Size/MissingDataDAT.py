# Handling missing data

# Handling missing data

import polars as pl
#import pandas as pd

def MissingDataDAT(output_files, data_file):
    ############## COUNT MISSING VALUES AND REMOVE THEM ###############

    df = pl.read_csv(data_file)
    df_drop = df.clone()
    df_fill = df.clone()

    # Check for missing data before manipulation
    missing_counts_before_drop = df_drop.null_count().sum(axis=1)

    df_drop = df_drop.drop_nulls()

    missing_counts_after_drop = df_drop.null_count().sum(axis=1)

    ############## COUNT MISSING VALUES AND REMOVE THEM ###############

    #pandas_df_fill_BEFORE = df_fill.to_pandas()
    #count_ones_before_fill = (pandas_df_fill_BEFORE == 1).values.sum()


    # Replace None with 0
    df_fill = df_fill.fill_null(1)  

    # Check for missing data (None values)
    missing_counts_after_fill = df_fill.null_count().sum(axis=1)

    #pandas_df_fill_AFTER = df_fill.to_pandas()
    #count_ones_after_fill = (pandas_df_fill_AFTER == 1).values.sum()



    print(f"Missing Counts before Drop: {missing_counts_before_drop},"+
        f"\nAFTER: {missing_counts_after_drop}"+
            f"\nNULLS AFTER FILL: {missing_counts_after_fill}")


for i in range(10):
    print("Hello I am here")
    output_files = './examples/pandas-polars/Code/DAT/Polars/Small_Dataset_Size/OUTPUT_FILES'
    small_data_files = './examples/pandas-polars/Data/final_small_dataset.csv'
    MissingDataDAT(output_files, small_data_files)














