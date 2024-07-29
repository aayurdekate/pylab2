# Functions for handling multiple dictionaries

def merging_Dict(*args):
    """Merges multiple dictionaries into one."""
    merged_dict = {}
    for dictionary in args:
        merged_dict.update(dictionary)
    return merged_dict

def common_keys(*args):
    """Finds common keys in multiple dictionaries."""
    if not args:
        return set()
    common = set(args[0].keys())
    for dictionary in args[1:]:
        common &= set(dictionary.keys())
    return common

def invert_dict(d):
    """Inverts a dictionary, swapping keys and values.
       If multiple keys have the same value, group these keys in a list."""
    inverted_dict = {}
    for key, value in d.items():
        if value not in inverted_dict:
            inverted_dict[value] = [key]
        else:
            inverted_dict[value].append(key)
    return inverted_dict

def common_key_value_pairs(*args):
    """Finds common key-value pairs across multiple dictionaries."""
    if not args:
        return {}
    common_pairs = set(args[0].items())
    for dictionary in args[1:]:
        common_pairs &= set(dictionary.items())
    return dict(common_pairs)

# Demonstration with examples

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}
dict3 = {'a': 1, 'c': 3, 'd': 6}

# Merging dictionaries
merged = merging_Dict(dict1, dict2, dict3)
print("Merged Dictionary:", merged)

# Finding common keys
common_keys_result = common_keys(dict1, dict2, dict3)
print("Common Keys:", common_keys_result)

# Inverting a dictionary
inverted_dict = invert_dict(dict1)
print("Inverted Dictionary:", inverted_dict)

# Finding common key-value pairs
common_kv_pairs = common_key_value_pairs(dict1, dict2, dict3)
print("Common Key-Value Pairs:", common_kv_pairs)
