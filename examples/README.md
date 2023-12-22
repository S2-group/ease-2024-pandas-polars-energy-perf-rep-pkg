<!-- # Pandas vs Polars: A Comparison of Energy Efficiency and Performance
---  -->

## Data Analysis Tasks Benchmarking
This folder contains the scripts we wrote in order to the compare energy efficiency of pandas and polars alongside any possible correlations between the energy efficiency and performance in the two libraries. The scripts contain differnt types of data analysis tasks commonly used by data scientists and the chosen tasks inspired by the following study: [Link to the study](https://ieeexplore.ieee.org/document/10174114)

Big Dataset used: 2017 US Census Demographic Data
[Link to the dataset](https://www.kaggle.com/datasets/muonneutrino/us-census-demographic-data)

Different techniques to evaluate the libraries: 
- IO Tasks
- Handling missing data 
    - count missing data 
    - drop missing data
    - fill missing data with value
- Row Column Operations
- Statistical Aggregation
    - columnwise dataframe counting
    - summing
    - Mean
    - Min / Max
    - Unique Values
- String Operations 
- Converting to different types
    - transform to json
    - transform to parquet
- Self generated time series 
- Viewing data 
    - head
    - tail
    - dtypes
    - describe
    - shape

<!-- <a name="setup"></a> -->
## Setup
For setting up the benchmark follow the below steps from the ***root*** directory:

```shell

python3 DAT/examples/pandas-polars/Data/Build_training.py

python3 examples/pandas-polars/Code/DAT/Pandas/Big_Dataset_Size/FileTypes.py 

python3 examples/pandas-polars/Code/DAT/Pandas/Small_Dataset_Size/FileTypes.py 

python3 examples/pandas-polars/Code/DAT/Polars/Big_Dataset_Size/FileTypes.py 

python3 examples/pandas-polars/Code/DAT/Polars/Small_Dataset_Size/FileTypes.py
