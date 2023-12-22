import pandas as pd

def ViewData(output_files, data_files):
    # Create a sample DataFrame
    df = pd.read_csv(data_files)

    # Display the DataFrame
    print("Pandas: Display DataFrame using head()")
    print(df.head())

    print("\nPandas: Display DataFrame using tail()")
    print(df.tail())

    print("\nPandas: Display DataFrame dtypes")
    print(df.dtypes)

    print("\nPandas: Display DataFrame describe()")
    print(df.describe())

    print("\nPandas: Display DataFrame shape")
    print(df.shape)
    

for i in range(10):
    output_files = './examples/pandas-polars/Code/DAT/Pandas/Big_Dataset_Size/OUTPUT_FILES'
    big_data_files = './examples/pandas-polars/Data/final_big_dataset.csv'
    ViewData(output_files, big_data_files)