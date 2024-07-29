import module_ListFunction as mlf  # Import with shorter alias

# Create lists using Python comprehension
numbers = [10, 20, 30, 40, 50]
mixed_list = [1, "hello", 3.14, True]
empty_list = []

# Demonstrate function usage
print("Maximum value:", mlf.find_max(numbers))
print("Minimum value:", mlf.find_min(numbers))
print("Sum:", mlf.calculate_sum(numbers))
print("Average:", mlf.compute_average(numbers))

try:
    print("Median (numbers):", mlf.find_median(numbers))  # Handles non-numeric values
except TypeError:
    print("Median calculation not applicable for mixed data types.")

print("Median (empty list):")
try:
    mlf.find_median(empty_list)  # Raises ValueError for empty list
except ValueError as e:
    print(e)
