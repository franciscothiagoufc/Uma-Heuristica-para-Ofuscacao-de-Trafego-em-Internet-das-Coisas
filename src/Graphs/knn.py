import numpy as np 
import matplotlib.pyplot as plt

plt.clf()

pinheiro = [57.06,34.45,32.71,32.30]
pinheiro_label = ["Level 100","Level 500","Level 700","Level 900"]

optimized = [30.32,23.16,32.30,25.46]
optimized_label = ["5 Frames","4 Frames","3 Frames","2 Frames"]

plt.plot([1,2,3,4],pinheiro,'bo-',label='Pinheiro et al')
plt.plot([1,2,3,4],optimized,'ro-',label='Proposto')

for x,y,l in zip([1,2,3,4],pinheiro,pinheiro_label):
    plt.annotate(l,(x,y),textcoords="offset points",xytext=(30,5),ha='center')

for x,y,l in zip([1,2,3,4],optimized,optimized_label):
    plt.annotate(l,(x,y),textcoords="offset points",xytext=(-35,-5),ha='center')

ax = plt.gca()
#hide x-axis
ax.get_xaxis().set_visible(False)
ax.margins(x=0.3, y=0.1)

plt.ylabel("Acurácia KNN(%)")
plt.legend()

plt.show()
