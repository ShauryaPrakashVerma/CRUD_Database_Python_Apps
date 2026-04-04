import nlpcloud


def ner(text_input):
   
    client = nlpcloud.Client("gpt-oss-120b", "<API-Key>", gpu=True)
    client.sentiment(
        text_input,
        target="NLP Cloud"
)