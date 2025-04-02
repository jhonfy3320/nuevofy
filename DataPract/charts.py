import matplotlib.pyplot as plt 

def generate_pie_chart():
    labels = ['A', 'B', 'C', 'D',]
    values = [12, 13, 14, 34]
    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('fig.png')
    plt.close()
    plt.show()
