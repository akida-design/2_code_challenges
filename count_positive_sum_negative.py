def count_positives_sum_negatives(arr):
    if not arr:
        return []
    
    count_positives = sum(1 for x in arr if x > 0)
    sum_negatives = sum(x for x in arr if x < 0)
    
    return [count_positives, sum_negatives]

# Example usage:
input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
result = count_positives_sum_negatives(input_array)
print(result)  # Output: [10, -65]