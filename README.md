# Machine Learning
## Property Price Prediction & Recommendation System 
### 1. Tools & Requirements
1. Python Programming Language
2. Google Colaboratory
3. Tensorflow
4. Python Libraries (Numpy, Pandas, Seaborn, Matplotlib, Keras, Scikit-learn)

### 2. Datasets
We are taking 2 datasets from kaggle links below:
1. https://www.kaggle.com/datasets/wisnuanggara/daftar-harga-rumah
2. https://www.kaggle.com/datasets/nafisbarizki/daftar-harga-rumah-jabodetabek

We have already cleaned and organized the data using Microsoft Excel from both datasets (remove irrelevant values, handle missing values, check duplicates, handle outliers, and check data types), so we obtained a total of 4500+ listings of properties data in the Jabodetabek area.

### 3. Pre-processing
We have performed data cleaning in Microsoft Excel, combined datasets in Google Colab, and implemented data visualization as well. We also used the IQR method and split the data into input and output for a more in-depth analysis. In addition, we evaluated metrics and applied three models to determine the most suitable accuracy.

### 4. Model & Deployment
1. Price Prediction: Convolutional Neural Network / Linear Regression, Random Forest, AdaBoost
2. Recommendation system: Cosine Similarity / K-Nearest Neighbor
3. Deployment: Mobile / Google Cloud API
