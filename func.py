import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import re



def Cleaner(column):
    """
    Cleaning series object
    
    Parameters
    ----------
    column : pd.series
    
    Returns
    -------
    pd.series
    
    The same column after the cleaning rules were applied.
    """
    
    column = column.replace(0,"0") #Replaces int 0 with str 0
    column = column.apply(lambda x: re.sub("\(.*\)", "", x)) #Erases every parentheses
    column = column.apply(lambda x: x.lower().strip()) #Lowers the string and erase the spaces
    
    return column


def Itemcounter(column):
    """
    Finds number of aparecences for every
    item in the column
    
    Useful for string columns with multiple answers
    divided by a coma (,)

    Parameters
    ----------
    column : pd.series
        The series object wich contains the answers.

    Returns
    -------
    dictionary : dictionary {keys: Categories
                             values: Repetions of each categorie}
        The dictionary whose keys are the categories and 
        the values are the number of repetitions of each 
        category.

    """
    
    
    types = column.apply(lambda x: x.split(",")) 
    dictionary = dict()
    for row in types:
        for item in row:
            item = item.strip()
            dictionary[item] = dictionary.get(item,0) + 1
            
    return dictionary

def Histogramplotter(dictionary,name):
    """
    Plots a dictionary with frequencies as an histogram.

    Parameters
    ----------
    dictionary : dictionary {keys: Categories
                             values: Repetions of each categorie}
        
    name : String
        The general name of the categories.

    Returns
    -------
    
    None.

    """
        
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
    """
    Plots a heatmap comparing two series objects
    with categories.
    
    
    Parameters
    ----------
    column1 : pd.series
        Main column values or index values to compare along the different categories.
    column2 : pd.series
        Column with the categories to compare the index column.

    Returns
    -------
    None.

    """
    
    column = column2.apply(lambda x: x.split(","))
    categories = set()
    for i in column:
        categories = categories|set([j.strip() for j in i])
    
    
    categoriesDF = pd.DataFrame([[1 if categorie in column[i] else 0 for categorie in categories]
                  for i in range(len(column))],columns=list(categories))
    
    
    newAuxFrame = pd.concat([column1, categoriesDF],axis=1)
    pivotAux = pd.pivot_table(data = newAuxFrame, 
                              aggfunc="sum",
                              index=[column1],
                              values=list(categories))
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(pivotAux, annot=True, cmap='YlGnBu', fmt='d')
   
    plt.title('Heatmap of Variable Relationships')
    plt.xticks(rotation=15, ha='right') 