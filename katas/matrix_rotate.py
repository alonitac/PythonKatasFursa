def rotate_matrix(matrix):
    """
    Rotates the given square matrix 90 degrees clockwise in place.

    Args:
        matrix: the 2D square matrix to rotate
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i > j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]

    pass


def print_matrix(matrix):
    """
    Helper function to print a 2D matrix.

    Args:
        matrix: the matrix to print
    """
    for row in matrix:
        print(' '.join(str(value) for value in row))


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Original Matrix:")
    print_matrix(matrix)
    rotate_matrix(matrix)
    print("Matrix after 90-degree clockwise rotation:")
    print_matrix(matrix)

    # Expected output:
    # Original Matrix:
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # Matrix after 90-degree clockwise rotation:
    # 7 4 1
    # 8 5 2
    # 9 6 3