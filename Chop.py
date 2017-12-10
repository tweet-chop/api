import nltk.data
import ipdb


def chop(text, res):
    n = 140
    if len(text) <= n:
        res.append(text)
        return [text]

    tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
    T = tokenizer.tokenize(text)
    if len(T) == 1:
        # Sentence is too long, chop it in chunks of 140 chars
        T = [ T[0][i:i+n] for i in range(0, len(T[0]), n)]

    for t in T:
        chop(t, res)
    return res

def naive_chop(text):
    return [ text[i:i+n] for i in range(0, len(text), n)]


# nltk.download('punkt')
if __name__ == '__main__':
    fp = open("test.txt")
    data = fp.read()

    print(chop(data))

