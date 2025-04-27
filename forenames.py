# Import the necessary libraries
import pandas as pd

# Load the data into a dataframe
df = pd.read_csv("forenames.csv")

df["FirstName"] = df["FirstName"].astype(str)

cleaned_data = []

# Loop through dataframe finding two names
for index, row in df.iterrows():

    member_id = row["MemberID"]

    # Check for &
    if row["FirstName"].find(" & ") != -1:

        person_1 = row["FirstName"][:row["FirstName"].find(" & ")]
        person_2 = row["FirstName"][row["FirstName"].find(" & ") + len(" & "):len(row["FirstName"])]

        cleaned_data.append([member_id, person_1])
        cleaned_data.append([member_id, person_2])
    
    # Check for and
    elif str(row["FirstName"]).find(" and ") != -1:

        person_1 = row["FirstName"][:row["FirstName"].find(" and ")]
        person_2 = row["FirstName"][row["FirstName"].find(" and ") + len(" and "):len(row["FirstName"])]

        cleaned_data.append([member_id, person_1])
        cleaned_data.append([member_id, person_2])

    else:

        cleaned_data.append([member_id, row["FirstName"]])

cleaned_df = pd.DataFrame(cleaned_data, columns=["MemberID", "FirstName"])

                                                                                                                                                                                                                                                                                               

cleaned_df["FirstNameLength"] = cleaned_df["FirstName"].str.len()

# View final dataframe 
# print(cleaned_df)

# Now filter out those rows in the Pandas dataframe that are greater than 14 and put them into a new dataframe
filtered_cleaned_df = cleaned_df[cleaned_df['FirstNameLength'] > 14]

# print(filtered_cleaned_df)


# Now filter out those rows in the Pandas dataframe that are greater than 14 from the original dataframe
filtered_cleaned_df2 = cleaned_df[cleaned_df['FirstNameLength'] < 14]
# print(filtered_cleaned_df2)

deceased_df = cleaned_df[cleaned_df['FirstName'].str.contains("died|DIED")]
print(deceased_df)