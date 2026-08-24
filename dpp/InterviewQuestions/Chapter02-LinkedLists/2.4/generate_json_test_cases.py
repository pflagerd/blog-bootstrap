
def rotate_string_right(string: str, n: int) -> str:
    return string[n:] + string[0:n]

def generate_python_test_case_for_all_rotations_of_given_string(string: str) -> str:
    test_case_number = 0

    s = ""
    for i in range(0, len(string)):
        if i != 0:
            s += ",\n"
        prototype_test_case_string = f'{{ "input": [ {{ "type": "string", "value": "\\"{string}"\\" }}, {{ "type": "string", "value": "\\"{rotate_string_right(string, i)}"\\" }} ], "expected output": {{ "type": "int", "value": "{i}" }}, "explanation": "Degenerate test case" }}'
        s += prototype_test_case_string
        test_case_number += 1

    return s

# Example usage
if __name__ == "__main__":
    prototype_string = "The quick brown fox jumps over the lazy dog"

    print(generate_python_test_case_for_all_rotations_of_given_string(prototype_string))

