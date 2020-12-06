input_file = "input.txt"

input_data = [i for i in open(input_file, "r").read().split('\n\n')]
print(sum(len(set(i)) for i in [i.replace('\n', '') for i in input_data]))
print(sum(len(j) for i in input_data for j in set.intersection(*map(set, i.split('\n')))))