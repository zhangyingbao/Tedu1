from bll import GameCoreController


class GameConsoleView:
    def __init__(self):
        self.__console=GameCoreController() #类名的括号很重要

    def start(self):
        while True:
            if self.__console.is_game_over()==False:
                break
            else:
                self.__console.random_number()
                self.__console.random_number()
                self.interface_draw()
                controller_direction=input("请输入WSAD方向：")
                if controller_direction=="w":
                    self.__console.move_up()
                elif controller_direction=="s":
                    self.__console.move_down()
                elif controller_direction=="a":
                    self.__console.left_list_move()
                elif controller_direction=="d":
                    self.__console.right_list_move()
        print("游戏结束！！！")


    def interface_draw(self):
        for r in range(len(self.__console.map)):
            for c in range(len(self.__console.map)):
                print(self.__console.map[r][c],end="  ")
            print("")
