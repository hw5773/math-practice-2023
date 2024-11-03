import argparse
import logging

alphabets = set("abcdefghijklmnopqrstuvwxyz")

def is_integer(exp):
    try:
        a = int(exp)
        return True
    except:
        return False

def eval(exp):
    logging.error("Not implemented yet")
    raise NotImplementedError

def syntax_checker(statement):
    logging.error("Not implemented yet")
    raise NotImplementedError

def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--statement", required=True, help="Statement to be proved", type=str)
    parser.add_argument("-l", "--log", help="Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)", type=str, default="INFO")

    args = parser.parse_args()
    return args

def main():
    args = command_line_args()
    logging.basicConfig(level=args.log)

    logging.info("statement: {}".format(args.statement))
    logging.info("syntax check result: {}".format(syntax_checker(args.statement)))

if __name__ == "__main__":
    main()
