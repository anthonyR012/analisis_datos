
Introduction to Regression
What is Regression?

Regression: a supervised learning technique that models the relationship between a continuous target variable and explanatory features.

Example: Predicting CO2 emissions of a car using features like engine size, cylinders, and fuel consumption.

Types of Regression

Simple Regression

Uses one independent variable to estimate a dependent variable.

Can be linear (straight-line relationship) or nonlinear (curved relationship).

Example: Predicting CO2 emissions only from engine size.

Multiple Regression

Uses two or more independent variables to estimate a dependent variable.

Can also be linear or nonlinear.

Example: Predicting CO2 emissions from engine size + number of cylinders.

Applications of Regression

Sales forecasting: predict yearly sales from leads, customers, order history.

Real estate: estimate house prices from size, bedrooms, location.

Predictive maintenance: estimate when a car or machine will fail.

Income prediction: based on education, occupation, experience, age, etc.

Environmental science: predict rainfall or wildfire severity.

Public health: forecast spread of diseases, estimate risk of conditions like diabetes or cancer.

Algorithms for Regression

Classical: Linear regression, Polynomial regression.

Modern ML: Random Forest, XGBoost, K-Nearest Neighbors, Support Vector Machines, Neural Networks.

Key Takeaways

Regression predicts continuous values.

Simple regression → one variable; Multiple regression → several variables.

Widely applied in business, healthcare, environment, finance, and retail.

=================================================================================

Introduction to Simple Linear Regression
What is Simple Linear Regression?

A supervised learning method modeling a linear relationship between a continuous dependent variable (y) and one independent variable (x).

Example: Predicting CO2 emissions of a car using engine size.

How it Works

Scatter Plot

Shows the correlation between variables (engine size vs CO2).

A regression line (best-fit line) is drawn to model this relationship.

Selected by the regression algorithm to minimize error.

Residual Error

Difference between actual and predicted values.

Measured using Mean Squared Error (MSE).

Goal: find line that minimizes MSE.

Ordinary Least Squares (OLS)

Standard method to estimate coefficients (
𝜃
0
,
𝜃
1
θ
0
	​

,θ
1
	​

).

Derived by Gauss & Legendre.

Fast, simple, interpretable, no tuning needed.

Example

For engine size = 2.4 → predicted CO2 = 214.

If actual = 50, discrepancy = 90 → this difference is the residual error.

Strengths

Easy to understand and implement.

Fast for small datasets.

Provides interpretable results.

Limitations

Assumes linear relationship (fails with nonlinear patterns).

Outliers can distort results significantly.

Too simplistic for complex datasets.

Key Takeaways

Simple linear regression predicts a continuous variable from one feature.

Uses the best-fit line calculated via OLS regression.

Evaluates performance with residual error and MSE.

Useful for quick, interpretable predictions, but limited in handling complexity and outliers.