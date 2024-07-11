import pandas as pd

print("\nRead Csv file\n")
# pd.options.display.max_rows = 9999
csv_data = pd.read_csv("Day -9/matches.csv")
print(csv_data)

print("\n\nRead Json file\n")
json = pd.read_json("Day -9/data.json")
print(json)


# head method is use to print the first data from the table
data = pd.read_csv("Day -9/matches.csv")
print("\nhead()\n")
print(data.head(10)) # head(10) method is print first 10 rows from the csv file 
print(data.head()) # if value is not assign then it will print 5 rows

# tail methos is use the print the last data from the table
print(data.tail(10)) # tail(10) method is print last 10 rows from the csv file 
print(data.tail()) # if value is not assign then it will print 5 rows

# info() method is use to print the all information about the dataframe object
print(data.info())
