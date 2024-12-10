# Heritage Housing.

## Overview

The Heritage Housing project is a data analysis project designed to help a client maximise the sale price of homes they have inherited in Ames, Iowa. To achieve this, the client has provided a dataset that includes house sale prices and various features of the properties. Our goal is twofold: to identify the optimal sale price for these homes and to analyze how specific property features influence their market value. These objectives are further detailed in the Business Requirements section.

The project findings are presented through an interactive Streamlit dashboard, hosted on [Heroku](https://heritage-house-9fb9b02e459c.herokuapp.com/), allowing for easy visualisation and exploration of the results.

To ensure a structured and systematic approach, the project follows the CRoss Industry Standard Process for Data Mining (CRISP-DM). This six-phase methodology provides a comprehensive framework for navigating the data science life cycle, from understanding the business problem to delivering actionable insights.

## Business objectives:
The CRISP-DM process starts with a thorough analysis of business objectives. For this project they were clearly defined in [Handbook: Heritage Housing Issues](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PA_PAGPPF+2/courseware/bde016cdbd184cdeafd341a73807e138/bd2104eb84de4e48a9df6f685773cbf2/). They are presented unaltered here.

As a good friend, you are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximising the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

1. The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.

2. The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

#### Is there any business requirement that can be answered with conventional data analysis?
1.  Yes, we can use conventional data analysis to investigate how house attributes are correlated with the sale prices.

#### Does the client need a dashboard or an API endpoint?
1. The client needs a dashboard

#### What does the client consider as a successful project outcome?
1. A study showing the most relevant variables correlated to sale price.
2. Also, a capability to predict the sale price for the 4 inherited houses, as well as any other house in Ames, Iowa.

#### Can you break down the project into Epics and User Stories?
1. Information gathering and data collection.
2. Data visualisation, cleaning, and preparation.
3. Model training, optimization and validation.
4. Dashboard planning, designing, and development.
5. Dashboard deployment and release.

These epics were used to develop user stories added to a [kanban board](https://github.com/users/ewradcliffe/projects/6) in the project repository.

#### Ethical or Privacy concerns?
1. No. The client found a public dataset.

#### Does the data suggest a particular model?
1. The data suggests a regressor where the target is the sale price.

#### What are the model's inputs and intended outputs?
1. The inputs are house attribute information and the output is the predicted sale price.

#### What are the criteria for the performance goal of the predictions?
1. We agreed with the client an R2 score of at least 0.75 on the train set as well as on the test set.

#### How will the client benefit?
1. The client will maximise the sales price for the inherited properties.

## Dataset Content

The next phase of the CRISP-DM process focuses on data understanding. Most of this phase was conducted in jupyter Notebook 02 - Data Inspection, where the dataset was explored in detail. For the convenience of other analysts, the data is presented here along with a summary of initial observations to provide a clear starting point for further analysis.

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data).

* The dataset has 1460 observations and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|


#### Initial observations
1. We don't know how representative this sample is:
  *  We don’t know the extent to which the data set captures all of the house sales in the area, or if feature distribution reflects the city.
  * We don’t know the time of sale. The housing market can vary over time based on factors such s a change in interest rates.
  * We don’t know the location within the city. The housing market can vary tremendously in an area depending on factors such as crime rate, distance to amenities etc.

2. There is significant missing data. We will need a strategy to deal with this.

## Hypothesis and how to validate?

### Hueristics.

Initial examination of the data revealed that other than the target SalePrice, there were three categories of features:

1. Features related to the size of a house.
2. Features related to the condition of the house.
3. Features related to time (when the house was constructed or when renovation work was completed).

Based on conventional wisdom we made three heuristic observations about these categories:

1. Larger houses would be more expensive than smaller houses.
2. Houses in good condition would be more expensive than houses in poor condition.
3. Age would not affect the value of the house.

We then formulated these heuristics into testable hypothesis:

### Hypothesis 1
H0 (Null hypothesis): There is no correlation between the size of the house and the price of a house.

H1 (Alternative hypothesis): There is a positive correlation between the size of the house and the price of a house.

### Hypothesis 2
H0 (Null hypothesis): There is no correlation between the condition of the house and the price of a house.

H1 (Alternative hypothesis): There is a positive correlation between the condition of the house and the price of a house.

### Hypothesis 3
H0 (Null hypothesis): There is no correlation between the age of the house and when it was last reconditioned and the price of a house.

H0 (Null hypothesis): There is a positive correlation between the age of the house and when it was last reconditioned and the price of a house.

These Hypotheses are tested in Jupyter notebook 05 - PriceCorrelationStudy. Spearman and Pearson correlations were conducted and the results displayed on the Project Hypothesis page of the dashboard, with the following conclusions.

### Conclusion

### Hypothesis 1
There is a positive relationship between SalePrice and 'GarageArea', 'GrLivArea', 'TotalBsmtSF'. As these factors increase in size, so does the house price. The null hypothesis is disproven, the alternative hypothesis is true.

### Hypothesis 2
There is a positive relationship between SalePrice and 'KitchenQual' and 'OverallQual'. As quality ratings increase, so does the house price. The null hypothesis is disproven, the alternative hypothesis is true.

### Hypothesis 3
There is a positive relationship between SalePrice and 'YearBuilt', and 'YearRemodAdd'. Newer houses and those recently remodelled have higher prices than older houses. The null hypothesis is disproven, the alternative hypothesis is true.

## The rationale to map the business requirements to the Data Visualisations and ML tasks
**Business Requirement 1:** The client is interested in discovering how house attributes correlate with sale prices. Therefore, the client expects data visualisations of the correlated variables against the sale price.  

*  We will inspect the data related to house prices  
* We will perform Pearson and Spearman correlation studies to investigate how the variables are related to Sale Price.  
* We can extract the most important variables.
* We will plot the main variables against Sale Price to assist the client in visualising the relationship between them.
* We will display this on the dashboard.


**Business Requirement 2:** The client is interested in predicting the house sale prices from her 4 inherited houses, and any other house in Ames, Iowa.  
* We want to be able to predict the best sale price of the clients houses. We want to use an ML model based on regression analysis.
* We can train, validate and test the model using the data provided. 
* We can use this model to provide the client with estimations as to the best sale price for her houses, and display it on the dashboard.
* We can add input widgets for the most important variables to the dashboard, so the client can see the potential Sale Price of any other house in Ames, Iowa.

## ML Business Case
### Predict house prices
#### Regression Model
1 - We want an ML model to predict the highest sale price based on the data collected. As the target variable is price, a regression model is most appropriate. We want to be able to output a single figure - price. 

2 - The ideal outcome is to be able to provide our client with a tool for accurately predicting house prices and an understanding of what the most important variables for determining house prices are.

3 - We agreed with the client an R2 score of at least 0.75 on the train set as well as on the test set.

4 - We can also investigate different models for a better R2 score.

## Data understanding, preparation and modelling.
The Data Understanding, Data Preparation and Modelling phases of the CRISP-DM paradigm were undertaken in Jupyter Notebooks.  

### 01 - Data Collection
The House Price dataset and Inherited Houses dataset was sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data) and saved as CSV files.

### 02 - Data Inspection
The data was loaded and investigations were performed to describe the data, establishing the type, distribution, extent of missing data and outliers of the housing data set. Scatter plots visualised the relationships between the features and target variable (SalePrice). A number of observations were recorded, notably that there was substantial missing data, and that the features could be placed into three categories: Features related to house size, features related to house condition and features related to house quality. These investigations were critical to formulating the three hypotheses and are detailed in the notebook in full.

The Inherited house data set was loaded however only limited investigations were necessary as we will not be using this data to produce a model, and no data was missing.

### 03 - Data Cleaning
This section, along with Feature Engineering, constitutes the data preparation phase of CRISP-DM. The purpose of this notebook was to clean the data in preparation for subsequent investigative phases, guided by observations from the Data Inspection notebook. Since machine learning models require complete datasets for training, handling missing data was a critical step.

The features 'EnclosedPorch' and 'WoodDeckSF' were removed from both datasets due to the extensive missing data they contained. Imputing these missing values posed a higher risk of distorting the analysis compared to simply omitting these features.

Following this step, 797 observations in the House Price dataset remained complete. Further investigations examined the impact of various imputation methods on the data.

Several numeric, continuous features ('LotFrontage,' 'BedroomAbvGr,' '2ndFlrSF,' 'GarageYrBlt,' and 'MasVnrArea') exhibited skewed distributions (either positively or negatively). Imputation using the median was explored, as it was found to have minimal impact on the features' distribution and range. This approach significantly increased the number of usable observations without introducing substantial distortion, making it the preferred method for this dataset.

For categorical features such as 'GarageFinish' and 'BsmtFinType1,' missing values were treated as representing the absence of the corresponding feature (e.g., houses without a garage or a finished basement). Investigations confirmed that this approach had little effect on the data's overall distribution, and it was therefore applied to the House Price dataset.

### 04 - Feature Engineering
This section, together with Data Cleaning, forms the data preparation phase of CRISP-DM. Both correlation studies and machine learning models require data to be in specific formats, and we have a variety of transformation tools available for this purpose. Before applying these transformations, we first evaluate their effects.

A function is used to analyse the impact of different transformations on the variables. For ordinal variables that are not already in ordinal format, we apply the OrdinalEncoder from sklearn. For numerical variables, the Power Transformer from Pythons Feature Engine library is selected to address skewness and stabilise variance.

The Data Inspection notebook revealed a significant number of outliers. Instead of removing them, we use the Windsoriser from Feature Engine, which caps extreme values at specified minimum and maximum limits. This approach retains more observations while mitigating the influence of outliers.

Next, we examine the impact of Feature Scaling, which standardises variables to a common scale. This prevents any single variable from disproportionately influencing the model. We choose the StandardScaler from Feature Engine.

Finally, we assess feature correlations using Pearson and Spearman correlation tests. Features with strong correlations (above 0.6) are identified for removal. Eliminating these redundant features reduces the model’s complexity and training time without compromising accuracy.


### 05 - Price Correlation Study
The Price Correlation Study addresses the first business requirement: understanding how house attributes correlate with sale prices and generating data for client visualisations on our dashboard. This study also supports testing our three hypotheses.

Categorical data is encoded using the sklearn OrdinalEncoder before performing Pearson and Spearman correlation analyses between each feature and the sale price. These methods are suited to different data types, and comparing their results provides a broader perspective. Notably, both analyses consistently identify the three most strongly correlated features.

We combine the findings from both methods and create visualizations to present to the client. The data is also used to test our three hypotheses, with additional visualizations prepared to illustrate the results.

### 06 - Modelling and Evaluation.
This notebook is one of two dedicated to the modelling phase of the CRISP-DM methodology. It focuses on addressing the second business requirement: predicting house sale prices for our client's four inherited houses and any other house in Ames, Iowa.

The cleaned house price dataset is loaded and split into training, testing, and validation sets. A pipeline is built to implement the data transformation steps outlined in the Feature Engineering notebook. For this pipeline, we opted to use the Ordinal Encoder from Feature Engine instead of sklearn to ensure better integration. This choice does not affect the reliability of the transformed data.

A linear regression model is developed using a neural network architecture. The input layer contains a number of nodes equal to the number of input features, while the output layer, as required for regression, has a single node. After extensive experimentation, the best-performing configuration was determined to include four hidden layers of 512 nodes, each followed by a dropout layer with a rate of 0.25. The activation function for all layers is Rectified Linear Unit (ReLU). The model is optimized using Adam, with the loss function set to Mean Squared Error (MSE).

Model performance is evaluated based on the agreed criterion of achieving an R² score of at least 0.75.

#### Key Notes:
Model Deployment: The model and pipeline in this notebook were not deployed to the dashboard. Instead, a second model and pipeline were created in Notebook 07 - Modelling Most Important Features to provide a better user experience. However, this notebook remains a crucial part of the project documentation, as it contains the foundational work for the modelling phase.

Encoder Correction: Initially, the Ordinal Encoder was set to arbitrary encoding instead of ordered encoding, which caused unexpected behavior during early testing. While the pipeline from this notebook was not deployed, the error has been corrected, and the model was retrained on the updated pipeline for the convenience of future developers.

Inherited house data set prediction: The pipeline and model from this notebook were used to predict the sale prices of the client’s four inherited houses. However, these predictions are not displayed on the dashboard, as the dashboard uses predictions generated by the deployed model from Notebook 07 - Modeling Most Important Features. Despite this, the code and predictions from this notebook have been retained for consistency and documentation purposes.

### 07 - Modelling most important Features.
The model and pipeline in the notebook above was trained on 16 features. This meant that a user wishing to use it to predict a house price would need to gather data for all 16 features. To simplify this process and provide convenience for users, a second model was created using the five features most strongly correlated with SalePrice from the Price Correlation Study.

The same pipeline and model architecture were applied. Experiments showed that reducing the number of features did not significantly affect model accuracy.

Finally, the clients Inherited house dataset was put through the pipeline and model to produce house price predictions which could be displayed on the dashboard.

## Dashboard Design
A dashboard was created to present the project findings to the client. The content was agreed with the client prior to the project and created with the streamlit app.

### Page 1: Quick project summary

#### Describe Project Dataset
The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data) and provided by Code Institute. It features 1460 observations and 23 features.

#### State Business Requirements
1. The client is interested in discovering how the house attributes correlate with the sale price. 

2. The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

#### Project Terms & Jargon
* Features: The individual characteristics of a house, such as number of bedrooms.
* Target: The characteristic we are interested in predicting. In this case Sale Price.
* Saleprice: The price at which a house has been sold in USD.
* Inherited house: A house the client has inherited and wishes to sell.

### Page 2: Findings 

Answers business requirement 1 by presenting the results of the Pearson and Spearman correlation studies. Proof is demonstrated by:

1. Dataframe showing which features are strongly and very strongly correlated with SalePrice.

2. Data Visualisation: An interactive plotly chart shows the combined correlation of all features. Users can control the threshold at which features are selected with a slider input widget to group features together.

3. Dataframe showing the correlation of all features with SalePrice. This is collapsible to save space.

4. Conclusion section which interprets the data.

### Page 3: Display 4 houses' attributes and their respective predicted sale price. 

Answers business requirement 2. 

1. Displays a dataframe of the prices of the clients inherited houses as predicted by the model.

2. Interactive widget allowing users to input live data to predict a house price using the same model. Considerable attention has been paid to making user experience as intuitive as possible:

* Because the model can only make a prediction if all inputs are provided, the model was trained using only features which were strongly or very strongly correlated with SalePrice. The user only has to gather five features, not twenty one. 

* Radio buttons were used for KitchenQual and OverallQual. Options are based on those in the original data set. The original data set did provide for five grades of KitchenQual however as the original observations only reported four of them and there was no missing data for this feature it wasn't possible to train the model with them.

* Sliders were selected for GarageArea, GrLivArea and TotalBsmtSF to make it easy for the user to move the value over a large range. The minimum input is zero in all cases, as it is possible for any of these features to be absent. The top range was based on an appreciation of the top ranges reported for these features, but rounded up to allow for larger price estimations.

* Radio and slider inputs prevent input data which the model won't recognise.

* The price is displayed when the "get my house price" button is clicked.

### Page 4: Hypothesis

This page lists the null and alternative hypothesis (as per the hypothesis section) and displays  scatter plots of the relationship between a particular feature and SalePrice. The features chosen were based on the most strongly correlated features relevant to each hypothesis and are listed below.

* Hypothesis 1 - GarageArea, GrLivArea and TotalBsmtSF.

* Hypothesis 2 - KitchenQual and OverallQual.

* Hypothesis 3. YearBuilt and YearRemodAdd.

A conclusion section for each explains each relationship.

### Page 5: Peformance (For technical users)

This page provides technical users with 

1. Model Performance
2. ML pipeline & Model.

#### Model Performance.
The performance for each of the train, validation and test sets. We note that the model meets the performance criteria of R2 of at least 0.75.

**Train Set**
R2 Score: 0.841
Mean Absolute Error: 20725.343
Mean Squared Error: 1003982222.455
Root Mean Squared Error: 31454.246

**Validation Set**
R2 Score: 0.841
Mean Absolute Error: 21274.337
Mean Squared Error: 870859719.18
Root Mean Squared Error: 29510.332

**Test Set**
R2 Score: 0.771
Mean Absolute Error:23296.594
Mean Squared Error: 1584495831.166
Root Mean Squared Error: 39805.726


#### ML pipeline & Model

I have included reasoning for some data cleaning as well as feature engineering.

* EnclosedPorch and WoodDeckSF were removed at the start as 90.7% and 89.4% of their respective data is missing. There was too much missing data to reliably impute and it was not possible to impute the missing data from another category.

* The features identified as strongly or very strongly correlated with SalePrice (GarageArea, GrLivArea, KitchenQual, OverallQual, TotalBsmtSF) were extracted from the data set. Other features were dropped.

* The data was split into train, validate and test sets.

* OrdinalCategoricalEncoder was applied to KitchenQual. PowerTransformer was applied to GarageArea, GrLivArea, OverallQual, TotalBsmtSF.

* The data was then Windsorised to cap outliers based on the Inter-Quartile Range (IQR).

* The data was scaled with StandardScaler

**The model**
* The model itself consists of a neural network.

* The input layer is equal to the number of features (i.e. 5).

* This is followed by four hidden layers of 512 nodes, each alternating with a dropout layer set to 0.25.

* Activation functions are all rectified linear unit (ReLU).

* As we created a linear regression model, the output layer consisted of one node, The loss function was Mean Squared Error (MSE). the optimizer was Adam.

## Testing
The following tests were conducted on the streamlit dashboard
| Page | Test | Pass |
| ----: |  ----: | ----: |
| Project Summary | Page renders | ✓ |
| Project Summary | Link to kaggle dataset works | ✓ |
| Project Summary | Link to READMe works | ✓ |
| Project Summary | Project Terms & Jargon displayed | ✓ |
| Project Findings | Page renders | ✓ |
| Project Findings | Most important features dataframe renders | ✓ |
| Project Findings | Combined Pearson and Spearman correlations dataframe renders when box ticked | ✓ |
| Project Findings | Strongly correlated features chart renders | ✓ |
| Predict Sale Price | Page renders | ✓ |
| Predict Sale Price | Inherited house prices predictions dataframe renders | ✓ |
| Predict Sale Price | House price prediction renders when get my house price button clicked | ✓ |
| Predict Sale Price | Users can select all four possible KitchenQual radio buttons | ✓ |
| Predict Sale Price | Users can select all 1 -10 possible OverallQual radio buttons | ✓ |
| Predict Sale Price | Users can select 0 - 3000 on GarageArea slider | ✓ |
| Predict Sale Price | Users can select 0 - 3000 on GarageArea slider | ✓ |
| Predict Sale Price | Users can select 0 - 10,000 on GrLivArea slider | ✓ |
| Predict Sale Price | Users can select 0 - 10,000 on TotalBsmtSF slider | ✓ |
| Project Hypothesis | Page renders | ✓ |
| Project Hypothesis | Hypothesis 1 results shown | ✓ |
| Project Hypothesis | Hypothesis 2 results shown | ✓ |
| Project Hypothesis | Hypothesis 3 results shown | ✓ |
| Project Hypothesis | Graphs renders when boxes ticked | ✓ |
| Technical Information | Page renders | ✓ |
| Technical Information | Up to date R2 scores for train, validate and test set displayed | ✓ |
| Technical Information | Pipeline steps displayed | ✓ |
| Technical Information | Model Information displayed | ✓ |


Note that in particular I tested that the model predictions were in line with the hypothesis. Each feature was tested by increasing and decreasing the rating while other features were kept the same. 


| Feature | Test | Pass |
| ----: |  ----: | ----: |
| KitchenQual | Price prediction increases when rating increases | ✓ |
| KitchenQual | Price prediction decreases when rating decreases | ✓ |
| OverallQual | Price prediction increases when rating increases | No |
| OverallQual | Price prediction decreases when rating decreases | ✓ |
| GarageArea | Price prediction increases when GarageArea size increases | ✓ |
| GarageArea | Price prediction decreases when GarageArea size decreases | ✓ |
| GrLivArea | Price prediction increases when GrLivArea size increases | ✓ |
| GrLivArea | Price prediction decreases when GrLivArea size decreases | ✓ |
| TotalBsmtSF | Price prediction increases when TotalBsmtSF size increases | ✓ |
| TotalBsmtSF | Price prediction decreases when TotalBsmtSF size decreases | ✓ |

* Note that when OverallQual is increased from a rating of 1-2 the price remains static, rather than increasing. This is still in line with the hypothesis. On all other occassions an increase in rating leads to an increase in price. 

## Validation
The below pages have been tested with the Code Institute [PEP8 linter](https://pep8ci.herokuapp.com/) And have no errors

| Page | Pass |
| ----: |  ----: |
| app.py | ✓ |
| src/machine_learning/data_management | ✓ |
| src/machine_learning/predict_house_price.py | ✓ |
| app_pages/multipage.py | ✓ |
| app_pages/predict_sale_price.py | ✓ |
| app_pages/project_findings.py | ✓ |
| app_pages/project_hypothesis.py | ✓ |
| app_pages/project_summary.py | ✓ |
| app_pages/project_technical_information.py | ✓ |

## Unfixed Bugs
There is a dependency issue in the packages in the Code Institute template. The below error message appears when they are installed.  

![](docs/plots/dependency_issue.png)

To resolve this enter `pip install "anyio<4.0" "async-lru<2.0" "rich<10.0"` followed by `pip install twine==3.7.1` to resolve the conflict.

## Deployment
The latest version of the App is deployed on [Heroku](https://heritage-house-9fb9b02e459c.herokuapp.com/)

* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

* You may need to set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.

* To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In your Cloud IDE, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with *Regenerate API Key*.

### To fork

1. Log into Github, or create an account. 

2. Click 'Create fork' and select '+ Create new fork'

3. Once the repo has been created, Click the 'Code' button and copy the URL.

4. Log into the cloud-based IDE with your GitHub account.

5. On your Dashboard, click on the Create button

6. Paste in the URL you copied from GitHub earlier

7. Click Create

8. Wait for the workspace to open. This can take a few minutes.

9. Open a new terminal and `pip3 install -r requirements.txt`

10. You may see the error below:
![](docs/plots/dependency_issue.png)

11. If so enter `pip install "anyio<4.0" "async-lru<2.0" "rich<10.0"` followed by `pip install twine==3.7.1` to resolve the conflict.

12. Open the jupyter_notebooks directory and click on the notebook you want to open.

13. Click the kernel button and choose Python Environments.

Note that the kernel says Python 3.8.18 as it inherits from the workspace so it will be Python-3.8.18 as installed by our template. To confirm this you can use `! python --version` in a notebook code cell.


## Main Data Analysis and Machine Learning Libraries

The below libraries were used in the project. The versions used are in brackets after the name.

* numpy (1.19.2). A library for managing numbers and arrays in Python. Most of the packages below need numpy as a prerequasit.

* pandas (1.1.2). To Convert CSV files and numpy arrays into data frames. 

* matplotlib (3.3.1). To provide data visualisations, including a visualisation of the features which strongly correlate with SalePrice in the streamlit dashboard. Matplotlib offers more customisation than seaborn.

* seaborn (0.11.0). To provide data visualisations, including visualisations showing hypotheses in the streamlit dashboard. Seaborn offers analysts powerful and effective visualisations where no customisation is needed

* streamlit (0.85.0). Was used to create the dashboard.

* feature-engine (1.0.2). OrdinalEncoder, vt.PowerTransformer and Winsorizer were used in the pipeline to encode data prior to training the machine learning model.

* scikit-learn (0.24.2 ). Pipeline and StandardScaler were used in the pipeline to encode data prior to training the machine learning model. The scikit-learn Ordinal Encoder was used to encode categorical data prior to the correlation study.

* tensorflow-cpu (2.6.0) and keras (2.6.0) were used to create a neural network model.

* plotly (4.12.0) was used to create an interactive chart in the project findings page of the dashboard.

* protobuf (3.20) & altair (<5>). Are installed as part of the Code Institute template but not used.


## Credits

### Content

* The business case was taken from [Handbook: Heritage Housing Issues](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PA_PAGPPF+2/courseware/bde016cdbd184cdeafd341a73807e138/bd2104eb84de4e48a9df6f685773cbf2/) from The Code Institute

* This ReadMe was based on [milestone-project-heritage-housing-issues](https://github.com/Code-Institute-Solutions/milestone-project-heritage-housing-issues) from The Code Institute

* Formula for calculating IQR from [How To Find Outliers in Data Using Python (and How To Handle Them)](https://careerfoundry.com/en/blog/data-analytics/how-to-find-outliers/#finding-outliers) by Eric Kleppen in Career Foundry.

* [How to Handle Missing Values of Categorical Variables?](https://www.analyticsvidhya.com/blog/2021/04/how-to-handle-missing-values-of-categorical-variables/) from analyticsvidhya.

* Ordinal Encoding discussion on [Stack Exchange](https://datascience.stackexchange.com/questions/72343/encoding-with-ordinalencoder-how-to-give-levels-as-user-input)

* Pearson correlation vs. Spearman correlation methods from [https://uk.surveymonkey.com/](https://uk.surveymonkey.com/market-research/resources/pearson-correlation-vs-spearman-correlation/)

### Media
* Icon from https://smiley.cool/twitter-emoji.php

## Acknowledgements (optional)

[Hypothesis testing for data scientists](https://towardsdatascience.com/hypothesis-testing-for-data-scientists-everything-you-need-to-know-8c36ddde4cd2)  by Alicia Horsch
What is CRISP DM? By Nick Hotz for Data Science Process Alliance.

I would like to thank my mentor, Mo Shami, encouragement and comments.
