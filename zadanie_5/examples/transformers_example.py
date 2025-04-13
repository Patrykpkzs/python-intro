from transformers import pipeline

# Ładowanie gotowego pipeline do analizy sentymentu
classifier = pipeline("sentiment-analysis")

text = "I absolutely love working with Python!"
result = classifier(text)[0]

print("Wynik analizy sentymentu:")
print(f"Label: {result['label']}, Score: {result['score']:.2f}")