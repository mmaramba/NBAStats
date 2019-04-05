import pandas as pd

df = pd.read_csv('nba_draft.csv')

print(df)

# How to clean the data: do we delete samples or impute? Probably just gonna impute


# Info: Steals recorded 73-74 season, Blocks recorded 73-74 season, 3PT recorded since 79




# Dropping columns:
# df.drop(['Season', 'Lg', 'Player', 'Voting', 'Tm', 'WS/48'], axis=1, inplace=True)