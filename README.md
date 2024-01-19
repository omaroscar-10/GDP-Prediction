## QUANTIFYING THE IMPACT OF GDP GROWTH ON ACHIEVING A 70-YEAR LIFE EXPECTANCY IN SUB-SAHARAN AFRICA ​
Group members: Omar Aguirre, Jorge Martinez, Matthew Rand, Shameema Shahulhameed

## Description
This project uses a wide arrange of data from the World Bank, the World Health Organization (WHO), and World Development Indicators (WDI) to determine the required level of Gross Domestic Product (GDP) that a sub-Saharan African nation must attain for the average life expectancy in their country to reach the world median of 70 years of age. Our mission is to provide a roadmap for informed policymaking, helping to elevate average life expectancy while considering factors like emissions, economic activity, financial transactions, and healthcare access.

Previous literature noted that GDP and life expectancy were positively linked, and established a correlation between the variables across the globe. The literature also noted that increases in those variables are likely the result of intermediary variables, such as access to health care and infant mortality. As such, we attempted to determine a set of key intermediary variables with predictive power for both attributes and built a predictive linear regression model based on those variables, as a means of targeting key investment opportunities to improve both life expectancy and GDP.

We source data from reputable organizations such as the World Bank, the World Health Organization (WHO), and World Development Indicators (WDI). This data encompasses GDP, life expectancy, health-related variables, and environmental factors, forming the foundation of our analysis. We decided to use the World Development Indicators (WDI) dataset, encompassing the entire regiono from 1985 to 2022. It can be found under the **data** folder in the main project directory or at the following URL: https://databank.worldbank.org/source/world-development-indicators# 

## Installation
To install the project, clone the Github repository to your local machine. This can be accomplished via HTTPS or via CLI.

##### Clone the repository via HTTPS
https://github.gatech.edu/CSE-6242-Fall-23/6242-Project.git 

##### Clone the repository via CLI
```
gh repo clone github.gatech.edu/CSE-6242-Fall-23/6242-Project
```

##### Navigate to the project directory
```
cd your-repository
```

Once complete, it is recommended that a virtual environment be created within the project directory. Open a bash terminal from within the project directory.

##### Create virtual environment
```
python -m venv venv
```

##### Activate the virtual environment
On Windows: 
```
.\venv\Scripts\activate
```
On macOS and Linux: 
```
source venv/bin/activate
```

##### Install dependencies into the virtual environment
```
pip install -r requirements.txt
```

You are now ready to run the project.

Once complete, deactivate the virtual environment from the bash terminal.

##### Deactivate
```
deactivate
```

## Execution

##### Data Preprocessing
To prepare the data for modeling run the following file:

```
python Data_Preprocessing.ipynb
```

The notebook is structured into different sections, including data cleaning, feature selection, model development, and evaluation for GDP and Life Expectancy. Furthermore, the notebook provides evaluations of model performance and feature importance, and concludes with identifying overlapping predictors significant for both GDP and Life Expectancy. 

##### Exploratory Data Analysis
Exploratory Data Analysis (EDA) for all Sub-Saharan countries can be explored by executing the following command from the home directory:
```
bash Code pythonEDA.ipynb
```

This generates an HTML report (EDA_report.html) offering insights for all countries int he region. The report includes details on data types, missing values, summary statistics, and visualizations, providing a comprehensive understanding of the dataset.

##### Predictive Model
The predictive model for determining the required Gross Domestic Product (GDP) to achieve a 70-year life expectancy is available in the Jupyter NOtebook file: Data_Preprocessing_Modeling_Final.ipynb

All project results, including tree maps, are provided in two Jupyter Notebook files:
TreemapVisual.ipynb and
GDPVisualization.ipynb

##### Visualizations
To explore the data, execute the following code from the command line.

```
python visualizations.py
```

The Dash app will be served on your local host,  http://127.0.0.1:8050/ or similar. Navigate to this address in your browser of choice to view the data.

![alt text](https://github.gatech.edu/CSE-6242-Fall-23/6242-Project/blob/7df55db64216dda79796325f00adc2b7895fe7db/visuals/updated_choropleth.png)

Within the application, you will be presented with a slider where the user can select a year to visualize and an interactive choropleth map of Subsaharan Africa. The nation's will be color-coded based on the life expectancy for the selected year. Once a country is clicked on, a boxplot will appear below the choropleth that depicts 12 variables that were found to be significant to predicting both Life Expectancy and GDP per capita. The box plot shows the general distribution of the data across all of Subsaharan Africa, and will show a colored dot corresponding to the relative position of the selected country.
