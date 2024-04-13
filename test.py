import pandas as pd
import re

df = {'Latin': [], 'Russian': []}
with open('латинские выражения.txt', 'r', encoding='utf-8' ) as f:
    text = f.readlines()
    for line in text:
        line = re.split(r'\.|!|\?', line)
        df['Latin'].append(line[1])
        df['Russian'].append(line[2])
    df = pd.DataFrame(df)

print(df.head())
df.to_csv('latin.csv', encoding='UTF-8', index=False)
    