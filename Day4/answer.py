import re
from typing import List, Mapping, Callable

input_file = "input.txt"

def parse_passports(filepath: str) -> List[str]:
    """Parses passports from a text file

    :param filepath: path to input file
    :return: dictionary of 'passports'
    """
    passports, passport = [], {}
    for line in open(filepath, "r"):
        if line == '\n':
            passports.append(passport)
            passport = {}
        else:
            line_data = line.split()
            for field in line_data:
                key, value = field.split(':')
                passport[key] = value
    passports.append(passport)
    return passports

def is_valid_passport(passport: Mapping[str, str], fields: Mapping[str, str]) -> bool:
    """Check if passport contains all given fields and field patterns

    :param passport: mapping of field name -> value
    :param fields: list of fields to be checked with regex patterns
    :return: true if all fields are present in passport and values match patterns
    """
    if all(key in passport.keys() for key in fields.keys()):
        for attribute, value in passport.items():
            if attribute in fields and not fields[attribute](value):
                return False
        print(passport)
        return True
    return False    

def count_valid_passports(passports: List[Mapping[str, str]], fields: Mapping[str, str]) -> int:
    """Counts number of valid passports in given passport list

    :param passports: list of passport mappings - field name -> value
    :param fields: list of fields to be checked with patterns
    :return: number of valid passports in list
    """
    count = 0
    for passport in passports:
        count += 1 if is_valid_passport(passport, fields) else 0
    return count

passports = parse_passports(input_file)

fields = {
    'byr': lambda x: int(x) >= 1920 and int(x) <= 2002,
    'iyr': lambda x: int(x) >= 2010 and int(x) <= 2020,
    'eyr': lambda x: int(x) >= 2020 and int(x) <= 2030,
    'hgt': lambda x: re.match(r"(?:1(?:[5-8]\d|9[0-3])cm|(?:59|6\d|7[0-6])in)", x),
    'hcl': lambda x: re.match(r"#[\da-f]{6}", x),
    'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    'pid': lambda x: re.match(r"\d{9}$", x),
}

print(count_valid_passports(passports, fields))