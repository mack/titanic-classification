# TitanicClassification
Classifying whether a passenger will survive on the titanic. This will be my first Kaggle submission.

## Feature selection/Data Preprocessing
I performed feature selection manually on columns that I felt wouldn't contribute to the final prediction, other than add unnecessary noise. These columns were name, ticket, cabin, and embarked.

To perform data preprocessing, I converted the sex label to a numerical label (although I believe this causes issues so I will change it to a onehot label)

## Running PCA on the dataset
Prior to performing PCA, the data was normalized.
These were my results, (1 - Survivors, 0 - Non Survivors)

<p align="center">
  <h3>Results by setting NaN fields to 0.</h3>
  <img src="https://i.imgur.com/B1AAM9B.png" alt="Current"/>
</p>
<p align="center">
  <h3>Dropping rows that contain NaN fields.</h3>
  <img src="https://i.imgur.com/GhERVSc.png" alt="Current"/>
</p>
