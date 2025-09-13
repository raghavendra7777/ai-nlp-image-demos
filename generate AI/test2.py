from transformers import pipeline
summarizer = pipeline("summarization",model="facebook/bart-large-cnn")

text="""Alexander was born in 356 bce in Pella, Macedonia, the son of King Philip II and Queen Olympias. In his early teens he became a pupil of Aristotle, who sparked his interest in philosophy and science. However, it was in military affairs that he excelled. In a war against the allied Greek states, 18-year-old Alexander led a cavalry charge that helped Philip win the conflict. In 336 Philip was assassinated. Alexander was acclaimed by the army and succeeded to the throne without opposition. He inherited a highly trained, mobile military force and his father’s dream of conquering the Persian empire.
"""
summary=summarizer(text, max_length=50, min_length=25, do_sample=False)
print("summarizer:",summary[0]['summary_text'])