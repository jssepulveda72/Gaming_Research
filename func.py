import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import re



def Cleaner(column):
    column = column.replace(0,"0")
    column = column.apply(lambda x: re.sub("\(.*\)", "", x))
    column = column.apply(lambda x: x.lower().strip())
    
    return column


def Itemcounter(column):
    
    types = column.apply(lambda x: x.split(","))
    dictionary = dict()
    for row in types:
        for item in row:
            item = item.strip()
            dictionary[item] = dictionary.get(item,0) + 1
            
    return dictionary

def Histogramplotter(dictionary,name):
    
    
    df = pd.DataFrame(list(dictionary.items()), columns=[f'{name}', 'Counts'])
    df[f'{name}'] = df[f'{name}'].apply(lambda x: x.capitalize())
    
    plt.figure(figsize=(12, 6))  
    sns.barplot(x=f'{name}', y='Counts', data=df, palette='coolwarm')
    
    
    plt.xlabel(f'{name}', fontsize=12)
    plt.ylabel('Counts', fontsize=12)
    plt.title(f'Category Distribution of {name}', fontsize=14)
    plt.xticks(rotation=45, ha='right') 
    
    
    plt.tight_layout()  
    plt.grid()
    
def Heatmapplotter(column1,column2):
    
    column = column2.apply(lambda x: x.split(","))
    categories = set()
    for i in column:
        categories = categories|set([j.strip() for j in i])
    
    
    categoriesDF = pd.DataFrame([[1 if categorie in column[i] else 0 for categorie in categories]
                  for i in range(len(column))],columns=list(categories))
    
    # categories = map(lambda x: x.capitalize(), categories)
    newAuxFrame = pd.concat([column1, categoriesDF],axis=1)
    pivotAux = pd.pivot_table(data = newAuxFrame, 
                              aggfunc="sum",
                              index=[column1],
                              values=list(categories))
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(pivotAux, annot=True, cmap='Blues', fmt='d')
   
    plt.title('Heatmap of Variable Relationships')
    plt.xticks(rotation=15, ha='right') 