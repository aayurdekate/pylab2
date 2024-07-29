def find_max(data_list):
    """Finds the maximum value in a list."""
    if not data_list:
        raise ValueError("List cannot be empty")
    return max(data_list)

def find_min(data_list):
    """Finds the minimum value in a list."""
    if not data_list:
        raise ValueError("List cannot be empty")
    return min(data_list)

def calculate_sum(data_list):
    """Calculates the sum of all elements in a list."""
    if not data_list:
        raise ValueError("List cannot be empty")
    return sum(data_list)

def compute_average(data_list):
    """Computes the average of the elements in a list."""
    if not data_list:
        raise ValueError("List cannot be empty")
    return sum(data_list) / len(data_list)  # Handle division by zero

def find_median(data_list):
    """Finds the median of a sorted list."""
    if not data_list:
        raise ValueError("List cannot be empty")

    sorted_list = sorted(data_list)  # Create a copy to avoid modifying the original list
    length = len(sorted_list)
    if length % 2 == 0:
        # Even-length list: median is the average of the middle two elements
        mid1 = length // 2 - 1
        mid2 = length // 2
        return (sorted_list[mid1] + sorted_list[mid2]) / 2
    else:
        # Odd-length list: median is the middle element
        mid = length // 2
        return sorted_list[mid]
