from transformers import pipeline
ner = pipeline("ner",grouped_entities=True)
text = "Elon usk founded SpaceX and Tesla in the USA."

entities = ner(text)
for entity in entities:
    print(f"{entity['word']} -> {entity['entity_group']}({entity['score']:2f})")