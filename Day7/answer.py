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

def make_graph(bags: List[str]) -> Mapping[str, List[Tuple[int, str]]]:
    """Construct a 1 bag -> n bags graph from list of rules

    :param bags: list of bag rules
    :return: graph represented as a key-value mapping
    """
    graph = {}
    for rule in bags:
        parent, children = rule.split(" bags contain")
        children = re.findall(r'(\d+) ([a-zA-Z ]+) bag[s]?', children.strip())
        graph[parent] = children
    return graph


def count_paths(graph: Mapping[str, List[Tuple[int, str]]], label: str) -> int:
    """Count all paths to node with 'label' in graph. We search backward from the target node until we
    exhaust all paths

    :param graph: graph as a dict -> bag key-value mapping i.e x bag can contain n of y bags
    :param label: node to search for
    :return: number of paths to node i.e how many bags can eventually contain bag 'label'
    """
    inverted_graph = defaultdict(list)
    for parent, children in graph.items():
        for child in children:
            inverted_graph[child[1]].append(parent)

    seen, stack = set(), [label]
    while stack:
        node = stack.pop()
        for parent in inverted_graph[node]:
            if parent not in seen:
                seen.add(parent)
                stack.append(parent)
    return len(seen)

def weighted_count_children(graph: Mapping[str, List[Tuple[int, str]]], label: str) -> int:
    """Count all paths from node to leaf nodes and do a weighted sum. We search forward from the target until
    we exhaust all paths

    :param graph: graph as a dict -> bag key-value mapping i.e x bag can contain n of y bags
    :param label: node to search from
    :return: number of paths to node i.e how many bags does bag 'label' eventually contain
    """
    def helper(node):
        """Recursive helper to do a weighted sum on child nodes

        :param node: get children of this node
        """
        return sum(
            int(count) + int(count) * helper(child) for count, child in graph[node]
        )
    
    return helper(label)

rules = parse_input(input_file)
graph = make_graph(rules)
print(count_paths(graph, 'shiny gold'))
print(weighted_count_children(graph, 'shiny gold'))