# For checking if a word/token is positive or negative -> (5)
class LexiconManager:
    def __init__(self):
        # Initialize positive & negative lexicons
        self.positive_lexicons = self.read_lexicons("positive")
        self.negative_lexicons = self.read_lexicons("negative")

    # Read from sameple data
    def read_lexicons(self, type):
        lexicon_list = []
        file = open(type + "_lexicons.txt", "r")
        for line in file:
            lexicon_list.append(line.replace("\n", ""))
        return lexicon_list

    # Search given token inside lexicons
    def get_polarity(self, token):
        token = token.lower()
        if token in self.positive_lexicons:
            return 1
        elif token in self.negative_lexicons:
            return -1
        else:
            return 0


# For analysing polarity of a sentence -> (2)
class SuperNaiveAnalyzer:
    def __init__(self, test_string):
        # Cleaning up the string when initialized
        self.test_string = self.cleanup(test_string)

    # Removes special character & unnecessary spaces -> (3)
    def cleanup(self, test_string):
        s_char_list = [".", ",", "!", "?", "+", "/", "*", "&", "\n"]
        for schar in s_char_list:
            test_string = test_string.replace(schar, " ")
        return test_string.strip()

    # Determine the polarity of the string -> (4)
    def get_polarity_count(self):
        # Initialize the lexicon manager
        lexicon_manager = LexiconManager()
        positive_count = 0
        negative_count = 0
        # Tokenize the test string
        tokens = self.test_string.split(" ")
        # For each token measure the polarity & keep count
        for token in tokens:
            # Getting polarity for each token and
            # keeping count for respective polarity
            polarity = lexicon_manager.get_polarity(token)
            if polarity == 1:
                positive_count += 1
            elif polarity == -1:
                negative_count += 1
        # Returning the polarity counts
        return {
            "pos": positive_count,
            "neg": negative_count,
            "total": positive_count + negative_count
        }

    # From the polarity count, decide the polarity of the string and
    # based on the count, provide a confidence -> (6)
    def get_result(self):
        count = self.get_polarity_count()
        print("Analysis:-> There were", count["pos"], "positive words &",
              count["neg"], "negative words")
        tag = "Neutral"
        confidence = "100"
        if count["total"] > 0:
            positivity = round(count["pos"] / count["total"] * 100, 1)
            negativity = round(count["neg"] / count["total"] * 100, 1)
            if positivity > negativity:
                tag = "Positive"
                confidence = positivity
            elif negativity > positivity:
                tag = "Negative"
                confidence = negativity
        return (tag, str(confidence) + "%")


# Driver code block -> (0)

# Expect some epic failure if you use reviews.txt
# file = open("../reviews.txt", "r")

# These tests, works moderately
file = open("test.txt", "r")

# Traversing the test line by line
for test_string in file:
    print("[ " + test_string.strip() + " ]")
    # Initializing the super_naive_analyzer with one line -> (1)
    super_naive_analyzer = SuperNaiveAnalyzer(test_string)
    # Getting the result
    result = super_naive_analyzer.get_result()
    # Printing results
    print("Polarity:-> ", result[0])
    print("Confidence:-> ", result[1])
    print("\n")
