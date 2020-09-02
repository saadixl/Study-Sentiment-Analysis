from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


class SvmAnalyzer:
    def __init__(self):
        # read train Data
        trainData = pd.read_csv("train.csv")

        # Initialize the vectorizer
        self.vectorizer = TfidfVectorizer(min_df=5,
                                          max_df=0.8,
                                          sublinear_tf=True,
                                          use_idf=True)

        # Create train vector using vectorizer
        train_vectors = self.vectorizer.fit_transform(trainData['Content'])

        # Create a classification model
        self.classifier_linear = svm.SVC(kernel='linear')

        # Fit train data inside model
        self.classifier_linear.fit(train_vectors, trainData['Label'])

    def get_result(self, test_String):
        # Initialize test vector using vectorizer
        test_vector = self.vectorizer.transform([review])
        # Predict the polarity using the test vectory
        # NOTE THAT WE TAGGED neg/pos THAT'S WHY WE ARE CALLING IT POLARITY
        # IT CAN BE OTHER FEATURES OR EMOTIONS
        polarity = self.classifier_linear.predict(test_vector)
        # Get tyhe confidence of the polarity
        confidence = self.classifier_linear.decision_function(test_vector)
        # Returning as a tuple
        return (polarity[0], confidence[0])


# Initializing the svm analyzer
svm_analyzer = SvmAnalyzer()
file = open("../reviews.txt", "r")
# Traversing the input line by line
for review in file:
    # Get result for  each review
    result = svm_analyzer.get_result(review)
    print("\n[ " + review.strip() + " ]")
    print("Polarity:-> ", result[0])
    print("Confidence:-> ", result[1])
