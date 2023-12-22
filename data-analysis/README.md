# Data Analysis

Date: 2023-10-25

>This document presents the analysis for exploring and comparing data related to energy usage between two libraries, Pandas and Polars, for two different dataframe sizes, Small and Big as well as the correlation analysis for CPU usage, Memory Usage and Execution Time with respect to energy usage

# How to run
As our data analysis is done in R Markdown files, they can be run via R-Studio either in seperate chunks or all together. They are structured into 4 Files. 2 Files for H1(Hypothesis 1) which is the comparison between pandas and polars with respect to their energy use for big/small datasets. The 2 other files represent H2 (Hypothesis 2) which is the correlation analysis between energy usage and the other dependent variables (cpu usage,memory usage and execution time). The data for this lies within the Data folder. The two .csv files (Run_Table_DAT.csv and Run_Table_TPCH.csv) are the files that are needed to run the scripts. The full runs from our Experiment can be found either for the TPCH Benchmarking in TPCH-FULLRUN.zip.rar or for our Data Analysis Tasks (DAT) within DAT-FULLRUN.zip (both in the ./Data folder).

### Measures of Central Tendency and Variability
The code calculates the mean and median for energy usage in the TPCH dataset for different library types (Pandas and Polars) and dataframe sizes (Small and Big). It also calculates the standard deviation and variance. This is done for correlation analysis as well respectively.

### Normality - Visualize Data for Normality Checking
In this section, we create density and violin plots to visualize the data distribution of energy usage. These plots are created for both the Small and Big datasets, comparing Pandas and Polars libraries.

### QQ Plots
This section generates Quantile-Quantile (QQ) plots to visually assess whether the data follows a normal distribution. QQ plots are created for both Small and Big datasets for both Pandas and Polars libraries. For Correlation Analysis this has been done for all pairs to visualize the different distributions and their accordance to normality.

### Find Skewed Data and Apply Transformations
In this section, we check if the data is positively or negatively skewed and, if so, apply transformations to enhance the normality of the data. We calculate skewness and apply different transformations (square root or power) based on the type of skew. We also check the normality change of the data after applying these transformations.

### Normality Testing on Original Data
We perform the Shapiro-Wilk test to assess the normality of the original data for both Small and Big datasets in Pandas and Polars as well as for the multitude of pairs for correlation analysis libraries. A low p-value indicates departure from normality.

### Hypothesis Testing
We conduct a non-parametric Wilcoxon rank-sum test to compare energy usage between Pandas and Polars libraries for both Small and Big datasets as our data is generally not normally distributed (especially not when doing paired analysis of the dependent variables). The "alternative" parameter is set to "two.sided" for a two-tailed test. Also, Scatterplots are done to check correlations.

### Effect Size Estimation
For Comparison of Pandas/Polars within the two datasets, we calculate Cliff's Delta for the Big and Small datasets separately, providing an effect size measurement to quantify the difference in energy usage between Pandas and Polars libraries. Confidence Intervalls can be interpreted as well. The results are printed.

>This document provides a comprehensive analysis of the energy usage data, including data exploration, normality assessment, hypothesis testing, and effect size estimation for the TPCH dataset using the Pandas and Polars libraries.