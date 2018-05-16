import Quandl
import pandas as pd

api_key = open ('quandlapikey.text','r').read()

df = Quandl.get('ZILLOW/Z77006_ZRIFAH', authtoken=api_key)

print(df.head())
