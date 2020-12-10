import re
from typing import List, Mapping, Tuple
from collections import defaultdict

input_file = "input.txt"
JMP, ACC, NOP = 'jmp', 'acc', 'nop'

def parse_input(filepath: str) -> List[str]:
    """Parses list of input args from a text file

    :param filepath: path to input file
    :return: list of inputs 
    """
    return [i.strip() for i in open(filepath, "r")]

def find_loop_in_bootcode(cmds: List[str]) -> Tuple[int, bool]:
    """Runs list of bootcode commands and returns accumulator value when infinite loop starts

    :param cmds: list of bootcode commands - jmp, acc, nop
    :return: accumulator value when infinite loop starts and True if program terminated else False
    """
    seen, acc, line = set(), 0, 0
    while line < len(cmds) - 1 and line not in seen:
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

    return acc, line == len(cmds) - 1

def fix_infinite_loop(cmds: List[str]) -> int:
    """Fixes the infinite loop by changing each NOP or JMP command

    :param cmds: list of bootcode commands - jmp, acc, nop
    :return: accumulator value after infinite loops fixed
    """
    for idx, line in enumerate(cmds):
        old_cmd = line
        cmd, value = line.split()
        if cmd == NOP:
            cmd = JMP
        elif cmd == JMP:
            cmd = NOP
        cmds[idx] = f"{cmd} {value}"
        res = find_loop_in_bootcode(cmds)
        if res[1]:
            return res[0]
        cmds[idx] = old_cmd
    return -1


cmds = parse_input(input_file)
print(find_loop_in_bootcode(cmds))
print(fix_infinite_loop(cmds))