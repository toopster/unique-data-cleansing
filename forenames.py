# Import the necessary libraries
import pandas as pd

# Load the data into a dataframe
df = pd.read_csv("forenames.csv")

cleaned_data = []

# Loop through dataframe finding two names
for index, row in df.iterrows():

    member_id = row["MemberID"]

    # Check for &
    if str(row["FirstName"]).find(" & ") != -1:

        person_1 = str(row["FirstName"])[:str(row["FirstName"]).find(" & ")]
        person_2 = str(row["FirstName"])[str(row["FirstName"]).find(" & ") + len(" & "):len(str(row["FirstName"]))]

        cleaned_data.append([member_id, person_1])
        cleaned_data.append([member_id, person_2])
    
    # Check for and
    elif str(row["FirstName"]).find(" and ") != -1:

        person_1 = str(row["FirstName"])[:str(row["FirstName"]).find(" and ")]
        person_2 = str(row["FirstName"])[str(row["FirstName"]).find(" and ") + len(" and "):len(str(row["FirstName"]))]

        cleaned_data.append([member_id, person_1])
        cleaned_data.append([member_id, person_2])

    else:

        cleaned_data.append([member_id, row["FirstName"]])

cleaned_df = pd.DataFrame(cleaned_data, columns=["MemberID", "FirstName"])

print(cleaned_df.head(40))