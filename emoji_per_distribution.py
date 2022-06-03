import numpy as np
import matplotlib.pyplot as plt
import emoji

data=[]
with open("./mama-katu-DM-corpus/Mama_katu_DM_corpus.txt","r",encoding="utf-8",newline="\n") as f:
    data=f.readlines()

data_newline_del=[e.replace("__br__","") for e in data]

emoji_pers=100*np.array([emoji.emoji_count(e)/len(e) for e in data_newline_del])

#plt.hist(count_lens,bins=round(1 + np.log2(count_lens.shape[0])))
plt.title("Emoji per of DM")
plt.xlim(0,100)
plt.hist(emoji_pers,bins=10)

print("Min:{:0.3f}%".format(np.min(emoji_pers)))
print("Max:{:0.3f}%".format(np.max(emoji_pers)))
 
plt.savefig("img/emoji_per_dist.png")
