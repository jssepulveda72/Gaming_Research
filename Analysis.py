import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from func import *
plt.close()

survey = pd.read_excel("Gaming_Survey_Responses.xlsx")

survey["Gender"] = np.where(survey["Gender"]=="Male",0,1) #Male = 0 Female =1 

survey = survey.drop(["Timestamp",'How often do you play video games?',
                        'How many hours do you typically spend gaming in a week?',
                        'Which device do you play games on the most?(Check all that apply)',
                        'What genres of video games do you play? (Check all that apply)',
                        'What is your favorite game?',
                        'How do you discover new games? (Check all that apply)',
                        'Do you prefer single-player or multiplayer games?',
                        'How much do you spend on gaming monthly (including in-game purchases, new games, etc.)?',
                        'Why do you play video games? (Check all that apply)'],axis= 1)

survey.columns = ['Age', 'Gender', 'Location',
       'Frequency',
       'Hours/week',
       'Devices',
       'Genres',
       'Favorite',
       'Find new games',
       'Single-player or multiplayer',
       'Spend/monthly',
       'Reason',]
       






frequencies = dict()
for column in survey.columns[3:]:
    
    frequencies[column] = Itemcounter(survey[column])
    
for item in frequencies.keys():
    Histogramplotter(frequencies[item], item)
 




