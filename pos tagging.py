from collections import Counter
import nltk
#text=input("Enter your input:")

#text = "Wordembedding is a feature learning technique in which each word or phrase from the vocabulary is mapped to a N dimension vector of real numbers. Various word embedding methods have been proposed to translate unigrams into understandable input for machine learning algorithms"
f=open("sample.txt", "r")
if f.mode == 'r':
    text =f.read()
print(text)

lower_case = text.lower()
tokens = nltk.word_tokenize(lower_case)
tags = nltk.pos_tag(tokens)
counts = Counter( tag for word,  tag in tags)
print(counts)
words = nltk.tokenize.word_tokenize(text)
fd = nltk.FreqDist(words)
fd.plot()
Tokens = nltk.word_tokenize(text)
output = list(nltk.trigrams(Tokens))
print(output)
