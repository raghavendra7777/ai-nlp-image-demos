from transformers import pipeline

qa = pipeline("question-answering")

context="""Pichai Sundararajan (born June 10, 1972), better known as Sundar Pichai,[a] is an Indian-born American business executive.[3][4] He is the chief executive officer (CEO) of Alphabet Inc. and its subsidiary Google.[5]

"""

question = "what are some generative ai models?"
answer = qa(question=question, context=context)
print("Answer:",answer['answer'])