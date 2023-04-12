# Intermediate level
'''
Modify the following program to print out the tf-idf values for each document and each word. The following code calculates the tf and 
df values, so you'll just need to combine them according to the correct formula. There are three documents (sentences) and a total of 
eight terms (unique words), so the output should be three lists of eight tf-idf values each.
'''
# DATA BLOCK
import math

text = '''he really really loves coffee
my sister dislikes coffee
my sister loves tea'''

def main(text):
    # split the text first into lines and then into lists of words
    docs = [line.split() for line in text.splitlines()]

    N = len(docs)

    # create the vocabulary: the list of words that appear at least once
    vocabulary = list(set(text.split()))

    df = {}
    tf = {}
    for word in vocabulary:
        # tf: number of occurrences of word w in document divided by document length
        # note: tf[word] will be a list containing the tf of each word for each document
        # for example tf['he'][0] contains the term frequence of the word 'he' in the first
        # document
        tf[word] = [doc.count(word)/len(doc) for doc in docs]

        # df: number of documents containing word w
        df[word] = sum([word in doc for doc in docs])/N

    # loop through documents to calculate the tf-idf values
    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            # ADD THE CORRECT FORMULA HERE. Remember to use the base 10 logarithm: math.log(x, 10)
            t = tf[word][doc_index] * math.log(1/df[word], 10)
            tfidf.append(t) 

        print(tfidf)
        print(len(vocabulary))

main(text)
print('#################################')

# Advanced level
'''
Let's combine two tasks: finding the most similar pair of lines and the tf-idf representation.

Write a program that uses the tf-idf vectors to find the most similar pair of lines in a given data set. You can test your 
solution with the example text below. Note, however, that your solution will be tested on other data sets too, so make sure 
you don't make use of any special properties of the example data (like there being four lines of text).

This exercise requires a bit more work than average but you should be able to benefit from what you have done in the previous exercises.
'''
import math
import numpy as np

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def main(text):
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal 
    # despite casing) can be done with 
    docs = [line.lower().split() for line in text.split('\n')]

    N = len(docs)
    
    # create the vocabulary: the list of words that appear at least once
    vocabulary = list(set(text.lower().split()))

    # 2. go over each unique word and calculate its term frequency, and its document frequency
    
    df = {}
    tf = {}
    for word in vocabulary:
        # tf: number of occurrences of word w in document divided by document length
        # note: tf[word] will be a list containing the tf of each word for each document
        # for example tf['he'][0] contains the term frequence of the word 'he' in the first
        # document
        tf[word] = [doc.count(word)/len(doc) for doc in docs]

        # df: number of documents containing word w
        df[word] = sum([word in doc for doc in docs])/N

    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vector

    # loop through documents to calculate the tf-idf values
    tfidf_v = []
    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            t = tf[word][doc_index] * math.log(1/df[word], 10)
            tfidf.append(t)
        tfidf_v.append(tfidf)

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.

    N = len(tfidf_v)
    dist = np.empty((N, N), dtype=np.cfloat)
    
    for m, item_m in enumerate(tfidf_v):
        diff = 0
        for n, item_n in enumerate(tfidf_v):
            diff = 0
            for c, item_c in enumerate(tfidf_v[m]):
                diff += abs(tfidf_v[m][c]-tfidf_v[n][c])
            if m == n:
                dist[m][n] = np.Inf
            else:
                dist[m][n] = diff

    print(np.unravel_index(np.argmin(dist), dist.shape))

main(text)