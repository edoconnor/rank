import pandas as pd
import csv

df = pd.read_csv("scores.csv") 

df['f'] = df.groupby('score')['score'].transform('count')
df['n'] = len(df['score'])

df1 = df[['player','score']]

## This program ranks the LOWEST score as the best score.
## Edit the TWO sort functions below for 'high score is best'

df = df.sort_values(by='score', ascending=False)
## for 'high score is best' scenario change to:
## df = df.sort_values(by='score', ascending=True)

df = df.drop_duplicates(subset=['score'])
df['cf'] = df['f'].cumsum()
df['rank'] = (df['cf'] - (0.5 * df['f'])) / df['n'] * 100
df['rank'] = df["rank"].astype(int)

df2 = df[['score','rank']]

df3 = pd.merge(df1,df2, on='score', how='outer')

df3 = df3.sort_values(by='score', ascending=True)
## for 'high score is best' scenario change to:
## df = df.sort_values(by='score', ascending=False)

print(df3)

## to save file
# df3.to_csv('file.csv', header=None,index=False)
