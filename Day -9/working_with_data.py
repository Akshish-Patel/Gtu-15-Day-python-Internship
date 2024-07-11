import pandas as pd

df = pd.read_csv("Day -9/matches.csv")
print(df)


# dropna() function is use to remove all rows which contains any empty cells
new_df = df.dropna()
print(new_df)

# inplace=true is change the original dataframe
df.dropna(inplace=True) 
print(df)

# fillna method is use to fill the empty cells insted of remove entire row
df = pd.read_csv("Day -9/matches.csv")
print(df)
print(df.fillna(100)) # this method is fill the emply cells by 100 value

print(df['method'])
print(df['method'].fillna(130)) # this method is fill the emply cells by 100 value in only method column

mean = df['target_overs'].mean()
median = df['target_overs'].median()
mode = df['target_overs'].mode()
print(df['method'].fillna(mean)) # this method is fill the emply cells by mena of target_overs column value in only method column
print(df['method'].fillna(median)) # this method is fill the emply cells by median of target_overs column value in only method column
print(df['method'].fillna(mode)) # this method is fill the emply cells by mode of target_overs column value in only method column

# pd.to_dateime() is use to formate the date into proper way
df = pd.read_csv("Day -9/matches.csv")
formated = pd.to_datetime(df['date'])
print(formated)

df.loc[4, 'target_overs'] = 15 #df.loc  is use to change or set the value of cells in the given columr
# in above code value of target_overs at the index 4 is changed by 15
print(df)

for row in df.index:
    if df.loc[row, 'target_overs'] == 20:
        df.loc[row, 'target_overs'] = 10

print(df)

# if duplicate row are available in dataframe than return true otherwise return false
print("\n\n",df.duplicated())