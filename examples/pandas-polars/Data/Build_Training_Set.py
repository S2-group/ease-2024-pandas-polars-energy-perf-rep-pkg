import pandas as pd


df = pd.read_csv("big_dataset.csv")
print(df.columns)
print(len(df))


# Assuming you have your original DataFrame named df

# Create a sub-dataset with 50,000 rows and save it to a CSV file
sub_dataset = df.head(50000)

small_duplicated_datset = df.sample(n=1950000, replace=True)
final_small_dataset = pd.concat([sub_dataset, small_duplicated_datset])
final_small_dataset.to_csv('final_small_dataset.csv', index=False)

# Duplicate the rows of the original dataset to create a second dataset with 2,000,000 rows
big_duplicated_dataset = df.sample(n=14950000, replace=True)
# 1950000 is used because we already have 50000 rows in the sub_dataset

# Concatenate the sub-dataset and the duplicated dataset
final_big_dataset = pd.concat([sub_dataset, big_duplicated_dataset])

# Save the final dataset to a CSV file
final_big_dataset.to_csv('final_big_dataset.csv', index=False)
