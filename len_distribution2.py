import numpy as np
import matplotlib.pyplot as plt

data=[]
with open("./mama-katu-DM-corpus/Mama_katu_DM_corpus.txt","r",encoding="utf-8",newline="\n") as f:
    data=f.readlines()

data_newline_del=[e.replace("__br__","") for e in data]

count_lens=np.array([len(e) for e in data_newline_del])
count_lens=np.array([e for e in count_lens if e<np.max(count_lens)])

#plt.hist(count_lens,bins=round(1 + np.log2(count_lens.shape[0])))
plt.title("Lengths of DM")
plt.hist(count_lens,bins=20)
 
plt.savefig("img/len_dist2.png")
