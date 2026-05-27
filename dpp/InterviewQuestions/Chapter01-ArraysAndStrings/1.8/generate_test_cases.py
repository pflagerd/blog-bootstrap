def generate_test_cases(M: int, N: int, zeros: list[list[int]]) -> list[list[int]]:
    return [[N * row + col + 1 for col in range(N)] for row in range(M)]


# Example usage
if __name__ == "__main__":
    for arguments in [[2, 3, [[0, 0]]], [3, 1, [[]]], [4, 7, [[]]], [10, 10,[[]]]]:
        matrix = generate_test_cases(arguments[0], arguments[1], arguments[2])
        row_number = 1
        print("[", end="")
        for row in matrix:
            if row_number != 1:
                print(", ", end="")
            row_number += 1
            print(f"{row}", end="")
        print("]")
