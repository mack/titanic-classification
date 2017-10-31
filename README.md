# TitanicClassification
Classifying whether a passenger will be survive on the titanic. My first Kaggle submission.

## Feature selection/Data Preprocessing
I performed feature selection manually on columns that I felt wouldn't contribute to the final prediction, other than add unnecessary noise. These columns were name, ticket, cabin, and embarked.

To perform data preprocessing, I converted the sex label to a numerical label (although I believe this causes issues so I will change it to a onehot label)

## Running PCA on the dataset
Prior to performing PCA, the data was normalized, and to handle data inconsistency, I filled in all null entries with 0.
This was my result, (1 - Survivors, 0 - Non Survivors)
<p align="center">
  <img src="https://i.imgur.com/B1AAM9B.png" alt="Current"/>
</p>
