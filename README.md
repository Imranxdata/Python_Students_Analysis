# Python_Students_Analysis
Overview | Explanation | Suggestion | Conclusion

**STUDENTS SCORES ANALYSIS REPORT**

### Overview

The "Students Scores Analysis" project explores and analyzes various factors influencing students' academic performance. The project utilizes Python, NumPy, Pandas, Matplotlib, and Seaborn for data study, cleaning, transformation, and analysis. The primary focus is on understanding the impact of different variables on students' math, reading, and writing scores.

### Data Study and Importing

The project begins by loading the dataset ("Expanded_data_with_more_features.csv") into a Pandas DataFrame and provides an overview of the dataset using `head()`, `describe()`, and `info()` functions. It also checks for missing values using `isnull().sum()`.

### Data Cleaning

The dataset undergoes cleaning by dropping unnecessary columns, such as "Unnamed: 0." Additionally, the "WklyStudyHours" column is transformed to enhance data consistency.

### Analysis

#### 1. Gender Distribution

A countplot is generated to visualize the gender distribution in the dataset. The analysis reveals that the number of females in the dataset is higher than males.

#### 2. Impact of Parent's Education on Students' Scores

The project analyzes the mean scores of students based on their parents' education levels. The results are presented in both tabular and heatmap forms, indicating a positive influence of parent education on students' scores.

#### 3. Impact of Parent's Marital Status on Students' Scores

Similar to the previous analysis, this section explores the mean scores based on parents' marital status. The heatmap and table show no significant impact on students' scores due to their parents' marital status.

#### 4. Outliers in Math, Reading, and Writing Scores

Boxplots are generated to identify outliers in math, reading, and writing scores. These visualizations provide insights into the distribution and presence of outliers in each subject.

#### 5 Distribution of Ethnic Groups

The project explores the distribution of ethnic groups using a pie chart. The chart illustrates the count and percentage representation of each ethnic group among the surveyed population.

### Conclusion

The "Students Scores Analysis" project provides valuable insights into factors influencing students' academic performance. From lunch types to parental education, gender distribution, and ethnic groups, the analysis enhances our understanding of the dataset and its implications for educational outcomes.

The visualizations and analyses conducted in this project can be further utilized to inform educational strategies, interventions, and policies aimed at improving students' scores and overall academic success.
