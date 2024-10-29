import pandas as pd 

#creating a data dictionary

raw_data = {"name" : ['bulbasar', 'Charman', 'Squirtle', 'caterpie'], "evolution": ['Ivysaur', 'Charmelon', 'Wartortle', 'Metapod'], "type": ['grass', 'fire','water','bug'],"hp": ['45','39','44','45'], "pokedex": ['yes','no','yes','no'], "place": ['park','street', 'lake','forest']}

pk = pd.DataFrame(raw_data)
print(pk.head()) 

pk = pk[['name', 'type', 'hp', 'evolution','pokedex']]
print("updated dataframe:")
print(pk)
print("\ndata Type:") 
print(pk.dtypes)
