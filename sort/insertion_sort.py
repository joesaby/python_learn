
class InsertionSort(object):

    def sort_fn(self, unsorted_list):

        sorted_list = unsorted_list
        for i in range (1, len(sorted_list)):
            newValue = sorted_list[i]
            j = i
            while j > 0 and sorted_list[j - 1] > newValue:
                sorted_list[j] = sorted_list[j - 1]
                j -=1

            sorted_list[j] = newValue;
        print sorted_list

sorter = InsertionSort()
sorter.sort_fn([33,32,15,1,4,6,5,10,5,7,8,9,11,2,12,2])