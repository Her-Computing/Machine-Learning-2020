import pandas as pd 

#converting dataset (list of lists) to pandas dataframe
data = [
  [3, 2, 0, 1], 
  [0, 3, 7, 2]
]

purchases = pd.DataFrame(data)
print(purchases)

#formatting dataframe better so it can be more readable
purchases = pd.DataFrame(data, columns=['June', 'Robert', 'Lily', 'David'], index = ['apples', 'oranges'])
print("\n", purchases)

#dataframe stats
print("\nColumn Names: ", purchases.columns)
print("\nShape of Dataframe: ", purchases.shape)
print("\nNumber of Null Values Per Column in Dataframe:", "\n", purchases.isnull().sum())

#accessing certain cols and rows of dataframe
print("\nJune's count of apples and oranges: \n", purchases['June']) #col
print("\nTotal count of apples and oranges: \n", purchases.loc['apples'])

#adding new data (rows) to dataframes
more_purchases = pd.DataFrame([[3, 5, 6, 7], [2, 6, 9, 4]], columns = purchases.columns, index = purchases.index)
print("\nSecond set of data: \n", more_purchases)

total_purchases = purchases.append(more_purchases)
print("\ncombined dataframe: \n", total_purchases)

#adding new data (cols) to dataframes
total_purchases['Tanish'] = [3, 7, 8 ,1]
print("\n", total_purchases)