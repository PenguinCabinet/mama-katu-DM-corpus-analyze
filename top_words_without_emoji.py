from token import tok_name
from janome.tokenizer import Tokenizer
import collections
import itertools
import emoji
import re

t = Tokenizer(udic="./userdic.csv",udic_enc="utf-8")

#emoji_list = [str(c) for c in emoji.UNICODE_EMOJI]

data=[]
with open("./mama-katu-DM-corpus/Mama_katu_DM_corpus.txt","r",encoding="utf-8",newline="\n") as f:
    data=f.readlines()

data_newline_del=[e.replace("__br__","") for e in data]

data_newline_emoji_del=[
    re.sub(emoji.get_emoji_regexp(), '', e)
    for e in data_newline_del
]

#print(emoji_list)

def token_split(v,Only_meaning_words):
    A=[]
    for token in t.tokenize(v):
        token_type1=token.part_of_speech.split(',')[0]
        token_type2=token.part_of_speech.split(',')[1]
        #print(token_type1)
        if Only_meaning_words:
            if token_type1 in ["名詞","形容詞"]:
                if len(token.base_form)!=0:
                    A.append(token.base_form)
                elif len(token.surface)!=0:
                    
                    A.append(token.surface)
        else:
            A.append(token.base_form)
    return A

#print([e.part_of_speech.split(',') for e in list(t.tokenize(" A \n  A\n AA "))])

data_tokens=[token_split(e,True) for e in data_newline_emoji_del]
#print(data_tokens)

data_tokens_f=list(itertools.chain.from_iterable(data_tokens))

#print(data_tokens)
print("使用頻度が多い単語Top10")

c = collections.Counter(data_tokens_f)
for i,e in enumerate(list(c.most_common(10))):
    print("{0}位:{1} {2}回".format(i+1,e[0],e[1]))


