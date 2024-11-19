import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import re


def Itemcounter(column):
    column = column.replace(0,"0")
    column = column.apply(lambda x: re.sub("\(.*\)", "", x))
    types = column.apply(lambda x: x.lower().split(","))
    dictionary = dict()
    for row in types:
        for item in row:
            item = item.strip()
            dictionary[item] = dictionary.get(item,0) + 1
            
    return dictionary

def Histogramplotter(dictionary,name):
    
    df = pd.DataFrame(list(dictionary.items()), columns=[f'{name}', 'Counts'])

    
    plt.figure(figsize=(12, 6))  
    sns.barplot(x=f'{name}', y='Counts', data=df, palette='coolwarm')
    
    
    plt.xlabel(f'{name}', fontsize=12)
    plt.ylabel('Counts', fontsize=12)
    plt.title(f'Category Distribution of {name}', fontsize=14)
    plt.xticks(rotation=45, ha='right') 
    
    
    plt.tight_layout()  
    plt.grid()