import re
from typing import List, Mapping, Tuple
from collections import defaultdict

input_file = "input.txt"

def parse_input(filepath: str) -> List[str]:
    """Parses list of input args from a text file

    :param filepath: path to input file
    :return: list of inputs 
    """
    return [i.strip() for i in open(filepath, "r")]

def find_loop_in_bootcode(cmds: List[str]) -> int:
    """Runs list of bootcode commands and returns accumulator value when infinite loop starts

    :param cmds: list of bootcode commands - jmp, acc, nop
    :return: accumulator value when infinite loop starts
    """
    seen, acc, line = set(), 0, 0
    JMP, ACC, NOP = 'jmp', 'acc', 'nop'
    while line not in seen:
        cmd, value = cmds[line].split()
        value = int(value)
        seen.add(line)
        if cmd == JMP:
            line += value
        elif cmd == ACC:
            acc += value
            line += 1
        elif cmd == NOP:
            line += 1
    return acc

cmds = parse_input(input_file)
print(find_loop_in_bootcode(cmds))