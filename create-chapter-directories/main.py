import sys
import os

chapter_names = [
    "Arrays and Strings",
    "Linked Lists",
    "Stacks and Queues",
    "Trees and Graphs",
    "Bit Manipulation",
    "Math and Logic Puzzles",
    "Object Oriented Design",
    "Recursion and Dynamic Programming",
    "System Design and Scalability",
    "Sorting and Searching",
    "Testing",
    "C and C++",
    "Java",
    "Databases",
    "Threads and Locks"
]

def main(args):
    i = 1
    for chapter_name in chapter_names:
        os.makedirs(f"Chapter{i:02d}-{chapter_name.title().replace(" ", "")}", exist_ok=True)
        i += 1
    return 0

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sys.exit(main(sys.argv))
