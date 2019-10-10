import random

def quick_sort(array, start, end):
    '''
    平均时间复杂度O(nlog(n)), 最坏O(n^2)
    :param array:
    :return:
    '''
    if end <=  start:
        return

    pivot_key = partition(array, start, end)
    quick_sort(array, start, pivot_key-1)  # 排pivot左边的
    quick_sort(array, pivot_key + 1, end)  # 排pivot右边的


def partition(array, start, end):
    '''
    找一个基准下标index，使得在index之前的数全比index的值小，之后的比index的值大
    思想分为三步：1.随便找个值当哨兵 2.找到这个哨兵应该在的位置（找基准下标）3. 把哨兵放进去
    平均时间复杂度O(log(n)), 最坏O(n)
    :param array:
    :param start:
    :param end:
    :return:
    '''
    pivot_index = random.randint(start, end) # sample一个index，这个index的值作为哨兵

    swap(array, pivot_index, end)  # 哨兵放在在最后

    smaller_than_pivot_index = start - 1  # 用于计算比哨兵小的数的index, 初始为samll-1,因为还没比较，不知道small是不是比哨兵小
    for i in range(start, end+1):
        if array[i] < array[end]:
            smaller_than_pivot_index += 1  # 表示找到比哨兵小的数，他所在的下标应该是smaller_than_pivot_index，从而使得他所在的下标应该是smaller_than_pivot_index之前的数都比哨兵小
            if smaller_than_pivot_index != i:  # 当前的值虽然比哨兵小，但他所在的位置不对（因为比哨兵小的应该在smaller_than_pivot_index之前），所以当前应该与smaller_than_pivot_index位置的数交换
                swap(array, i, smaller_than_pivot_index)

    # 循环结束，smaller_than_pivot_index之前的（包括smaller_than_pivot_index）都比哨兵小
    smaller_than_pivot_index += 1  # 所以smaller_than_pivot_index+1应该是这个基准下标的位置，找到基准下标
    swap(array, smaller_than_pivot_index, end) # 把哨兵放到基准下标里

    return smaller_than_pivot_index

def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]

    return array

array = [3,4,2,5,10,1,-1,0,4,1,6,-2]
quick_sort(array, 0, len(array)-1)
print(array)