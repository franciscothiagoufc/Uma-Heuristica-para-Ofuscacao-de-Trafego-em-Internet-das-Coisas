import numpy as np 
import matplotlib.pyplot as plt

plt.clf()

pinheiro = [29.17,10.94,7.97,5.26]
pinheiro_label = ["Level 100","Level 500","Level 700","Level 900"]

optimized = [25.51,16.35,29.23,27.03]
optimized_label = ["5 Frames","4 Frames","3 Frames","2 Frames"]

plt.plot([1,2,3,4],pinheiro,'bo-',label='Pinheiro et al')
plt.plot([1,2,3,4],optimized,'ro-',label='Proposto')

for x,y,l in zip([1,2,3,4],pinheiro,pinheiro_label):
    plt.annotate(l,(x,y),textcoords="offset points",xytext=(30,5),ha='center')

for x,y,l in zip([1,2,3,4],optimized,optimized_label):
	plt.annotate(l,(x,y),textcoords="offset points",xytext=(-35,-5),ha='center') if x != 2 else plt.annotate(l,(x,y),textcoords="offset points",xytext=(30,-5),ha='center')

ax = plt.gca()
#hide x-axis
ax.get_xaxis().set_visible(False)
ax.margins(x=0.3, y=0.1)

plt.ylabel("Acurácia DT(%)")
plt.legend()

plt.show()
