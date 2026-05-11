def generate_input_matrix(M: int, N: int) -> list[list[int]]:
    return [[N * row + col + 1 for col in range(N)] for row in range(M)]


# Example usage
if __name__ == "__main__":
    for size in [[2, 3], [3, 1], [4, 7], [10, 10]]:
        matrix = generate_input_matrix(size[0], size[1])
        row_number = 1
        print("[", end="")
        for row in matrix:
            if row_number != 1:
                print(", ", end="")
            row_number += 1
            print(f"{row}", end="")
        print("]")
