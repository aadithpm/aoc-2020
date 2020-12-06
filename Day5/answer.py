from typing import List, Set, Callable
from math import ceil

input_file = "input.txt"

def parse_input(filepath: str) -> List[str]:
    """Parses list of input args from a text file

    :param filepath: path to input file
    :return: list of inputs 
    """
    return [i.strip() for i in open(filepath, "r")]

def binary_search(seat_str: str, high: int, shifts: Set[str]) -> int:
    """Standard binary search to find number specified by a string based on pre-defined shifts

    :param seat_str: seat string made up of 'F', 'B', 'L' or 'R'
    :param high: upper limit for search range
    :param shifts: characters that control range limiting
    :return: row/column number
    """
    l, h = 0, high
    for char in seat_str:
        if char in shifts:
            h = l + (h - l) // 2
        else:
            l = l + ceil((h - l) / 2)
    return (h + l) // 2

def calc_seat_number(row: int, col: int) -> int:
    return row * 8 + col

def find_seat_id(seat_str: str, search: Callable[[str, int, Set[str]], int], seat_number_fn: Callable[[int, int], int]) -> int:
    """Find seat ID from a seat string

    :param seat_str: seat string made up of 'F', 'B', 'L' or 'R'
    :param seat_number_fn: callable that calculates seat ID from a row and column
    :return: seat ID
    """
    r, c = binary_search(seat_str[:-3], 127, {'F', 'L'}), binary_search(seat_str[-3:], 7, {'F', 'L'})
    return seat_number_fn(r, c)

input_data = parse_input(input_file)

seat_ids = list(map(lambda x: find_seat_id(x, binary_search, calc_seat_number), input_data))
first, last = min(seat_ids), max(seat_ids)
print(last)
print(set(range(first, last)) - set(seat_ids))