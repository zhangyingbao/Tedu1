"""
    2048核心算法
"""
list_merge = [2, 0, 0, 2]

# 1.定义函数,将list_merge列表中的0元素移到末尾
def zero_element_end():
    """
    零元素移到末尾
    """
    for idex_element in range(len(list_merge)-1,-1,-1):
        if list_merge[idex_element] == 0:
            del list_merge[idex_element]
            list_merge.append(0)
        else:
            continue

# 2.定义函数，将list_merge中的元素合并（相邻元素相同即合并）
def adjacent_element_merage():
    """
    元素的合并：
             1、元素先移动
             2、然后相邻元素相加
    """
    zero_element_end()
    for element_index in range(len(list_merge)-1):
        if list_merge[element_index]==list_merge[element_index+1]:
            list_merge[element_index]=2*list_merge[element_index]
            list_merge[element_index+1]=0
    zero_element_end()

# 3.定义函数，将二维列表map中的元素向左移动
map=[
    [2,0,0,2],
    [2,4,4,2],
    [0,4,2,0],
    [2,0,2,0],
]
# 将二维列表map中的元素左移
def left_list_move():
    """
    通过调用单个一维列表左移算法，来对二维列表数组进行数值的改变
    """
    global list_merge  #global声明成全局变量，使得一维列表指向二维列表
    for element in map:
        list_merge=element
        adjacent_element_merage()

# 将二维列表map中的元素右移
def right_list_move():
    global list_merge
    for element in map:
        list_merge=element[::-1]#切片创建新列表
        adjacent_element_merage()#调整新列表
        element[::-1]=list_merge #将新列表中的数据反向放入一维列表中

        # list_merge=element
        # adjacent_element_merage()
        # zero_element_end()
        # element[::-1]=list_merge


def squre_reverse(list01):
    """
        可变类型的数据传参时，函数内部可以改变原数据
    :param list01: 列表参数
    :return: 无
    """
    for i in range(len(list01)):
        for c in range(len(list01)):
            if i >= c:
                continue
            list01[i][c], list01[c][i] = list01[c][i], list01[i][c]

def move_down():
    """
       矩阵的转置
       向左移动
       再转置
    """
    squre_reverse(map)
    left_list_move()
    squre_reverse(map)

def move_up():
    """
       先转置
       向右对齐
       再转置
    :return:
    """
    squre_reverse(map)
    right_list_move()
    squre_reverse(map)

# zero_element_end()
# adjacent_element_merage()
right_list_move()
# left_list_move()
# move_up()
for items in map:
    print(items)
