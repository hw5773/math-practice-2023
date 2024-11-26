import os
import sys
import argparse
import logging
from func import load_graph

# degree_of_vertice: set * dict -> dict
# This function returns degree of each vertice in a dictionary form (e.g, ret["a"] = 3) for an undirected simple graph
def degree_of_vertice(graph):
    pass

# is_isomorphic: (set * dict) * (set * dict) -> bool
# This function returns True if two given graphs are isomorphic; otherwise, it returns False
def is_isomorphic(graph1, graph2):
    pass

def check_duplicated(funcs, f):
    pass

def bijections(domain, codomain):
    pass
   
def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--graph1", required=True, metavar="<graph file name 1>", help="Graph file name 1", type=str)
    parser.add_argument("-j", "--graph2", metavar="<graph file name 2>", help="Graph file name 2", type=str)
    parser.add_argument("-u", "--undirected", help="If a graph is undirected", action='store_true')
    parser.add_argument("-m", "--multigraph", help="If a graph allows multiple edges", action='store_true')
    parser.add_argument("-n", "--loop", help="If a graph allows loops", action='store_true')
    parser.add_argument("-l", "--log", help="Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)", type=str, default="INFO")

    args = parser.parse_args()
    return args

def main():
    args = command_line_args()
    logging.basicConfig(level=args.log)

    if not os.path.exists(args.graph1):
        logging.error("The path of the first graph does not exist: {}".format(args.graph1))
        sys.exit(1)

    if args.graph2 and not os.path.exists(args.graph2):
        logging.error("The path of the second graph does not exist: {}".format(args.graph2))
        sys.exit(1)

    is_undirected = False
    if args.undirected:
        is_undirected = True

    allow_multiple = False
    if args.multigraph:
        allow_multiple = True

    allow_loop = False
    if args.loop:
        allow_loop = True

    if args.graph1 and not args.graph2:
        graph = load_graph(args.graph1, is_undirected, allow_multiple, allow_loop)
        logging.debug("Vertex of Graph: {}".format(graph[0]))
        logging.debug("Edge of Graph: {}".format(graph[1]))
        if args.undirected and not allow_multiple and not allow_loop:
            logging.info("Degree of Each Vertex: {}".format(degree_of_vertice(graph)))
    elif args.graph1 and args.graph2:
        graph1 = load_graph(args.graph1, True, False, False)
        logging.debug("Vertex of Graph1: {}".format(graph1[0]))
        logging.debug("Edge of Graph1: {}".format(graph1[1]))
        graph2 = load_graph(args.graph2, True, False, False)
        logging.debug("Vertex of Graph2: {}".format(graph2[0]))
        logging.debug("Edge of Graph2: {}".format(graph2[1]))

        logging.info("Are Graph1 and Graph2 isomorphic?: {}".format(is_isomorphic(graph1, graph2)))

if __name__ == "__main__":
    main()
