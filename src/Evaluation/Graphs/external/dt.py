from matplotlib import pyplot as plt

if __name__=="__main__":
    adptative_labels = ["Level 100","Level 500","Level 700","Level 900"]
    adptative_values = [29.17,10.94,7.97,5.26]

    optimized_labels = ["Level 66","Level 123","Level 124","Level 156"]
    optimized_values = [23.98,19.43,8.87,28.25]

    '''plt.bar(adptative_labels , adptative_values,color="blue",label='PINHEIRO et al')
    plt.bar(optimized_labels , optimized_values,color="red",label='Proposto')'''
    
    plt.bar(adptative_labels[0] , adptative_values[0],color="blue",label='PINHEIRO et al')
    plt.bar(optimized_labels[0] , optimized_values[0],color="red",label='Proposto')
    
    plt.bar(adptative_labels[1] , adptative_values[1],color="blue")
    plt.bar(optimized_labels[1] , optimized_values[1],color="red")
    
    plt.bar(adptative_labels[2] , adptative_values[2],color="blue")
    plt.bar(optimized_labels[2] , optimized_values[2],color="red")
    
    plt.bar(adptative_labels[3] , adptative_values[3],color="blue")
    plt.bar(optimized_labels[3] , optimized_values[3],color="red")

    plt.title("Decision Tree - Observador Externo",fontsize=24)
    plt.ylabel("Acurácia média",fontsize=24)
    plt.xlabel("Nível de preenchimento",fontsize=24)
    
    plt.legend(fontsize=18)
    plt.tick_params(axis='both', which='major', labelsize=18)

    plt.grid(visible=True, axis='y',which="major")
    fig = plt.gcf()
    fig.set_size_inches((14.2, 8), forward=False)
    fig.savefig("dt.png", bbox_inches='tight')




