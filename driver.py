import argparse

parser = argparse.ArgumentParser(description='Parser for the n-puzzle game')

"""Possible Values:
    bfs (Breadth-First Search)
    dfs (Depth-First Search)
    ast (A-Star Search)
    ida (IDA-Star Search)
"""
parser.add_argument('function', action="store")

"""
    Possible Value: A List of numbers
"""
parser.add_argument('state', action="store")

results = parser.parse_args()


# Solves the state given by the user using the search method given by the user
option = eval(results.function + "([{}])".format(results.state))

def
