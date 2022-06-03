import numpy as np
import emoji

data=[]
with open("./mama-katu-DM-corpus/Mama_katu_DM_corpus.txt","r",encoding="utf-8",newline="\n") as f:
    data=f.readlines()

data_newline=[e.replace("__br__","\n") for e in data]
data_newline_del=[e.replace("__br__","") for e in data]

print("ママ活DMコーパス概要(少数二桁まで表示)\n")
print("サンプル数:{0}".format(len(data)))

A_len=np.mean(np.array([len(e) for e in data_newline_del]))
print("一DMあたりの平均文字数:{:0.2f}個".format(A_len))

A_lb=np.mean(np.array([e.count("__br__") for e in data]))
print("一DMあたりの平均改行数:{:0.2f}個".format(A_lb))


A_lb=np.mean(np.array([len(e)/(e.count("__br__")+1) for e in data]))
print("一DMの一行あたりの平均文字数:{:0.2f}文字".format(A_lb))

#print(data_newline[0])

A_e=np.mean(np.array([emoji.emoji_count(e) for e in data_newline]))
print("一DMあたりの平均絵文字数:{:0.2f}個".format(A_e))

A_ep=np.mean(np.array([emoji.emoji_count(e)/len(e) for e in data_newline_del]))
print("一DMあたりの平均絵文字率(改行除く):{:0.2f}%".format(A_ep*100))
