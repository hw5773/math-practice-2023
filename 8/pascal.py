import sys
import argparse
import logging
from counting import combination

def pascal_triangle(n, k):
    pass

def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", required=True, metavar="<total level of a pascal triangle>", help="Total level of a pascal triangle", type=int)
    parser.add_argument("-k", "--row", required=True, metavar="<target row of interest>", help="Target row of interest", type=int)
    parser.add_argument("-l", "--log", help="Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)", type=str, default="INFO")

    args = parser.parse_args()
    return args

def main():
    args = command_line_args()
    logging.basicConfig(level=args.log)

    logging.info("n: {}".format(args.number))
    logging.info("k: {}".format(args.row))

    ret = pascal_triangle(args.number, args.row)

    logging.info("result: {}".format(ret))

if __name__ == "__main__":
    main()
