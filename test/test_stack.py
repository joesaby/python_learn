import unittest
import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

from stack.simple_stack import Stack

DATA = ["abcd", "defg", "hijk", "lmno"]

class StackTest(unittest.TestCase):

    def test_simple_push_pop(self):
        st_obj = Stack()
        st_obj.push("test_data")
        self.assertEquals (st_obj.pop(), "test_data")
        self.assertEquals(st_obj.pop(), None)

    def test_push_pop_2_elements(self):
        st_obj = Stack()
        for d in DATA[:2]:
            st_obj.push(d)

        # Validate
        pushed_list = []
        for val in st_obj:
            pushed_list.append(val.get_data())

        self.assertTrue(pushed_list[::-1], DATA[:2])
        # pop last
        st_obj.pop()

        pushed_list = []
        for val in st_obj:
            pushed_list.append(val.get_data())

        self.assertTrue(pushed_list[::-1][:1], DATA[:1])

    def test_push_pop_4_elements(self):
        """
        Create 4 elements by pushing element one by one
        Verify all 4 elements can be retrieved & they are stored in the reverse order of
            how they were pushed
        Delete last element & verify 3 elements exists in the above format too
        :return:
        """
        st_obj = Stack()
        for d in DATA:
            st_obj.push(d)

        # Validate
        pushed_list = []
        for val in st_obj:
            pushed_list.append (val.get_data())

        self.assertTrue(pushed_list[::-1], DATA)
        # pop last
        st_obj.pop()

        pushed_list = []
        for val in st_obj:
            pushed_list.append(val.get_data())

        self.assertTrue(pushed_list[::-1][:3], DATA[:3])