
class BubbleSort(object):

    def sort_fn(self, unsorted_list):
        sorted_list = unsorted_list
        list_len = len(unsorted_list)
        print sorted_list
        for k in range(list_len):
            sub_list = sorted_list[k:]
            sub_list_len = len(sub_list)
            for outer_idx, outer_value in enumerate(sorted_list[k:]):
                left_idx = outer_idx
                right_idx = outer_idx + 1
                if right_idx < sub_list_len:
                    left_val = sorted_list[left_idx]
                    right_val = sorted_list[right_idx]
                    if left_val > right_val :
                        sorted_list[ left_idx] = right_val
                        sorted_list[ right_idx] = left_val
                        print sorted_list

sorter = BubbleSort()
sorter.sort([32,33,15,1,4,6,5,10,5,7,8,9,11,2,12,2])