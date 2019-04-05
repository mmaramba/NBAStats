import pandas as pd

# Info: Steals recorded 73-74 season, Blocks recorded 73-74 season, 3PT recorded since 79
df = pd.read_csv('nba_draft.csv')

# Fill NaNs with zeros. Alternatives?
df = df.fillna(0)

df.to_csv('nba_draft.csv')  # Export as csv

