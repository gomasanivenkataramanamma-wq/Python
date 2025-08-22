# Input list
numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

# Dictionary comprehension to count multiples
multiples_count = {i: sum(1 for num in numbers if num % i == 0) for i in range(1, 10)}

print(multiples_count)