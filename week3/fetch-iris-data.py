from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
X = iris.data.features 
y = iris.data.targets 
  
# number of records 
print("Total number of records in the file: ", len(X))

different_flowers = []
for line in y['class']:
  if line not in different_flowers:
    different_flowers.append(line)

# number of different flowers
print("Total number of different flower available: ", len(different_flowers))

# names of different flowers
print("Names of all different flowers in the dataset: ", different_flowers)
