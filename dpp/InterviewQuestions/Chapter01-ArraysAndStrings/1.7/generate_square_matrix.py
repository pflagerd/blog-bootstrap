def generate_square_matrix(n: int) -> list[list[int]]:
    return [[n * row + col + 1 for col in range(n)] for row in range(n)]


# Example usage
if __name__ == "__main__":
    for size in [2, 3, 4, 10]:
        matrix = generate_square_matrix(size)
        row_number = 1
        print("[", end="")
        for row in matrix:
            if row_number != 1:
                print(", ", end="")
            row_number += 1
            print(f"{row}", end="")
        print("]")
