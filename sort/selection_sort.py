
class SelectionSort(object):

    def sort_fn(self, unsorted_list):
        sorted_list = unsorted_list
        for outer_idx, outer_val in enumerate(sorted_list):
            min_val = outer_val
            min_val_idx = outer_idx
            for inner_idx, inner_value in enumerate(sorted_list[outer_idx:]):
                if inner_value < min_val :
                    min_val_idx = outer_idx + inner_idx
                    print "Resetting Current_Val [{}] to new MinVal [{}] in iteration [{}] at idx [{}]".format(min_val,
                                                                                                              inner_value,
                                                                                                              outer_idx,
                                                                                                              min_val_idx)
                    min_val = inner_value
            print "After iteration [{}], minval = [{}] at position [{}]".format(outer_idx, min_val, min_val_idx)
            sorted_list[min_val_idx] = outer_val
            sorted_list[outer_idx] = min_val

        print sorted_list



sorter = SelectionSort()
sorter.sort_fn([32,33,15,1,4,6,5,10,5,7,8,9,11,2,12,2])