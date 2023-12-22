# Handling missing data

import pandas as pd

def MissingDataDAT(output_files,data_files):

    ############## COUNT MISSING VALUES AND REMOVE THEM ###############

    df = pd.read_csv(data_files)
    df_drop = df.copy()
    df_fill = df.copy()

    # Check for missing data before manipulation
    missing_counts_before_drop = df_drop.isnull().sum().sum()

    # drop missing data
    df_drop.dropna(inplace=True)

    # Check for missing data before manipulation
    missing_counts_after_drop = df_drop.isnull().sum().sum()

    ############## COUNT MISSING VALUES AND REMOVE THEM ###############



    # Fill None with 0
    df_fill.fillna(1, inplace=True) 

    # Check for missing data (None values)
    missing_counts_after_fill = df_fill.isnull().sum().sum()

   

    print(f"Missing Counts before Drop: {missing_counts_before_drop},"+
        f"\nAFTER: {missing_counts_after_drop}"+
            f"\nNULLS AFTER FILL: {missing_counts_after_fill}")
 
    
for i in range(10):
    output_files = './examples/pandas-polars/Code/DAT/Pandas/Small_Dataset_Size/OUTPUT_FILES'
    small_data_files = './examples/pandas-polars/Data/final_small_dataset.csv'
    MissingDataDAT(output_files, small_data_files)
