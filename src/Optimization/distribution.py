import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    
    MTU = 1500
    RAW = "../../Data/Raw/"
    filenames = ['16-09-25.csv','16-09-26.csv','16-09-27.csv','16-09-28.csv','16-09-29.csv','16-09-30.csv','16-10-01.csv','16-10-02.csv','16-10-03.csv','16-10-04.csv','16-10-05.csv','16-10-06.csv','16-10-07.csv','16-10-08.csv','16-10-09.csv','16-10-10.csv','16-10-11.csv','16-10-12.csv']
    
    plt.clf()

    distribution = np.zeros(MTU+1)
    frequency = np.zeros(MTU+1)
    total = 0
    for file in filenames:
        print(file)
        df = pd.read_csv(RAW+file,encoding='latin1')
        count = df["Length"].value_counts()
        for i in count.keys():
            if i <= MTU:
                frequency[i] = frequency[i]+count[i]
            total = total + count[i]

    for i,j in enumerate(frequency):
        distribution[i] = j/total
    
    plt.step(range(0,MTU+1),distribution)
    plt.ylabel("Frequência Relativa")
    plt.xlabel("Tamanho do pacote")
    
    plt.grid(visible=True, axis='y',which="major")
    
    plt.show()

    #file = open("distribution.txt","w")
    #for i in distribution:
        #file.write(str(i)+"\n")
    #file.close()
