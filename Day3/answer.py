from typing import List

input_file = "input.txt"

def parse_input(filepath: str) -> List[str]:
    """Parses list of input args from a text file

    :param filepath: path to input file
    :return: dictionary of 'password': (character, lower limit, upper limit) for password requirements 
    """
    return [i.strip() for i in open(filepath, "r")]

def generate_indices(start: int, step: int, size: int, limit: int) -> int:
    """Generate 'size' number of indices from start in increments of 'step' limiting by 'limit'

    :param start: start index
    :param step: increment
    :param size: number of indices to generate
    :param limit: maximum possible index in list
    :return: list of indices
    """
    indices = []
    while len(indices) < size:
        start += step
        indices.append(start)
    return list(map(lambda x: x % limit, indices))

def traverse(pattern: List, indices: List, step: int) -> int:
    """Traverses the pattern and counts number of trees encountered

    :param pattern: list of rows containing the pattern in each row
    :param indices: indices to check for the pattern
    :param step: number of rows to move down by
    :return: number of trees until we reach the bottom of the map
    """
    trees, spaces = 0, 0
    pattern = pattern[::step]
    print(pattern[0])
    indices = indices[:len(pattern)]
    for row, index in zip(pattern, indices):
        trees += 1 if row[index] == '#' else 0
        spaces += 1 if row[index] != '#' else 0
    return trees

input_data = parse_input(input_file)
steps = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

prod = 1
for step in steps:
    res = traverse(input_data[step[1]:], generate_indices(0, step[0], len(input_data), len(input_data[0])), step[1])
    prod *= res
print(prod)