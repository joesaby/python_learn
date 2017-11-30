import unittest
import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

from linkedlists.singly_linkedlist import SinglyLinkedList , Node

DATA = ["abcd", "defg", "hijk", "lmno"]

class SingleLinkedListTests(unittest.TestCase):

    def test_add_to_head(self):
        ret_list = []
        ll = SinglyLinkedList()
        for el in DATA:
            ll.add_to_head(el)
            self.assertTrue(ll.get_head() == Node(el))
        for retdata in ll:
            ret_list.append(retdata.get_data())
        self.assertEquals(ret_list[::-1], DATA, "Expect return list to be a reverse of added list")

    def test_add_to_tail(self):
        ret_list = []
        ll = SinglyLinkedList()
        for el in DATA:
            ll.add(el)
            self.assertTrue(ll.get_tail() == Node(el))
        for retdata in ll:
            ret_list.append(retdata.get_data())
        self.assertEquals(ret_list, DATA, "Expect return list to be the same as added list")

    def test_delete_tail(self):
        ll = SinglyLinkedList()
        # Only one node where Test tail & head are same
        ll.add("some")
        self.assertEquals(ll.get_head().get_data(), "some")
        self.assertEquals(ll.get_tail().get_data(), "some")
        ll.delete_tail()
        self.assertEquals(ll.get_head(), None)
        self.assertEquals(ll.get_tail(), None)

    def test_delete_tail_list_contains_2_items(self):
        ll = SinglyLinkedList()
        for el in DATA[:2]:
            ll.add(el)
        ll.delete_tail()
        self.assertEquals(ll.get_head().get_data(), DATA[0])
        self.assertEquals(ll.get_tail().get_data(), DATA[0])

    def test_delete_tail_list_contains_more_than_2_items(self):
        ll = SinglyLinkedList()
        for el in DATA:
            ll.add(el)

        ll.delete_tail()
        log.debug("Current Tail {}".format(ll.get_tail().get_data()))
        self.assertEquals(ll.get_head().get_data(), DATA[0])
        self.assertEquals(ll.get_tail().get_data(), DATA[len(DATA) - 2])