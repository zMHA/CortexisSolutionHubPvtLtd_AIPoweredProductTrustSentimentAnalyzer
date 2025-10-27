from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(reviews):
    results = []
    for text in reviews:
        res = sentiment_model(text[:512])[0]
        label = res["label"]
        score = res["score"]
        if score < 0.6:
            label = "NEUTRAL"
        results.append({"text": text, "label": label, "score": score})
    return results
