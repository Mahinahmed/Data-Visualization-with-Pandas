import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
web_stats = {'Day':[1,2,3,4,5],
             'Visitors':[44,54,66,77,98],
             'Bounce':[65,72,64,54,66]}
df = pd.DataFrame(web_stats)
#print(df)
#print(df.head())
#print(df.tail())
#print(df.set_set_index('Day'))
#print(df.head())
print(df['Visitors'])
