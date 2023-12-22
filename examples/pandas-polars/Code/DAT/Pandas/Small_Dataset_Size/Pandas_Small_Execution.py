from FileTypes import FileTypes
from InputOutputDAT import InputOutputDAT
from MissingDataDAT import MissingDataDAT
from StatisticalAggregationMinMaxUnique import StatisticalAggregationMinMaxUnique
from StatisticalAggregationSumMeanDAT import StatisticalAggregationSumMeanDAT
from ViewData import ViewData
import os, shutil

# Specify the desired working directory

def execute_files(n_times):
    for i in range(n_times):
        current_directory = os.getcwd()
        output_files = './examples/pandas-polars/Code/DAT/Pandas/Small_Dataset_Size/OUTPUT_FILES'
        small_data_files = './examples/pandas-polars/Data/final_small_dataset.csv'


        FileTypes(output_files, small_data_files)
        MissingDataDAT(output_files, small_data_files)
        StatisticalAggregationMinMaxUnique(output_files, small_data_files)
        StatisticalAggregationSumMeanDAT(output_files, small_data_files)
        ViewData(output_files, small_data_files)
        InputOutputDAT(output_files, small_data_files)


execute_files(10)


        