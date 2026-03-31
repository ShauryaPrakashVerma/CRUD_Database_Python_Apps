import nlpcloud


class API:
    
    def sentiment_response(self, text):
        client = nlpcloud.Client("gpt-oss-120b", "<API Key>", gpu=True)
        # response = client.sentiment(
        #     text,
        #     target="NLP Cloud"
        # )
        response = {'scored_labels': [{'label': 'POSITIVE', 'score': 1}, {'label': 'joy', 'score': 1}]}
        return response["scored_labels"]