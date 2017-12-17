import nltk.data
import textwrap

def chop(text, n):
    T = [text]
    old_T = []

    while T != old_T:
        # print(T)
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

    for i in range(0, len(T)):
        T[i] += "(" + str(i+1) + "/"+str(len(T))+")"

    return T

def naive_chop(text):
    return [ text[i:i+n] for i in range(0, len(text), n)]


nltk.download('punkt')

if __name__ == '__main__':
    fp = open("test.txt")
    fp = open("test2.txt")
    data = fp.read()

    print(chop(data, 140))

