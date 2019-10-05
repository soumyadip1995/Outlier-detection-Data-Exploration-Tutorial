## Outlier-detection-Data-Exploration-Tutorial

### Definition - What does Outlier Detection mean?
Outlier detection is the process of detecting and subsequently excluding outliers from a given set of data.

An outlier may be defined as a piece of data or observation that deviates drastically from the given norm or average of the data set. An outlier may be caused simply by chance, but it may also indicate measurement error or that the given data set has a heavy-tailed distribution.

### What is this Tutorial all about ?

I have designed this tutorial to give you, the reader a brief introduction to the overview of Exploratory Data Analysis, Outlier detection and Feature Engineering. After completion of this tutorial, I hope you will gain some insight as to how outlier detection is done, why it is necessary when it comes to learning. Why we perform Exploratory data analysis and the necessity of Feature Engineering. I have included a real life example of Exploratory data analysis on the Airbnb dataset of Austin,Texas. This will definitely help you gain a better insight. 

### How is the Tutorial designed ?

The tutorial begins with the concepts that are necessary when it comes to knowing how to perform outlier detection. The ways to perform Outlier detection, Treating Missing values and Feature Engineering. Finally, we arrive at the Exploratory data Analysis on the Airbnb dataset of Austin, Texas ending with data preprocessing and Feature Engineering. While approaching the tutorial, make sure you go through the concepts first before arriving to the airbnb_austin_texas notebook. Everything is rendered on nbviewer. So, sit down with a pen and paper and try to work everything out. It will take you a few hours..!!. All the ipynb notebooks are avaiable for download and you can run it on your own on colab and jupyter. I have also included the dataset for Airbnb, Austin TX.

### Table of contents
#### Outlier Detection, Data Exploration and Feature Engineering
- [Data Exploration, Outlier detection, Feature Engineering,What is an Outlier?](https://nbviewer.jupyter.org/gist/soumyadip1995/fe7049614cfc594a9e3f09a699c8dd7f#Data-Exploration,-Outlier-detection,-Feature-Engineering)
- [Angle-Based Outlier Detection (ABOD) and KNN](https://nbviewer.jupyter.org/gist/soumyadip1995/fe7049614cfc594a9e3f09a699c8dd7f#Angle-Based-Outlier-Detection-(ABOD)-and-KNN)
- 5 ways to detect anomalies
  - [Standard Deviation,Isolation Forest,DBScan,Boxplots](https://nbviewer.jupyter.org/gist/soumyadip1995/fe7049614cfc594a9e3f09a699c8dd7f#5-ways-to-detect-anomalies)
  - [Robust Random Cut Forest (RRCF)](https://nbviewer.jupyter.org/gist/soumyadip1995/fe7049614cfc594a9e3f09a699c8dd7f#Robust-Random-Cut-Forest-(RRCF))
  - [Creating the tree,Inserting point, Deleting point](https://nbviewer.jupyter.org/gist/soumyadip1995/fe7049614cfc594a9e3f09a699c8dd7f#Creating-the-tree)
- [Robust Random Cut Forest code..!!!](https://nbviewer.jupyter.org/gist/soumyadip1995/fe7049614cfc594a9e3f09a699c8dd7f#Robust-Random-Cut-Forest-code..!!!)
- [Treating Missing values](https://nbviewer.jupyter.org/gist/soumyadip1995/fe7049614cfc594a9e3f09a699c8dd7f#Treating-Missing-values)
  - [Univariate Analysis,Bi-variate Analysis](https://nbviewer.jupyter.org/gist/soumyadip1995/fe7049614cfc594a9e3f09a699c8dd7f#Univariate-Analysis)
  - [Chi-square Test(Categorical and categorical)](https://nbviewer.jupyter.org/gist/soumyadip1995/fe7049614cfc594a9e3f09a699c8dd7f#Chi-square-Test(Categorical-and-categorical))
  - [Code for chi-square test..!!!](https://nbviewer.jupyter.org/gist/soumyadip1995/fe7049614cfc594a9e3f09a699c8dd7f#Code-for-chi-square-test..!!!)
- [Types of Combinations](https://nbviewer.jupyter.org/gist/soumyadip1995/fe7049614cfc594a9e3f09a699c8dd7f#Types-of-Combinations)
- [Feature Engineering](https://nbviewer.jupyter.org/gist/soumyadip1995/fe7049614cfc594a9e3f09a699c8dd7f#Feature-Engineering)

Full jupyter notebook is [here](https://nbviewer.jupyter.org/gist/soumyadip1995/fe7049614cfc594a9e3f09a699c8dd7f)


### Exploratory data analysis on the Airbnb dataset of Austin,TX.
- [Exploring & Machine Learning for Airbnb Listings in Austin,Texas](https://nbviewer.jupyter.org/gist/soumyadip1995/2d0abb2e814aa3ad8289674b52b07d0d#Exploring-&-Machine-Learning-for-Airbnb-Listings-in-Austin,Texas)
  - [Calender](https://nbviewer.jupyter.org/gist/soumyadip1995/2d0abb2e814aa3ad8289674b52b07d0d#Calender)
  - [Neighbourhood Listings, review score rating,Exploring the price,Listings price distribution after removing outliers](https://nbviewer.jupyter.org/gist/soumyadip1995/2d0abb2e814aa3ad8289674b52b07d0d#Neighbourhood-Listings)
  - [Neighbourhood vs price, host vs price, property type vs price, room type vs price, bed type vs price](https://nbviewer.jupyter.org/gist/soumyadip1995/2d0abb2e814aa3ad8289674b52b07d0d#Neighbourhood-vs.-Price)
  - [Amenities, Top 20 most common amenities, Amenities vs. price top 20, Number of beds vs price](https://nbviewer.jupyter.org/gist/soumyadip1995/2d0abb2e814aa3ad8289674b52b07d0d#Amenities)
  - [Numeric Features](https://nbviewer.jupyter.org/gist/soumyadip1995/2d0abb2e814aa3ad8289674b52b07d0d#Numeric-features)
 - [Modeling Listing Prices, data preprocessing and Feature Engineering](https://nbviewer.jupyter.org/gist/soumyadip1995/2d0abb2e814aa3ad8289674b52b07d0d#Modeling-Lising-Prices)
 - [Random Forest Regressor](https://nbviewer.jupyter.org/gist/soumyadip1995/2d0abb2e814aa3ad8289674b52b07d0d#Random-Forest-Regressor)
 - [Feature importance of Random Forest, Assessing the Fit of Regression Models, R square and Adjusted R square](https://nbviewer.jupyter.org/gist/soumyadip1995/2d0abb2e814aa3ad8289674b52b07d0d#Feature-importance-of-Random-Forest)
 - [F-Test, RMSE](https://nbviewer.jupyter.org/gist/soumyadip1995/2d0abb2e814aa3ad8289674b52b07d0d#The-F-test)
 - [LightGBM](https://nbviewer.jupyter.org/gist/soumyadip1995/2d0abb2e814aa3ad8289674b52b07d0d#LightGBM)
 - [Feature importance of LightGBM](https://nbviewer.jupyter.org/gist/soumyadip1995/2d0abb2e814aa3ad8289674b52b07d0d#Feature-importance-of-LightGBM)
 
 The full Jupyter Notebook is [here](https://nbviewer.jupyter.org/gist/soumyadip1995/2d0abb2e814aa3ad8289674b52b07d0d)
 
 ### Credits
