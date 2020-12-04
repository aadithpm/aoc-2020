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

def traverse(pattern: List) -> int:
    """Traverses the pattern and counts number of trees encountered

    :param pattern: list of rows containing the pattern in each row
    :return: number of trees until we reach the bottom of the map
    """
    indices = generate_indices(0, 3, len(pattern), len(pattern[0]))
    target_indices = []
    trees, spaces = 0, 0
    for row, index in zip(pattern, indices):
        trees += 1 if row[index] == '#' else 0
        if row[index] == '#':
            target_indices.append(index)
        spaces += 1 if row[index] != '#' else 0
    return trees

input_data = parse_input(input_file)[1:]
print(traverse(input_data))