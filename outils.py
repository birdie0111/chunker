import spacy as sp



nlp_fr = sp.load("fr_core_news_sm") # pour tokeniser textes en francais



def fr_token(f_in, f_token):
    phrase = ""
    with open(f_in, "r", encoding="utf-8") as f_in:
        with open(f_token, "w", encoding="utf-8") as file_token:
            for line in f_in:
                line = line.strip()
                phrase += line
            doc = nlp_fr(phrase)
            for token in doc:
                file_token.write(token.text.lower() + "|")


def dic_tokens(file_token):
    tokens = []
    article = ""
    for line in file_token:
        line = line.strip()
        article += line
    tokens = article.split("|")
    return tokens

def write_chunker(fd_out, word_out, mark):
    for chunk in range(len(word_out) - 1):
        fd_out.write(word_out[chunk] + " ")
    fd_out.write("\t->" + mark + "\n")

def init_values(token, list_word, key):
    mark = ""
    word_out = []
    word_out.append(token)
    count_dict_words = 0
    list_word.clear()
    list_word[token] = key
    return mark, word_out, count_dict_words, list_word


def handle_pct_conj(fd_out,token, pct_or_conj, word_out, mark):
    # ecrire le chunker
    if(len(word_out) > 0):
        for chunk in word_out:
            fd_out.write(chunk + " ")
        if(mark != ""):
            fd_out.write("\t-> " + mark + "\n")
    # ecrire pct ou conj et reinitialiser
    count_dict_words = 0
    fd_out.write(token+"\t-> "+ pct_or_conj +"\n")
    mark = ""
    word_out = []
    return mark, count_dict_words, word_out