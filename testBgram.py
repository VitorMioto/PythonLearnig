import pandas as pd

df = pd.read_csv("https://s3.amazonaws.com/automl-example/produtos.csv", delimiter = ";")
df.dropna(inplace=True)
df["NomeProd"] = df.nome + " " + df.descricao
import nltk
#nltk.download("stopwords")

stopwords = nltk.corpus.stopwords.words("portuguese")

len(stopwords)

from nltk.tokenize import word_tokenize
#nltk.download("punkt")

string = ""
for x in df.NomeProd:
  string = string + " " + x



tokens = word_tokenize(string)
#bgram = nltk.bigrams(tokens)
ngram = nltk.ngrams(tokens,4)

#print(list(bgram))
print(len(list(ngram)))
i= 0
new_token = [word for word in tokens if word not in stopwords]

ngram2 = nltk.ngrams(new_token,4)
print(len(list(ngram2)))