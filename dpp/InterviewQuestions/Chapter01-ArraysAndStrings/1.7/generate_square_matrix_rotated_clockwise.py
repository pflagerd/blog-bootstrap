def generate_square_matrix_rotated_clockwise(n: int) -> list[list[int]]:
#    return [[n * row + col + 1 for col in range(n)] for row in range(n)]
    output_matrix = [[0] * n for _ in range(n)]
    i = 1
    for col in range(n - 1, -1, -1):
        for row in range(n):
            output_matrix[row][col] = i
            i += 1
    return output_matrix

# Example usage
if __name__ == "__main__":
    for size in [2, 3, 4, 10]:
        matrix = generate_square_matrix_rotated_clockwise(size)
        row_number = 1
        print("[", end="")
        for row in matrix:
            if row_number != 1:
                print(", ", end="")
            row_number += 1
            print(f"{row}", end="")
        print("]")
