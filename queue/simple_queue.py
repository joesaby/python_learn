import logging
log = logging.getLogger(__name__)

class Queue(object):

    def __init__(self):
        self._top = None

    def __iter__(self):
        """
        Override default iterator with a generator
        :return:
        """
        current_node = self._top
        while current_node:
            yield current_node
            current_node = current_node.get_next_node()

    def push(self, data):
        """
        Push data to the top of the queue
        :param data:
        :return:
        """
        new_node = Node(data, self._top)
        self._top = new_node

    def pop(self):
        """
        Pop data from top of queue
        :return:
        """
        if not self._top:
            return None

        ret_val = self._top.get_data()
        self._top = self._top.get_next_node()
        return ret_val

class Node(object):

    def __init__(self, data, next_node = None):
        self._data = data
        self._next_node = next_node

    def get_next_node(self):
        return self._next_node

    def am_i_last(self):
        return True if self._next_node is None else False

    def set_next_node(self, node = None):
        prev_node = self._next_node
        self._next_node = node
        log.debug("I am {}, My next node is {}".format(self._data,
                                                       self._next_node.get_data() if self._next_node else None))
        return prev_node

    def get_data(self):
        return self._data

    def __eq__(self, node):
        assert (isinstance(node, Node))
        return self._data == node.get_data()

    def __str__(self):
        return self._data