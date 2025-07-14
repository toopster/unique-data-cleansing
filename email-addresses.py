# Import the necessary libraries
import pandas as pd

# Load the data into a dataframe
df = pd.read_csv("email_addresses.csv")

#print(df)

df = df.astype(str)
valid_df = df[df['email'].str.contains("@")]
#print(valid_df)

ultra_valid_df = valid_df[valid_df['email'].str.contains(".co.uk|.com|.org|.org.uk")]
print(ultra_valid_df)

final_df = ultra_valid_df[ultra_valid_df["email"].str.contains(" ") == False]
print(final_df)