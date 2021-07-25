"""
     将２０４８游戏定义到此类当中
"""
import random


class GameCoreController:
    def __init__(self):
        self.__list_merge = None
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.__flag=0   #是否可进行移动的标志

    @property
    def map(self):
        return self.__map

    def zero_element_end(self):
        """
        零元素移到末尾
        :return:
        """
        for idex_element in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[idex_element] == 0:
                del self.__list_merge[idex_element]
                self.__list_merge.append(0)
            else:
                continue

    def adjacent_element_merage(self):
        """
        元素的合并：
                 1、元素先移动
                 2、然后相邻元素相加
        :return:
        """
        self.zero_element_end()
        for element_index in range(len(self.__list_merge) - 1):
            if self.__list_merge[element_index] == self.__list_merge[element_index + 1]:
                self.__list_merge[element_index] = 2 * self.__list_merge[element_index]
                self.__list_merge[element_index + 1] = 0
                self.__flag+=1
        self.zero_element_end()


    def left_list_move(self):
        """
        通过调用单个一维列表左移算法，来对二维列表数组进行数值的改变
        """
        for element in self.__map:
            self.__list_merge = element
            self.adjacent_element_merage()

    def right_list_move(self):
        for element in self.__map:
            self.__list_merge = element[::-1]  # 切片创建新列表
            self.adjacent_element_merage()  # 调整新列表
            element[::-1] = self.__list_merge  # 将新列表中的数据反向放入一维列表中

            # list_merge=element
            # adjacent_element_merage()
            # zero_element_end()
            # element[::-1]=list_merge

    def __squre_reverse(self):
        """
            可变类型的数据传参时，函数内部可以改变原数据
        :param list01: 列表参数
        :return: 无
        """
        for i in range(len(self.__map)):
            for c in range(len(self.__map)):
                if i >= c:
                    continue
                self.__map[i][c], self.__map[c][i] = self.__map[c][i], self.__map[i][c]

    def move_down(self):
        """
           矩阵的转置
           向左移动
           再转置
        """
        self.__squre_reverse()
        self.left_list_move()
        self.__squre_reverse()

    def move_up(self):
        """
           先转置
           向右对齐
           再转置
        :return:
        """
        self.__squre_reverse()
        self.right_list_move()
        self.__squre_reverse()

    def random_number(self):
        """
        　　　　在空位置随机产生一个２，或者４
        :return:无
        """
        random_probility=random.randint(1,10)
        if(random_probility<9):
            map_number=2
        else:
            map_number=4
        map_zero=[]#
        for r in range(len(self.__map)):
            for c in range(len(self.__map)):
                if self.__map[r][c]==0:
                    map_zero.append([r,c])
        random_map_zero=random.randint(0,len(map_zero)-1)
        self.__map[map_zero[random_map_zero][0]][map_zero[random_map_zero][1]]=map_number

    def is_game_over(self):
        """
        　　　判断游戏是否结束
        :return:
        """
        if self.__is_empty_position()==False and self.__flag==0:
            return False
        return True

    def __is_empty_position(self):
        """
        判断有没有空位置
        :return: Boolen
        """
        for r in range(len(self.__map)):
            for c in range(len(self.__map)):
                if self.__map[r][c]==0:
                    return True
        return False





# if __name__ == '__main__':
#     g01 = GameCoreController()
#     print(g01.map)
#     g01.random_number()
#     print("_____________________")
#     print(g01.map)
