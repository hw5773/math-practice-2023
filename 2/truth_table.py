import re
import argparse
import logging
import copy
import time
from operators import *

def extract_variables(expression):
    sorted_variable_set = sorted(set(re.findall(r'\b[a-z]\b', expression)))
    return sorted_variable_set

def make_combinations(nvar):
    if nvar == 0:
        combinations = [[]]
    else:
        tmp = make_combinations(nvar - 1)
        combinations = []
        for c in tmp:
            c1 = copy.copy(c)
            c2 = copy.copy(c)
            c1.append(True)
            c2.append(False)
            combinations.append(c1)
            combinations.append(c2)
    logging.debug("nvar: {}, combinations: {}".format(nvar, combinations))
    return combinations

def truth_table(expression):
    vlst = extract_variables(expression)
    nvar = len(vlst)
    combinations = make_combinations(nvar)

    for c in combinations:
        logging.debug("c (before): {}".format(c))
        for idx in range(nvar):
            e = "{}={}".format(vlst[idx], c[idx])
            logging.debug(e)
            exec(e)
        ret = eval(expression)
        c.append(ret)
        logging.debug("c (after): {}".format(c))

    return combinations

def print_truth_table(expression):
    vlst = extract_variables(expression)
    table = truth_table(expression)

    logging.debug("vlst: {}".format(vlst))
    logging.debug("table: {}".format(table))

    for v in vlst:
        print ("{}\t".format(v), end="")
    print(expression)

    for row in table:
        for e in row:
            print ("{}\t".format(e), end="")
        print("")

def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--exp", required=True, help="Expression", type=str)
    parser.add_argument("-l", "--log", help="Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)", type=str, default="INFO")

    args = parser.parse_args()
    return args

def main():
    args = command_line_args()
    logging.basicConfig(level=args.log)

    logging.info("Expression: {}".format(args.exp))
    logging.debug("  Extracted variables: {}".format(extract_variables(args.exp)))
    print_truth_table(args.exp)

if __name__ == "__main__":
    main()
