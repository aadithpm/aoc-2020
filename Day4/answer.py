from typing import List, Mapping

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
    return passports

def is_valid_passport(passport: Mapping[str, str], fields: List[str]) -> bool:
    """Check if passport contains all given fields

    :param passport: mapping of field name -> value
    :param fields: list of fields to be checked
    :return: true if all fields are present in passport
    """
    return all(key in passport.keys() for key in fields)

def count_valid_passports(passports: List[Mapping[str, str]], fields: List[str]) -> int:
    """Counts number of valid passports in given passport list

    :param passports: list of passport mappings - field name -> value
    :param fields: list of fields to be checked
    :return: number of valid passports in list
    """
    count = 0
    for passport in passports:
        count += 1 if is_valid_passport(passport, fields) else 0
    return count

passports = parse_passports(input_file)
fields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
]

print(count_valid_passports(passports, fields))