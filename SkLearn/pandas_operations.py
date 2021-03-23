import pandas as pd 

#converting dataset (dictionary) to pandas dataframe
data = {
    'apples': [3, 2, 0, 1], 
    'oranges': [0, 3, 7, 2]
}

purchases = pd.DataFrame(data)
print(purchases)

#editing indexes of row for dataframe
purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
print("\n", purchases)

print("\nColumn Names: ", purchases.columns)
print("\nShape of Dataframe: ", purchases.shape)
print("\nNumber of Null Values Per Column in Dataframe:", "\n", purchases.isnull().sum())