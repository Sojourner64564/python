def transpose(matrix):
    matrix[:] = [list(x) for x in zip(*matrix)]


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transpose(matrix)
    print(matrix)



matrix = [[1]]
transpose(matrix)
for line in matrix:
    print(*line)