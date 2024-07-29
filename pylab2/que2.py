def add_element(set_a, element):
    """Adds an element to a set, safely handling duplicates."""
    set_a.add(element)

def remove_element(set_a, element):
    """Removes an element from a set, safely handling non-existence."""
    if element in set_a:
        set_a.remove(element)

def union(set_a, set_b):
    """Returns the union of two sets."""
    return set_a | set_b

def intersection(set_a, set_b):
    """Returns the intersection of two sets."""
    return set_a & set_b

def difference(set_a, set_b):
    """Returns the difference of two sets (S1 - S2)."""
    return set_a - set_b

def is_subset(set_a, set_b):
    """Checks if set_a is a subset of set_b."""
    return set_a.issubset(set_b)

def set_length(set_a):
    """Calculates the length of a set without using len()."""
    count = 0
    for _ in set_a:
        count += 1
    return count

def symmetric_difference(set_a, set_b):
    """Returns the symmetric difference of two sets."""
    return set_a ^ set_b

def power_set(set_a):
    """Calculates the power set of a given set."""
    power_set = [set()]
    for element in set_a:
        new_subsets = [subset | {element} for subset in power_set]
        power_set.extend(new_subsets)
    return power_set

def unique_subsets(set_a):
    """Returns all unique subsets of a given set."""
    return power_set(set_a)

# Example usage:
set1 = {1, 2, 3}
set2 = {2, 3, 4}

add_element(set1, 4)
print(set1)  # Output: {1, 2, 3, 4}

remove_element(set1, 5)  # No error, element not present

print(union(set1, set2))  # Output: {1, 2, 3, 4}
print(intersection(set1, set2))  # Output: {2, 3}
print(difference(set1, set2))  # Output: {1}
print(is_subset(set1, set2))  # Output: False

print(set_length(set1))  # Output: 4

print(symmetric_difference(set1, set2))  # Output: {1, 4}

print(power_set(set1))  # Output: [{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]
print(unique_subsets(set1))  # Output: [{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]
