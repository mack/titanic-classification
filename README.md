# TitanicClassification
Classifying whether a passenger will survive on the titanic. This will be my first Kaggle submission.

## Log
I'm beginning to keep a log of my progress each day.
#### Nov 6th
I then ran several classification algorithms (naive bayes, SVC, random forest), which I thought would perform well on a small dataset. The all gave varying results... ranging from 0.40 - 0.77 on the test sets accuracy.

I believe that one issue that I'm running into is how to handle missing data. The only two approaches I've tried were setting NaN values to 0 or setting them to their columns mean. After further inspection, I realized that 20% of the test set contains NaN values so I believe that is where I'm running into problems.

What is my solution? Well from researching online, I've found that I can use linear regression, KNN, and other means to predict the values of missing fields.

After testing with KNN to impute missing values on the test set, I was able to achieve... a whopping 74%! -3% than my best score... I guess I'll keep on trying.

### Nov 7th
... will update


## Feature Extraction/Data Preprocessing
In regards to data preprocessing, I selected several columns that I felt would provide meaningful data to our classification algorithm.

I selected the following features
* Pclass
* Sex
* Age
* Fare_Per_Person


## Running PCA on the dataset
<sub>Using almost all of the columns</sub><br>
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

## Naive Bayes
Tested with bernoulli naive bayes and the results were around 76% on kaggle so I achieved about the same.

## Neural Network
Will test soon...
