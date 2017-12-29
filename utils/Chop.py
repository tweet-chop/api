import textwrap
import nltk.data

nltk.download('punkt')

def chop(text, n):
    T = [text]
    old_T = []

    while T != old_T:
        offset = 10
        old_T = T
        tmp = []
        for t in T:
            if len(t) <= n - offset:
                tmp.append(t)
            else:
                tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
                if len(tokenizer.tokenize(t)) == 1:
                    tmp.extend(textwrap.wrap(t, n - offset))
                else:
                    tmp.extend(tokenizer.tokenize(t))
            T = tmp

    if len(T) > 1:
        for i in range(0, len(T)):
            T[i] += " " + str(i + 1) + "/" + str(len(T))

    return T

# For debugging and development purposes, so we are able to
# execute the algorithm directly on some test data!
if __name__ == '__main__':
    fp = open("test.txt")
    fp = open("test2.txt")
    data = fp.read()

    print(chop(data, 140))

