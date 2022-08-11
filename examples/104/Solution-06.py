# Prog-06: Jaccard Similarity
# Knight N104

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

STOP_WORDS = stopwords.words('english')
STEMMER = PorterStemmer()

def read_tweets():
    f = open('biden.txt', encoding='utf-8')
    tweets = [line.strip() for line in f.readlines()]
    f.close()
    return tweets

def normalize_text( text ):
    words = []
    for w in word_tokenize(text.lower()):
        if w.isalnum() and w not in STOP_WORDS:
            words.append(STEMMER.stem(w))
    return get_unique( words )

def main():
    tweets = read_tweets()
    norm_tweets = []
    for t in tweets:
        norm_tweets.append( normalize_text(t) )

    print_width = 48
    while True:
        query = input('Query words   : ')
        if query == '': break
        n = int(input('No. of results: '))
        norm_query = normalize_text(query)
        top_n = top_n_similarity(norm_tweets, norm_query, n)
        if len(top_n) == 0:
            print('No matches found.')
        else:
            for tid, jc_coef in top_n:
                show_tweet(tid, tweets[tid], jc_coef, print_width)
        print('-' * print_width)

#--------------------------------------------------------
def get_unique( words ):
    unique_words=[]
    for i in words:
        if i not in unique_words:
            unique_words.append(i)
    return unique_words

def jaccard(words_1, words_2):
    s=[x for x in words_1 if x in words_2]
    n=words_1+[y for y in words_2 if y not in words_1]
    jaccard_coef=len(s)/(len(n))
    return jaccard_coef

def top_n_similarity(norm_tweets, norm_query, n):
    count=[]
    for i in range(len(norm_tweets)):
        count.append([jaccard(norm_tweets[i],norm_query),-i])
    count.sort()
    count=count[len(count)-n:]
    top_n=[[abs(a),b] for b,a in count]
    top_n.reverse()
    return top_n

def show_tweet(tweet_id, tweet_content, jc_coef, print_width):
    print(f"\n#{tweet_id} ({round(jc_coef,2)})")
    x=tweet_content.split(' ')
    p='  '
    for i in range(len(x)):
        if len(p)+len(x[i])+1<=print_width:
            p+=' '*int(i!=0)+x[i]
        else:
            print(p)
            p='  '+x[i]
    print(p)

#--------------------------------------------
main()
