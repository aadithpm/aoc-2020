from typing import List
target = 2020
input_file = "input.txt"

def parse_input(filepath: str) -> List:
    """Parses list of input args from a text file

    :param filepath: path to input file
    :return: list of inputs
    """
    return [i.strip() for i in open(filepath, "r")]

def find_two_sum(i: List[int], n: int) -> int:
    """Returns product of x, y in a list where x + y = n

    :param i: list of numbers
    :param n: target sum

    :return: x * y where x and y are the two numbers in the list 
    that add up to n else -1
    """
    lookup = {}
    for number in map(lambda x: int(x), i):
        if n - number in lookup:
            return number * (n - number)
        lookup[number] = n - number

    return -1

def find_three_sum(i: List[int], n: int) -> int:
    """Returns product of x, y, z in a list where x + y + z = n

    :param i: list of numbers
    :param n: target sum

    :return: x * y * z where x, y and z are the three numbers in the list 
    that add up to n else -1
    """
    i = [int(_) for _ in i]
    for idx, number in enumerate(i):
        result = find_two_sum(i[idx + 1:], n - number)
        if result > 0:
            return number * result
    return -1

input_data = parse_input(input_file)

print(find_two_sum(input_data, target))
print(find_three_sum(input_data, target))