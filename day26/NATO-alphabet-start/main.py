import pandas as pd

nato_df = pd.read_csv("nato.csv")

nato_dict = {row.letter:row.code for (index,row) in nato_df.iterrows()}

your_name = input("what's your name? ").upper()
print([nato_dict[letter] for letter in your_name])