import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

data=[]
with open("./mama-katu-DM-corpus/Mama_katu_DM_corpus.txt","r",encoding="utf-8",newline="\n") as f:
    data=f.readlines()

data_newline_del=[e.replace("__br__","") for e in data]
count_lens=np.array([(len(e)) for e in data_newline_del ])
count_lens=np.array([(e) for e in count_lens if e<np.max(count_lens)])

#plt.hist(count_lens,bins=round(1 + np.log2(count_lens.shape[0])))
plt.title("QQ plot of lengths of DM")
stats.probplot(count_lens, dist="norm", plot=plt)
 
plt.savefig("img/len_QQ.png")

plt.clf()

plt.title("lengths of DM")
plt.hist(count_lens,bins=20,density=True)

count_lens_M=np.mean(count_lens)
count_lens_S=np.std(count_lens)

print(count_lens_M)
print(count_lens_S)

norm_X=np.linspace(40,160,100)
norm_Y=stats.norm.pdf(norm_X, loc=count_lens_M, scale=count_lens_S)

plt.plot(norm_X,norm_Y)
 
plt.savefig("img/len_norm.png")
