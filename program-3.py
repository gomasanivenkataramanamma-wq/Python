def generate_series(a: int):
    # If input is even, use (a-1) instead
    if a % 2 == 0:
        a -= 1

    series = []
    for i in range(a):
        series.append(2 * i + 1)   # odd number formula

    return ", ".join(map(str, series))


# Example usage
print(generate_series(1))  # 1
print(generate_series(2))  # 1
print(generate_series(3))  # 1, 3, 5
print(generate_series(4))  # 1, 3, 5
print(generate_series(5))  # 1, 3, 5, 7, 9
print(generate_series(6))  # 1, 3, 5, 7, 9

# For user input
n = int(input("Enter a number: "))
print("Series:", generate_series(n))