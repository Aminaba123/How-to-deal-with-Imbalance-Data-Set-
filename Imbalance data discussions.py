the class weights are used to tell your model how important a class is. That means that during the training, 
the classifier will make extra efforts to classify properly the classes with high weights.
How they do that is algorithm-specific. If you want details about how it works for SVC and the doc does not make sense to you, 
feel free to mention it.

# The metrics

Once you have a classifier, you want to know how well it is performing. Here you can use the metrics you mentioned:
accuracy, recall_score, f1_score...

Usually when the class distribution is unbalanced,
accuracy is considered a poor choice as it gives high scores to models which just predict the most frequent class.

as you can see in this print of a classification report they are defined for each class.
They rely on concepts such as true positives or false negative that require defining which class is the positive on

Take the average of the f1-score for each class: that's the avg / total result above. It's also called macro averaging.
Compute the f1-score using the global count of true positives / false negatives,
etc. (you sum the number of true positives / false negatives for each class). Aka micro averaging.

Compute a weighted average of the f1-score. Using 'weighted' in scikit-learn will weigh the f1-score by the support of the class:
the more elements a class has, the more important the f1-score for this class in the computation.

Which one you choose is up to how you want to measure the performance of the classifier: for instance macro-averaging does not take 
class imbalance into account and the f1-score of class 1 will be just as important as the f1-score of class 5. 
If you use weighted averaging however you'll get more importance for the class 5.

Last thing I want to mention (feel free to skip it if you're aware of it) is that scores are only meaningful
if they are computed on data that the classifier has never seen. This is extremely important as any score
you get on data that was used in fitting the classifier is completely irrelevant.

Here's a way to do it using StratifiedShuffleSplit, 
which gives you a random splits of your data (after shuffling) that preserve the label distribution.

 there are two concerns:
the class weights are used to tell your model how important a class is. That means that during the training, 
the classifier will make extra efforts to classify properly the classes with high weights.
How they do that is algorithm-specific. If you want details about how it works for SVC and the doc does not make sense to you, 
feel free to mention it.

# The metrics

Once you have a classifier, you want to know how well it is performing. Here you can use the metrics you mentioned:
accuracy, recall_score, f1_score...

Usually when the class distribution is unbalanced,
accuracy is considered a poor choice as it gives high scores to models which just predict the most frequent class.

as you can see in this print of a classification report they are defined for each class.
They rely on concepts such as true positives or false negative that require defining which class is the positive on

Take the average of the f1-score for each class: that's the avg / total result above. It's also called macro averaging.
Compute the f1-score using the global count of true positives / false negatives, etc.
(you sum the number of true positives / false negatives for each class).
Aka micro averaging.
Compute a weighted average of the f1-score. Using 'weighted' in scikit-learn will weigh the f1-score by the support of the class:
the more elements a class has, the more important the f1-score for this class in the computation.

Which one you choose is up to how you want to measure the performance of the classifier: for instance macro-averaging does not take 
class imbalance into account and the f1-score of class 1 will be just as important as the f1-score of class 5. 
If you use weighted averaging however you'll get more importance for the class 5.

Last thing I want to mention (feel free to skip it if you're aware of it) is that scores are only meaningful
if they are computed on data that the classifier has never seen. This is extremely important as any score
you get on data that was used in fitting the classifier is completely irrelevant.

Here's a way to do it using StratifiedShuffleSplit, 
which gives you a random splits of your data (after shuffling) that preserve the label distribution.

there are two concerns:

How to I score a multiclass problem?
How do I deal with unbalanced data?

you can tell if the unbalanced data is even a problem. If the scoring for the less represented classes (class 1 and 2)
are lower than for the classes with more training samples (class 4 and 5) then you know that the unbalanced data is in fact a problem,
and you can act accordingly, as described in some of the other answers in this thread.
However, if the same class distribution is present in the data you want to predict on,
your unbalanced training data is a good representative of the data, and hence, the unbalance is a good thing.

what metric should be used for multi-class classification with imbalanced data?

Macro-F1-measure

Macro Precision and Macro Recall can be also used, but they are not so easily interpretable as for binary classificaion,
they are already incorporated into F-measure, and excess metrics complicate methods comparison, parameters tuning, and so on.

Micro averaging are sensitive to class imbalance: if your method, for example, works good for the most common labels and totally messes others,
micro-averaged metrics show good results

Weighting averaging isn't well suited for imbalanced data, because it weights by counts of labels. Moreover, 
it is too hardly interpretable and unpopular: for instance, there is no mention of such an averaging in the following 
very detailed survey I strongly recommend to look through

                              
















