def generate_series(a: int):
    series = []
    for i in range(a):
        series.append(2 * i + 1)   # formula for odd numbers
    return series


# Example usage
print(generate_series(1))  # [1]
print(generate_series(2))  # [1, 3]
print(generate_series(3))  # [1, 3, 5]
print(generate_series(4))  # [1, 3, 5, 7]

# Taking user input
n = int(input("Enter a number: "))
print("Series:", generate_series(n))