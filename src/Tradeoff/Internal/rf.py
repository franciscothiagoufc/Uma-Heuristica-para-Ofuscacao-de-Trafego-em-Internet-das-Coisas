from tradeoff import tradeoff
from matplotlib import pyplot as plt

if __name__=="__main__":
    adptative_labels = ["Level 100","Level 500","Level 700","Level 900"]
    adptative_values = tradeoff([0.6603,0.5218,0.5038,0.4983],[1.3,2.58,3.44,4.33])

    optimized_labels = ["Level 66","Level 123","Level 124","Level 156"]
    optimized_values = tradeoff([0.6589,0.6436,0.5954,0.5525],[1.2417833123908109,1.3008506129573985,1.469192531290397,2.399349331176418])

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

    plt.title("RF - Observador Interno",fontsize=24)
    plt.ylabel("Tradeoff",fontsize=18)
    plt.xlabel("Byte Overhead",fontsize=18)
    
    plt.legend(fontsize=18)
    
    plt.grid(visible=True, axis='y',which="major")
    plt.tick_params(axis='both', which='major', labelsize=17.5)
    
    fig = plt.gcf()
    fig.set_size_inches((14.2, 8), forward=False)
    fig.savefig("rf.png", bbox_inches='tight')    
        
    print("Avg - adptative ", sum(adptative_values)/len(adptative_values),"Avg - optimized ",sum(optimized_values)/len(optimized_values))
