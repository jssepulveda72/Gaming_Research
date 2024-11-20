import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from func import *
plt.close()
frequencies = dict()

survey = pd.read_excel("Gaming_Survey_Responses.xlsx")

#Erase columns with irrelevant information
survey = survey.drop(["Timestamp","Location",'How often do you play video games?',
                        'How many hours do you typically spend gaming in a week?',
                        'Which device do you play games on the most?(Check all that apply)',
                        'What genres of video games do you play? (Check all that apply)',
                        'What is your favorite game?',
                        'How do you discover new games? (Check all that apply)',
                        'Do you prefer single-player or multiplayer games?',
                        'How much do you spend on gaming monthly (including in-game purchases, new games, etc.)?',
                        'Why do you play video games? (Check all that apply)'],axis= 1)

#Rename columns for easier handling
survey.columns = ['Age', 'Gender', 
       'Frequency',
       'Hours/week',
       'Devices',
       'Genres',
       'Favorite',
       'Find new games',
       'Single-player or multiplayer',
       'Spend/monthly',
       'Reason',]
       

survey["Gender"] = Cleaner(survey["Gender"])
for column in survey.columns[2:]:
    survey[column] = Cleaner(survey[column])
    

# for column1 in survey.columns[0:2]:
#     for column2 in survey.columns[2:]:
Heatmapplotter(survey["Gender"], survey["Spend/monthly"])
frequencies['Hours/week'] = Itemcounter(survey['Hours/week']) 
frequencies['Devices'] = Itemcounter(survey['Devices']) 
frequencies['Genres'] = Itemcounter(survey['Genres']) 
frequencies['Find new games'] = Itemcounter(survey['Find new games']) 
    
for item in frequencies.keys():
      Histogramplotter(frequencies[item], item)

 





