
def rotate_string_right(string: str, n: int) -> str:
    return string[n:] + string[0:n]

def generate_python_test_case_for_all_rotations_of_given_string(string: str) -> str:
    test_case_number = 0

    s = ""
    for i in range(0, len(string)):
        prototype_test_case = f"def test_{test_case_number}(self):\n    self.assertEqual({i}, rotationOffset(\"{prototype_string}\", \"{rotate_string_right(prototype_string, i)}\"))"
        s += prototype_test_case + "\n\n"
        test_case_number += 1

    return s

# Example usage
if __name__ == "__main__":
    prototype_string = "The quick brown fox jumps over the lazy dog"

    print(generate_python_test_case_for_all_rotations_of_given_string(prototype_string))

