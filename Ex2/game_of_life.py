def count_live_neighbors(matrix, row, col):
    rows = len(matrix)
    cols = len(matrix[0])
    live_neighbors = 0

    directions = [
        (-1, -1), (-1, 0), (-1, 1), (0, -1),
        (0, 1), (1, -1), (1, 0), (1, 1)
    ]


def next_generation(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    new_matrix = [[0 for i in range(cols)] for i in range(rows)]
    for row in range(rows):
        for col in range(cols):
            live_neighbors = count_live_neighbors(matrix, row, col)

    return new_matrix


def game_of_life(matrix, iterations=5):
    for i in range(iterations):
        matrix = next_generation(matrix)
    return matrix
