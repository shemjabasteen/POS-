# POS-
  Parts of speech Tagging is responsible for reading the text in a language and assigning some specific token (Parts of Speech) to each word.
e.g.
Input: Everything to permit us.
Output: [('Everything', NN),('to', TO), ('permit', VB), ('us', PRP)]
Steps Involved:

    Tokenize text (word_tokenize)
    Apply pos_tag to above step that is nltk.pos_tag(tokenize_text) 
    POS tagger is used to assign grammatical information of each word of the sentence. Installing, Importing and downloading all the packages of NLTK is complete.

Elaboration of the code :

          To count the tags, you can use the package Counter from the collection's module. A counter is a dictionary subclass which works on the principle of key-value operation. It is an unordered collection where elements are stored as a dictionary key while the count is their value.
         Import nltk which contains modules to tokenize the text.
         Write the text whose pos_tag you want to count.
        Some words are in upper case and some in lower case, so it is appropriate to transform all the words in the lower case before applying tokenization.
        Pass the words through word_tokenize from nltk.
         Calculate the pos_tag of each token
      Now comes the role of dictionary counter. We have imported in the code line 1. Words are the key and tags are the value and counter will count each tag total count present in the text. 

Frequency Distribution
         Frequency Distribution is referred to as the number of times an outcome of an experiment occurs. It is used to find the frequency of each word occurring in a document. It uses FreqDistclass and defined by the nltk.probabilty module.

Explanation of code:

    Import nltk module.
    Write the text whose word distribution you need to find.
    Tokenize each word in the text which is served as input to FreqDist module of the nltk.
    Apply each word to nlk.FreqDist in the form of a list
    Plot the words in the graph using plot() 
   Collocations: Bigrams and Trigrams
     Collocations are the pairs of words occurring together many times in a document. It is calculated by the number of those pair occurring    together to the overall word count of the document.
     
  Collocation can be categorized into two types-

    Bigrams combination of two words
    Trigramscombinationof three words 

 




