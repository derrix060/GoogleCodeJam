def solve_it():
    n = int(input())
    numbers = [int(x) for x in input().split(' ')]

    right_numbers = []
    left_numbers = []
    # odd index numbers only can change with odd index numbers.
    for i, number in enumerate(numbers):
        if i%2:
            right_numbers.append(number)
        else:
            left_numbers.append(number)

    # right_numbers and left_numbers can be sorted but not between themselfs.
    right_numbers.sort()
    left_numbers.sort()

    numbers = [None] * n
    # Check if merging the two lists they continue sorted
    # Populate left
    numbers[::2] = left_numbers
    numbers[1::2] = right_numbers

    # Check validity
    for idx in range(n - 1):
        if numbers[idx] > numbers[idx + 1]:
            return idx

    return 'OK'


t = int(input())

for case in range(1, t+1):
    answer = solve_it()
    print('Case #{}: {}'.format(case, answer))