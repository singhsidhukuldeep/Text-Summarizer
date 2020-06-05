from summarizer import Summarizer


class SummarizerBERT:
    """
    BERT text summarizer
    :param max_length: The maximum length to accept as a sentence. (default to 500)
    :param min_length: The minimum length to accept as a sentence. (default to 25)
    :param use_first: Importance of first sentence
    :param ratio: Ratio of sentences to summarize to from the original body. (default to 0.2)
    :param model: Model to be used (default to bert-large-uncased)
    :param clustering_algorithm: Which clustering algorithm to use (default to kmeans options kmeans OR gmm)
    All models available:
    'bert-base-uncased': (BertModel, BertTokenizer),
    'bert-large-uncased': (BertModel, BertTokenizer),
    'xlnet-base-cased': (XLNetModel, XLNetTokenizer),
    'xlm-mlm-enfr-1024': (XLMModel, XLMTokenizer),
    'distilbert-base-uncased': (DistilBertModel, DistilBertTokenizer),
    'albert-base-v1': (AlbertModel, AlbertTokenizer),
    'albert-large-v1': (AlbertModel, AlbertTokenizer)
    """
    def __init__(self, max_length=500, min_length=25, use_first=False, ratio=0.2, model="bert-large-uncased",
                 clustering_algorithm='kmeans'):
        self.max_length = max_length
        self.min_length = min_length
        self.use_first = use_first
        self.ratio = ratio
        self.model = model
        self.clustering_algorithm = clustering_algorithm

    def summary(self, text=''):
        """
        This returns the summary of the text using BERT Transformer
        :param text: Text to be summarized
        :return: Summarized Text
        """
        model = Summarizer(self.model)
        return model(text, min_length=self.min_length, max_length=self.max_length, use_first=self.use_first,
                     ratio=self.ratio, algorithm=self.clustering_algorithm)
