import logging

# load_graph: str * int -> set * dict
def load_graph(fname, is_undirected=False, allow_multiple=False, allow_loop=False):
    logging.info("Loading a graph from {}".format(fname))
    logging.debug("  is_undirected: {}".format(is_undirected))
    logging.debug("  allow_multiple: {}".format(allow_multiple))
    logging.debug("  allow_loop: {}".format(allow_loop))

    pass
