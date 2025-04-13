# Laboratorium 5 – Przetwarzanie języka naturalnego w Pythonie

## Temat: Analiza tekstu z użyciem bibliotek NLP

W ramach laboratorium postanowiłem przyjrzeć się dwóm popularnym bibliotekom z dziedziny przetwarzania języka naturalnego (NLP): **transformers** oraz **TextBlob**. Oferują one różne poziomy zaawansowania i mają ciekawe zastosowania, takie jak analiza sentymentu, rozpoznawanie części mowy czy ekstrakcja nazw własnych.

---

## 1. Biblioteka: `transformers`

### 📌 Opis:
`transformers` to biblioteka stworzona przez Hugging Face. Umożliwia korzystanie z potężnych modeli językowych (jak BERT, RoBERTa, GPT). Wymaga `torch` lub `tensorflow`.

### 🧪 Przykład użycia: `examples/transformers_example.py`

## 2. Biblioteka: `TextBlob`

### 📌 Opis:
`TextBlob` to prosta w użyciu biblioteka NLP zbudowana na bazie nltk i pattern. Umożliwia szybkie przetwarzanie tekstu – np. analizę sentymentu, tłumaczenie lub rozpoznawanie części mowy.

### 🧪 Przykład użycia: `examples/textblob_example.py`

## Instrukcja:
1. Utwórz środowisko wirtualne Python (.venv)
2. Aktywuj środowisko
	`.venv\Scripts\activate`
3. Zainstaluj wymagane biblioteki:
	`pip install textblob`
	`python -m textblob.download_corpora`
	`pip install transformers`
    `pip install torch`
4. Możesz uruchomić kod.