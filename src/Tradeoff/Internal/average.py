from tradeoff import tradeoff
from matplotlib import pyplot as plt

if __name__=="__main__":
    adptative_labels = ["KNN","DT","RF","SVM"]
    adptative_values = [0.33360896480504476,0.3440920245689198,0.335581014396653,0.3371580313775149]

    adptative_labels = ["KNN","DT","RF","SVM"]
    optimized_values = [0.4912228649020127,0.5377150411284296,0.5038622734422952,0.3849012420396068]

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

    plt.title("Tradeoff Médio - Observador Externo")
    plt.ylabel("Tradeoff Médio")
    plt.legend(
