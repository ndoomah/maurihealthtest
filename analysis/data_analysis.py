import pandas as pd
import os

os.environ['R_HOME'] = 'C:/Program Files/R/R-3.5.2' #path to your R installation
os.environ['R_USER'] = 'C:/Users/User1/Desktop/Webscraper/venv/Lib/site-packages/rpy2' #path depends on where you installed Python. Mine is the Anaconda distribution
os.environ['R_LIBS'] = 'C:/Users/User1/Documents/R/win-library/3.5'

import rpy2.robjects as ro
path="./"

from rpy2.robjects import pandas2ri
pandas2ri.activate()

# Load data from csv file
data = pd.read_csv('data.csv')
#print(data.columns.get_loc('date'))
d_list = ['influenza', 'gastroenteritis', 'conjunctivitis', 'respiratory infection']

for d in d_list:
    t = data[data['disease'] == d].groupby('date',as_index=False)[['disease']].count()
    print(t)

    #Calling rpredict function from prediction.R script
    r = ro.r
    r.source(path + "prediction.R")
    r.rpredict(t, d)


