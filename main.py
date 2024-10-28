import pandas as pd
import quandl

dataframe = quandl.get('QDL/BCHAIN')

print(dataframe.head)
