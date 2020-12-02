import functools
from typing import Mapping, Callable

input_file = "input.txt"

def parse_input(filepath: str) -> Mapping[str, tuple]:
    """Parses list of input args from a text file

    :param filepath: path to input file
    :return: dictionary of 'password': (character, lower limit, upper limit) for password requirements 
    """
    data = {}
    lines = [i.strip() for i in open(filepath, "r")]
    for line in lines:
        separated = line.split(':')
        reqs = separated[0].split('-')
        more_reqs = reqs[1].split()
        data[separated[1].strip()] = (more_reqs[1], int(reqs[0]), int(more_reqs[0]))
    return data

def is_valid_password_count(password: str, constraints: tuple) -> bool:
    """Validates passwords against a tuple of constraints

    :param password: password string
    :param constraints: tuple of requirements for password (character, min. count, max. count)
    :return: true if password is valid
    """
    return password.count(constraints[0]) >= constraints[1] and password.count(constraints[0]) <= constraints[2]

def is_valid_password_position(password: str, constraints: tuple) -> bool:
    """Validates passwords against a tuple of constraints

    :param password: password string
    :param constraints: tuple of requirements for password (character, first position, second position))
    :return: true if password is valid
    """
    return (password[constraints[1] - 1] == constraints[0]) ^(password[constraints[2] - 1] == constraints[0])

def valid_passwords_count(passwords: Mapping[str, tuple], validator: Callable[[str, tuple], bool]) -> int:
    """Returns count of valid passwords in the map

    :param passwords: mapping of password string -> requirements
    :param validator: validation function to check password
    """
    return len(list(filter(lambda x: validator(x[0], x[1]), passwords.items())))

input_data = parse_input(input_file)

print(valid_passwords_count(input_data, is_valid_password_count))
print(valid_passwords_count(input_data, is_valid_password_position))