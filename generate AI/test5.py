from transformers import pipeline
sentiment_analyzer=pipeline("sentiment-analysis")
text="kid is very bad and cunning guy"
sentiment=sentiment_analyzer(text)
print("sentiment:",sentiment[0]['label'],"with confidence:",sentiment[0]['score'])