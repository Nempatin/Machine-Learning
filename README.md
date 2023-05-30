# Machine Learning
## Property Price Prediction & Recommendation System 
### 1. Tools & Requirements
1. Python Programming Language
2. Google Colaboratory
3. Tensorflow
4. Python Libraries (Numpy, Pandas, Seaborn, Matplotlib, Keras, Scikit-learn)
### 2. Datasets
Source of our Indonesia property datasets:
1. https://www.kaggle.com/datasets/wisnuanggara/daftar-harga-rumah
2. https://www.kaggle.com/datasets/nafisbarizki/daftar-harga-rumah-jabodetabek
3. https://www.kaggle.com/datasets/rafliaping/dataset-harga-rumah-bandung

The total of our datasets is 8,072 datasets of listing property

### 3. Pre-processing

1. Data Cleaning: This step involves identifying and handling missing data, duplicate data, or invalid data. This could include deleting irrelevant rows or columns, filling in missing values using a certain method, or removing duplicate entries.

2. Data Transformation: At this stage, the data is transformed or formatted to make it more suitable for the machine learning model to be used. Examples of data transformations include normalizing (scaling data to a certain range), standardizing (converting the distribution of data to a normal distribution), or encoding categorical variables into numerical representations.

3. Feature Selection: This process involves selecting the most relevant subset of features from the available data. The purpose of feature selection is to reduce data dimensions and improve model quality, as well as reduce the tendency of overfitting. Commonly used methods include correlation analysis, model-based selection, or information-based methods such as Information Gain or Mutual Information.

4. Feature Engineering: This step involves creating new features that can improve data representation or reveal more useful information to the model. These features can be a mathematical transformation of existing features, data aggregation, or combining existing features to create new, more informative features.

5. Data Splitting: This process involves dividing data into training subsets, validation subsets, and test subsets. The training subset is used to train the model, the validation subset is used to evaluate the performance of the model during development, and the test subset is used to test the performance of the model that has been trained.
### 4. Model & Deployment
Model = Logistic Regression 

Deployment = google cloud
