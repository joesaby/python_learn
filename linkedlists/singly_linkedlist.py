import logging
log = logging.getLogger(__name__)


class SinglyLinkedList(object):
    def __init__(self):
        self._head = None
        self._tail = None

    def __iter__(self):
        """
        Override default iterator with a generator
        :return:
        """
        current_node = self._head
        while current_node:
            yield current_node
            current_node = current_node.get_next_node()

    def add_to_head(self, data):
        node = Node(data)
        if self._head:
            # Set the new node's next node to be current head
            # If only one node exists head & tail are same, so no update required to tail
            node.set_next_node(self._head)
        else:
            # Means tail doesnt exist too so set the tail
            self._tail = node
        self._head = node

    def add(self, data):
        """
        Simply adds to the tail
        :param data:
        :return:
        """
        node = Node(data)
        if self._tail:
            # Set the current tails next node to be the new node
            # If there was ever only one node, head & tail are same
            self._tail.set_next_node(node)
        else:
            # Means head also doesnt exist
            self._head = node
        self._tail = node

    def delete_node(self, key):
        previous_node = None
        for node in self :
            if node.get_data() == key:
                pass

    def delete_head(self):
        if self._head:
            self._head = self._head.get_next_node()
        # After resetting the current head, if head is null (ie if head
        # and tail were same), then set tail to null as well
        if not self._head:
            self._tail = None

    def delete_tail(self):
        if self._tail == self._head:
            self._tail = None
            self._head = None
            return

        second_last_node = None
        # At this stage you are guaranteed to have a list
        # of more that one element
        count = 0
        for node in self :
            # Traverse till the last node
            if not node.get_next_node():
                self._tail = second_last_node
                # Empty out next node
                self._tail.set_next_node()
                # If count of list is 1 then set the
                # head to be tail
                if count == 1:
                    self._head == self._tail
                return self._tail
            second_last_node = node
            count +=1

    #### For unit Testing ######
    def get_head(self):
        return self._head

    def get_tail(self):
        return self._tail

    #### For unit Testing Ends ######

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