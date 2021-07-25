"""
    数据模型类：StudentMode1
        数据：编号 id,姓名 name,年龄 age,成绩 score,
    逻辑控制类：StudentManagerController
        数据：学生列表__stu_list
        行为：获取列表 stu_list 添加学生 add_student 删除学生 remove_student
"""


class StudentMode1:
    def __init__(self, name="", age=0, score=0, id=0):
        self.name = name
        self.age = age
        self.score = score
        self.id = id


class StudentManagerController:
    # 编号：系统自动生成
    init_id = 1000
    @classmethod
    def atomatic_add(cls, stu):
        stu.id = cls.init_id
        cls.init_id += 1

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def get_list(self, id):
        """
           获取列表
        :param id: 根据id
        :return :返回对应的学生信息
        """
        for item in self.__stu_list:
            if id == item.id:
                return item

    def add_student(self, stu):
        """
          添加元素信息
        :param stu: 数据模型对象
        :return: 无
        """
        StudentManagerController.atomatic_add(stu)
        self.__stu_list.append(stu)

    def remove_student(self, id):
        """
          删除学生信息
        :param id: 根据学生id
        :return: 无
        """
        list_remove = self.get_list(id)
        if list_remove != None:
            self.__stu_list.remove(list_remove)
        else:
            print("无此学号，请重新输入！！！")

    def update_student(self, new_stu_message):
        """
             修改学生信息
        :param new_stu_message: 要修改的学生信息
        :return: 无
        """
        old_stu_message = self.get_list(new_stu_message.id)
        if old_stu_message == None:
            self.add_student(new_stu_message)
        else:
            old_stu_message.name = new_stu_message.name
            old_stu_message.age = new_stu_message.age
            old_stu_message.score = new_stu_message.score

    def order_by_student(self):
        """
           根据成绩升序排列
        :return:
        """
        for r in range(len(self.__stu_list) - 1):
            for c in range(r + 1, len(self.__stu_list)):
                if self.__stu_list[r].score > self.__stu_list[c].score:
                    self.__stu_list[r], self.__stu_list[c] = self.__stu_list[c], self.__stu_list[r]


class StudentManagerView:

    def __init__(self):
        """
        初始化：逻辑控制项
        """
        self.__manager = StudentManagerController()

    def __dispaly(self):
        """
        显示菜单
        :return: 无
        """
        print("1） 添加学生信息")
        print("2） 显示学生信息")
        print("3） 删除学生信息")
        print("4） 修改学生信息")
        print("5） 按照学生成绩升序排列显示")
        print("---------------------")

    def __select_menu_item(self):
        """
          选择菜单项
        :return: 无
        """
        input_select = input("请选择：")
        if input_select == "1":
            self.__input_students()
        elif input_select == "2":
            self.__output_student()
        elif input_select == "3":
            self.__delete_student()
        elif input_select == "4":
            self.__modify_student()
        elif input_select == "5":
            self.__order_student()
        else:
            print("输入错误，请重新输入！")

    def main(self):
        """
          入口逻辑
        :return:
        """
        while True:
            self.__dispaly()
            self.__select_menu_item()

    def __input_students(self):
        """
          添加学生
        :return: 无
        """
        name = input("姓名：")
        age = int(input("年龄："))
        score = int(input("成绩："))
        stu01 = StudentMode1(name, age, score)
        self.__manager.add_student(stu01)

    def __output_student(self):
        """
          输出学生
        :return: 无
        """
        for i in self.__manager.stu_list:
            print("学号：", i.id, " 姓名：", i.name, " 年龄：", i.age, " 成绩：", i.score)

    def __delete_student(self):
        """
        删除学生，根据学号进行删除
        :return:
        """
        delste_stu_ID = int(input("删除学生的学号："))
        self.__manager.remove_student(delste_stu_ID)

    def __modify_student(self):
        """
         学生信息的修改
        :return:
        """
        print("请在下边输入学生的基本信息：")
        ID = int(input("请输入修改学生的学号："))
        name = input("姓名：")
        age = int(input("年龄："))
        score = int(input("成绩："))
        stu01 = StudentMode1(name, age, score)
        stu01.id = ID
        self.__manager.update_student(stu01)

    def __order_student(self):
        """
        根据学生成绩的高低进行排序
        :return:
        """
        self.__manager.order_by_student()
        self.__output_student()


stu = StudentManagerView()
stu.main()
