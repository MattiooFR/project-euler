# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:


def read_triangle_array(path):
    with open(path) as data_file:
        col_number = len(data_file.readlines()[-1].split(" "))
    with open(path) as data_file:
        triangle_array = []
        for i, line in enumerate(data_file):
            triangle_array.append(
                [int(value) for value in line.strip().split(" ")]
                + [0 for i in range(col_number - i - 1)]
            )
    return triangle_array


def make_sum(path):
    triangle_array = read_triangle_array(path)
    reversed_array = triangle_array[::-1]
    while len(reversed_array) > 1:
        for j in range(0, len(reversed_array[0]) - 1):
            if (
                reversed_array[0][j] + reversed_array[1][j]
                > reversed_array[0][j + 1] + reversed_array[1][j]
            ):
                reversed_array[1][j] = reversed_array[0][j] + reversed_array[1][j]
            else:
                reversed_array[1][j] = reversed_array[0][j + 1] + reversed_array[1][j]
        else:
            if len(reversed_array) > 1:
                del reversed_array[0]
    return max(reversed_array[0])


print(make_sum("p067_triangle.txt"))
# Answer 7273
