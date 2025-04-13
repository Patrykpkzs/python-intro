from textblob import TextBlob

text = "I really love using Python. It's so easy and powerful!"

blob = TextBlob(text)

print("Sentyment:")
print(blob.sentiment)

print("\nRozpoznane części mowy:")
for word, tag in blob.tags:
    print(f"{word:15} - {tag}")
