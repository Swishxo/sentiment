# Import libraries
from matplotlib import pyplot as plt


def plot(pos:int, neg:int, nu:int):
# Creating dataset
    positive = 'Positive:\n {}'.format(pos)
    negative = 'Negative:\n {}'.format(neg)
    nuetrual = 'Neutral:\n {}'.format(nu)
    politicalViews = [positive, negative, nuetrual]

    data = [pos, neg, nu]
    explode = []

    if(pos > neg and pos > nu):
        explode.append(0.2)
        explode.append(0.0)
        explode.append(0.0)
    elif(neg > pos and neg > nu):
        explode.append(0.0)
        explode.append(0.2)
        explode.append(0.0)
    else:
        explode.append(0.0)
        explode.append(0.0)
        explode.append(0.2)

    #getting count
    total(pos,neg,nu)

    # Creating plot
    fig = plt.figure(figsize=(10, 7))
    plt.pie(data, labels=politicalViews, explode=explode, shadow=True)

    #create legend
    plt.legend()

    # show plot
    plt.show()

def total(pos:int, neg:int, nu:int):
    print(pos + neg + nu)