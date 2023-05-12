import json
from collections import defaultdict

with open('data.json', 'r') as f:
    data = json.load(f)

# Turn the list of dictionaries into a single dictionary in O(n) time/space
dict_data = defaultdict(list)
{dict_data[key].append(sub_dict[key]) for sub_dict in data for key in sub_dict}

# Pull out the k:v pairs we want and load them into a new dictionary
# that's formatted in key=column name and value=column data (fields).
extracted_keys = ['name', 'address', 'position', 'available_bikes', 'banking']
transformed_data = {key:value for key, value in dict_data.items() if key in extracted_keys}

with open('transformed_data.json', 'w') as f:
    json.dump(transformed_data, f)