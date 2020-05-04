import pandas as pd

# READING IN DATA FROM CSV
data = pd.read_csv("filename.csv")    # Read in data from CSV-file
#data.head()                          # Show column names
#print(data)                          # Show data

# SELECT COLUMN
# print("\n\n")
# print(data["Firstname"])            # Select specific column

# SELECT SEVERAL COLUMNS
df = data[["Firstname","Lastname"]]   # Select two columns, extract to separate dataframe
# print(df)
# print("\n\n")

# SELECT COLUMN/ROW BY INDEX
# print(df.iloc[:,0])                 # Get first column, alternative way
# print(df.iloc[[0]])                 # Get first row
# print("\n\n")

# CHANGE VALUE IN CELL
# df["Firstname"][0] = "342"          # Insert "342" into specific cell, df["column_name"]["row_id"]
# print(df)
# print("\n\n")

# ADD CUSTOM COLUMN
# #array = ["value","value","value","value","value"]
# array = [1,1,1,1,1]
# df["new_column"] = array            # Add column to dataframe NOTE: array must be same length as dataframe
# print(df)
# print("\n\n")

# SHOW COLUMN DATA TYPES
# print(df.dtypes)                    # See what data type each column is
