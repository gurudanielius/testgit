print("Hello World")
# This is a simple Python script that prints "Hello World" to the console.
# It serves as a basic example of a Python program.
#create a pandas DataFrame with two columns: 'Name' and 'Age', and add three rows of data to it. Then, print the DataFrame.
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}

#ziauriai rimtas sakinys su ziauriai rimtais zodziais
#additonal dataframe
data2= {
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Country': ['USA', 'USA', 'USA'],
    'Population': [8419600, 3980400, 2716000],
    'Area': [783.8, 503, 227.3]
}
df2 = pd.DataFrame(data2)
print(df2)


