from typing import List, Mapping, Tuple, Set

input_file = "input.txt"

def parse_input(filepath: str) -> List[int]:
    """Parses list of integer input args from a text file

    :param filepath: path to input file
    :return: list of integer inputs 
    """
    return [int(i.strip()) for i in open(filepath, "r")]

def in_preamble(nums: List[int], target: int) -> bool:
    """Checks if target is the sum of any two numbers in nums

    :param nums: list of numbers to check against
    :param target: number to check
    :return: True if number is a sum of any two in tne preamble else False
    """
    nums = set(nums)
    for num in nums:
        if target - num in nums:
            return True
    return False

def check_preamble(nums: List[int], start: int) -> int:
    """Returns the first number that is not a sum of any two in the preamble

    :param nums: list of numbers to check from
    :param start: index to start from
    :return: first number that is not a sum of two numbers in the preamble
    """
    for idx, num in enumerate(nums[start:]):
        if not in_preamble(nums[start + idx - 25: start + idx], num):
            return num
    return -1

def encryption_addition(nums: List[int]) -> int:
    """Addition for contigious set of numbers for encryption weakness

    :param nums: list of contigious numbers from original list
    :return: sum of smallest and largest number in the set
    """
    return min(nums) + max(nums)

def find_encryption_weakness(nums: List[int], target: int) -> int:
    """Finds a contigious set of numbers in nums that sum to target and adds the smallest and largest number in that set

    :param nums: list of numbers to check from
    :param target: set should add up to this number
    :return: sum of smallest and largest number in contigious set
    """
    for window_size in range(2, len(nums)):
        window, idx = nums[:window_size], 1
        while idx < len(nums) - window_size:
            if sum(window) == target:
                return encryption_addition(window)
            idx += 1
            window = nums[idx:window_size + 1]
    return -1

input_data = parse_input(input_file)
target = check_preamble(input_data, 25)
print(target)
print(find_encryption_weakness(input_data, target))