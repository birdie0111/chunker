import spacy as sp

nlp_fr = sp.load("fr_core_news_sm") # pour tokeniser textes en francais
nlp_en = sp.load("en_core_web_sm")


def make_token(f_in, f_token, language):
    '''
    Tokenizer le fichier .txt et sauvegarder le résultat dans un autre fichier de .txt

    parameters:
        f_in (string): nom du fichier d'entrée (texte brut)
        f_token (string): nom du fichier sortie (token séparé par "|")

    return:
        None

    '''
    phrase = ""
    with open(f_in, "r", encoding="utf-8") as f_in:
        with open(f_token, "w", encoding="utf-8") as file_token:
            for line in f_in:
                line = line.strip()
                phrase += line
            if (language == "fr"):
                doc = nlp_fr(phrase)
            elif (language == "en"):
                doc = nlp_en(phrase)
            for token in doc:
                file_token.write(token.text.lower() + "|")


def dic_tokens(file_token):
    '''
    Sauvegarder les tokens dans une liste de chaîne de caractères

    parameters:
        file_token (string): nom du fichier d'entrée .txt (token séparé par "|")

    return:
        tokens (list): liste de tokens

    '''
    tokens = []
    article = ""
    for line in file_token:
        line = line.strip()
        article += line
    tokens = article.split("|")
    return tokens

def write_chunker(fd_out, word_out, mark):
    '''
    Ecrire les chunks et ses catégories dans un fichier .txt

    parameters:
        fd_out (file descriptor): descripteur du fichier sortie
        word_out (list): liste de tokens
        mark (string): catégorie du chunk

    return:
        None

    '''
    for chunk in range(len(word_out) - 1):
        fd_out.write(word_out[chunk] + " ")
    fd_out.write("\t->" + mark + "\n")

def init_values(token, list_word, key):
    '''
    Initialiser les valeurs

    parameters:
        token (string): le prochain token dans la phrase
        list_word (dict): le dictionnaire qui contient les tokens et ses catégories
        key (string): la catégorie du token

    return:
        mark (string): catégorie du chunk
        word_out (list): liste de tokens (chunk) avant le token
        count_dict_words (int): le nombre total des tokens dans le chunk
        list_word (dict): le dictionnaire qui contient les tokens et ses catégories


    '''
    mark = ""
    word_out = []
    word_out.append(token)
    count_dict_words = 0
    list_word.clear()
    list_word[token] = key
    return mark, word_out, count_dict_words, list_word


def handle_pct_conj(fd_out, token, pct_or_conj, word_out, mark):
    '''
    Ecrit le chunk de catégorie "pct" et "conj" directement dans le fichier de sortie

    parameters:
        fd_out (file descriptor): descripteur du fichier sortie
        token (string): le token qui va être écrit dans le fichier
        pct_or_conj (string): "pct" ou "conj"
        word_out (list): liste de tokens (chunk) avant le token
        mark (string): catégorie du chunk

    return:
        None

    '''
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