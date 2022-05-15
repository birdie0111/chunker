import outils as ot
import pandas as pd

# ---------------------------------------- noms des fichiers ------------------------------------------
f_in = "source.txt"
f_token = "tokens.txt"
f_out = "chunker.txt"

# ---------------------------------------- variables globaux ------------------------------------------
list_word = {}
word_out = []
previous_key = ""
mark = ""
count_dict_words = 0 # compter nombre de mots de dict dans list_word
non_dict_flag = False
duplicate_flag = False


# ---------------------------------------- faire le fichier de tokenization ----------------------------
ot.fr_token(f_in, f_token)
with open(f_token, "r", encoding="utf-8") as file_token:
    tokens = ot.dic_tokens(file_token)

# ---------------------------------------- faire les dictionnaires par rapport aux fichiers csv --------
category = pd.read_csv("dict.csv").fillna("NULL").to_dict("list")
regle = pd.read_csv("regle.csv", index_col="index").fillna("NULL").to_dict("dict")

# ---------------------------------------- faire les chunkers ------------------------------------------

print(category)
print(regle)

'''
with open(f_out, "w", encoding="utf-8") as try_out:
    for token in tokens:
        # Verifier si le token est deja un chunker lui-même
        if token in category["pct"]:
            mark, count_dict_words, word_out = ot.handle_pct_conj(try_out, token, "PCT", word_out, mark)
            list_word.clear()
        elif token in category["conj"]:
            mark, count_dict_words, word_out = ot.handle_pct_conj(try_out, token, "CONJ", word_out, mark)
            list_word.clear()
        # Si le token n'est pas un chunker:
        else:
            if token not in list_word:
                list_word[token] = "" # initialiser le token
            else:
                duplicate_flag = True
            word_out.append(token)
            for key in category.keys():
                # Si le token peut être combiné, alors on passe et regarde token prochain
                if token in category[key]: 
                    count_dict_words += 1

                    if (len(list_word) == 1):
                        list_word[token] = key  # sauvegarder le token et sa categorie
                        previous_key = key      # categorie de premier token
                        break
                    # Si on a deja de token avant:
                    elif (len(list_word) > 1):
                        # Si y'a moins de 3 tokens dans word_out:
                        if(count_dict_words < 3 and duplicate_flag == False):
                            list_word[token] = key  # sauvegarder le token et sa categorie

                            # rechercher dans regle
                            if (previous_key != ""):
                                if regle[previous_key][key] != "NULL":
                                    if(mark == "" or non_dict_flag == True):
                                        mark = regle[previous_key][key]
                                        non_dict_flag = False
                                    previous_key = key
                                else:
                                # Si pas dans regle, alors ce token est considere comme nouvel debut d'un chunker
                                    previous_key = key
                                    # ecrire le chunker
                                    ot.write_chunker(try_out, word_out, mark)
                                    # reinitialisation
                                    mark, word_out, count_dict_words, list_word = ot.init_values(token, list_word, key)
                            else:
                                print("problem, length of dict")
                                print(list_word)
                        else: # Si y'a déjà 2+ tokens de dict ou une duplicate, on ecrit le chunker:
                            
                            # ecrire le chunker
                            ot.write_chunker(try_out, word_out, mark)
                            # reinitialisation
                            mark, word_out, count_dict_words, list_word = ot.init_values(token, list_word, key)
                            duplicate_flag = False
                            previous_key = key

                else: # Si le token n'est meme pas dans le categorie
                    if(previous_key != "" and mark == ""):
                        mark = regle[previous_key]["default"]
                        non_dict_flag = True


'''