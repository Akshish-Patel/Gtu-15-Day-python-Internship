import pandas as pd

# pandas library is generaly use to formate the data in tabular format and modify tha data

data = {
    'Name' : ['Akshish', 'Shubham', 'Stavan', 'Neel'],
    'Marks' : [45, 78, 90, 95],
    'Gender' : ['Male', 'Male', 'Male', 'Male'],
    'Mobile No' : [1234567890, 9087654321, 6543217809, 4567893219]
}

# DataFrame is use to represent the data into tabular format
df = pd.DataFrame(data)
print(df)
print("\nName\n",df['Name']) 
print("Max marks from this dataframe = ", df['Marks'].max())

# we can change the index of dataframe bydefault index is starts with 0(zero)
index = ['one', 'two', 'three', 'four']
df = pd.DataFrame(data, index)
print("\n",df) 

# serice method is use the represent the 1-D data into tabular format
print("\n\nSerice\n")

data = [1,2,3,4,5]
no = pd.Series(data) # in series index is bydefault starts from zero(0)
print(no)
print("no[1] = ",no[1])
print("no[3] = ",no[3],"\n")

# we can change the index of the data 
no = [1,2,3]
index = ['x', 'y', 'z'] 
nos = pd.Series(no, index)
print(nos)
print("no[x] = ",nos['x'])
print("no[z] = ",nos['z'],"\n")

# we can also pass the data into key-value format

data = {
    "Student 1" : "Akshish",
    "Student 2" : "Stavan",
    "Student 3" : "Dhruv",
    "Student 4" : "Shubham"
}

students = pd.Series(data)
print("\n",students)
print("\nstudents[Student 2] = ",students['Student 2'])
print("students[Student 4] = ",students['Student 4'])