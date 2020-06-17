# How to optimize a basic model
- using the mae to optimize leaf_nodes (tree) or n_estimators (forest)
- Try a criterion, various other parameters to model
- feature picking (choose which columns to use)
      
# Things to consider
- dealing with numerical missing values:
    - Drop column (stupid)
    - Impute some logical constant value
    - Impute mean
    - impute mean with extra column identifying missing data
    - impute mean based on extra criteria (average lotfrontage for given
      neighborhood)
- Have to encode categorical data to numerical values (codebook)
    - drop columns (stupid)
    - label encoding: single column with numbers representing categories
    - one-hot encoding: multiple boolean columns, one for each category 
