import pandas as pd

from S3.models import Word

# 형용사
adj = pd.read_excel('./S3/utils/words_excel/adj.xlsx', engine='openpyxl', usecols=[0])
adj_list = []
for row in adj['words']:
    adj_list.append(row)

adj_list = list(set(adj_list))
print(f'adj count: {len(adj_list)}')

for w in adj_list:
    try:
        Word(word=w, is_noun=False).save()
    except Exception as e:
        print(f'{w} is occuring error: {e}')
        continue
    print(f'{w=} is saving')

# 명사
noun = pd.read_excel('./S3/utils/words_excel/noun.xlsx', engine='openpyxl', usecols=[0])
noun_list = []
for row in noun['words']:
    noun_list.append(row)

adj_list = list(set(noun_list))
print(f'noun count: {len(noun_list)}')

for w in noun_list:
    try:
        Word(word=w, is_noun=True).save()
    except Exception as e:
        print(f'{w} is occuring error: {e}')
        continue
    print(f'{w=} is saving')
