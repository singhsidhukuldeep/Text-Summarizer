from transformers import pipeline


class SummarizerT5BART:
    """
    BART or T5 text summarizer
    :param model: select the model that you want to use as model in summarization pipeline (default is t5-small)
    :param max_length: The maximum length to accept as a sentence. (default to 20)
    :param min_length: The minimum length to accept as a sentence. (default to 5)
    Supported models:
    facebook/bart-large-cnn
    t5-11b
    t5-3b
    t5-base
    t5-large
    t5-small
    Warning: for T5 you can chose the size of the model. Everything above t5-base is very slow, even on GPU or TPU
    """

    def __init__(self, model='t5-small', min_length=5, max_length=20):
        self.model = model
        self.min_length = min_length
        self.max_length = max_length

    def summary(self, text=''):
        """
        This returns the summary of the text using BERT Transformer
        :param text: Text to be summarized
        :return: Summarized Text
        """
        summarizer = pipeline(task='summarization', model=self.model)
        return summarizer(text, max_length=self.max_length, min_length=self.min_length)[0]['summary_text']
