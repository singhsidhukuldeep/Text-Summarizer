try:
    import nltk
    nltk.download('stopwords')
    nltk.download('punkt')
except Exception as exp:
    print(f" ERROR {exp}")
    raise Exception("NLTK download failed")
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx


class SummarizerNLTK:
    """
    NLTK text summarizer
    :param max_length: This is the maximum number of sentences in the summary
    :param min_length: This is the minimum number of sentences in the summary. (Not being considered right now)
    """
    def __init__(self, max_length=2, min_length=1):
        self.max_length = max_length
        self.min_length = min_length

    def read_text(self, data=""):
        data = [data]
        article = data[0].split(". ")
        sentences = []

        for sentence in article:
            # print(sentence)
            sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
        sentences.pop()

        return sentences

    def sentence_similarity(self, sent1, sent2, stopwords=None):
        if stopwords is None:
            stopwords = []

        sent1 = [w.lower() for w in sent1]
        sent2 = [w.lower() for w in sent2]

        all_words = list(set(sent1 + sent2))

        vector1 = [0] * len(all_words)
        vector2 = [0] * len(all_words)

        # build the vector for the first sentence
        for w in sent1:
            if w in stopwords:
                continue
            vector1[all_words.index(w)] += 1

        # build the vector for the second sentence
        for w in sent2:
            if w in stopwords:
                continue
            vector2[all_words.index(w)] += 1

        return 1 - cosine_distance(vector1, vector2)

    def build_similarity_matrix(self, sentences, stop_words):
        # Create an empty similarity matrix
        similarity_matrix = np.zeros((len(sentences), len(sentences)))

        for idx1 in range(len(sentences)):
            for idx2 in range(len(sentences)):
                if idx1 == idx2:  # ignore if both are same sentences
                    continue
                similarity_matrix[idx1][idx2] = self.sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

        return similarity_matrix

    def summary(self, text=''):
        """
        This returns the summary of the text using NLTK corpus and sentence ranking
        :param text: Text to be summarized
        :return: Summarized Text
        """
        stop_words = stopwords.words('english')
        summarize_text = []

        # Step 1 - Read text anc split it
        sentences = self.read_text(data=text)

        # Step 2 - Generate Similary Martix across sentences
        sentence_similarity_martix = self.build_similarity_matrix(sentences, stop_words)

        # Step 3 - Rank sentences in similarity martix
        sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
        scores = nx.pagerank(sentence_similarity_graph)

        # Step 4 - Sort the rank and pick top sentences
        ranked_sentence = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
        # print("Indexes of top ranked_sentence order are ", ranked_sentence)

        for i in range(self.max_length):
            summarize_text.append(" ".join(ranked_sentence[i][1]))

        # Step 5 - Off course, output the summarize text
        return ". ".join(summarize_text)
