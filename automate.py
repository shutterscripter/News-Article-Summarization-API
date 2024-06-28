from model.summarization_model import TextSummarizationModel, create_text_summarization_model


summarization_model = create_text_summarization_model()

def summarize_article(article_text: str):
    # summarizer = TextSummarizationModel()
    return summarization_model.summarize(article_text)