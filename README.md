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

## Random Forest Classifier
Attempt 1.
Using a random forest classifier, I was able to achieve 96% accuracy on the train-split dataset with a 75/25 split. Sadly, I could only get between 0.70 - 0.75 on the test set. It could have been due to the way I preprocessed data and am handling missing values.

Attempt 2.
Tried with more features and received worse results.

## SVC
With a support vector classifier, I was able to get a slight increase of +2% on my kaggle prediction at 77%. I trained it on the training set with NaN values set to their columns mean and the same columns were dropped, as described above.

## Nieve Bayes
Will test soon...

## Neural Network
Will test soon...
