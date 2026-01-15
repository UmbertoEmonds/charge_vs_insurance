# Justification of Choices

- #### No Logarithmic Transformation on Charges
  - We already have a model with a good score **0.92** and a good MAE **2037 $**. Converting the charges to `log` lowered these values.

  - The `log` is often used to manage outliers; our `bmi` - `smoker` relationship creates a symmetry that compensates for the problem of charge outliers.

  - Keeping data in `$` format improves the readability of the results without resorting to calculations that could cause reconstruction problems.

- #### Normalization or Standardization?

  - We use normalization (Mix-Max) for variables that have fixed and known bounds, such as `age` or `children`.

  - We use standardization for values that have outliers, such as `bmi`.

  - For this project, we specifically use a StandardScaler for **all** our values for simplicity and consistency. This will handle the outlier issue for the BMI.

- #### Standardization after splitting

  - Prevents data leaks. Standardizing after splitting allows for minimum and maximum values specific to each dataset (train and test).

- #### Removal of regions

  - A variable with minimal impact on load. Improves software performance and avoids unnecessary OneHotEncoding.

- #### Relationship between `bmi` and `smoker`

  - New variable `ìs_obese` representing the risk threshold.

  - BMI is only relevant for smokers (relationship `smoker * bmi`)

  - We isolate the most expensive category (relationship `smoker * is_obese`)
- #### Balancing the proportions for the smoker variable in the split

  - We maintain a balanced proportion in both datasets for the value `smoker` because it has the greatest impact on costs (`stratify=df["smoker"]`).