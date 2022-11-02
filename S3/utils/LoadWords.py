import pandas as pd

from S3.models import Word


def delete_every_words():
    Word.objects.all().delete()


def __save_words(words_from_excel: [str], is_noun: bool):
    # Remove duplicated words in row input array.
    words_from_excel = [str(w).lower() for w in list(set(words_from_excel))]

    # Check words from db and compare.
    all_words_from_db = [w.word for w in Word.objects.all()]
    temp = []
    for i, v in enumerate(words_from_excel):
        if v not in all_words_from_db:
            temp.append(v)

    words_from_excel = temp
    del temp

    for i, w in enumerate(words_from_excel):
        word = str(w).lower()
        try:
            word = Word.objects.create(word=word, is_noun=is_noun)
        except Exception as e:
            print(f'{word} is occurring error: {e}')
            continue
        print(f'{word} ({i}/{len(words_from_excel)})')


# 형용사
def load_adj():
    adj = pd.read_excel('./S3/utils/words_excel/adj.xlsx', engine='openpyxl', usecols=[0])
    adj_list = []
    for row in adj['words']:
        adj_list.append(row)

    __save_words(adj_list, is_noun=False)


# 명사
def load_noun():
    noun = pd.read_excel('./S3/utils/words_excel/noun.xlsx', engine='openpyxl', usecols=[0])
    noun_list = []
    for row in noun['words']:
        noun_list.append(row)

    __save_words(noun_list, is_noun=True)
