"""
    采用面向对象思想编写购物系统，使用MVC的设计
"""
class ShoppingMode:
    def __init__(self):
        """
        初始化所有的商品信息，使用字典的形式进行存储
        """
        self.__shopping_message={
                101: {"name": "屠龙刀", "price": 10000},
                102: {"name": "倚天剑", "price": 10000},
                103: {"name": "九阴白骨爪", "price": 8000},
                104: {"name": "九阳神功", "price": 9000},
                105: {"name": "降龙十八掌", "price": 8000},
                106: {"name": "乾坤大挪移", "price": 10000}
            } #私有的，只能读取不可修改

    @property
    def shopping_message(self):
        return self.__shopping_message

class Shopping_Controller:
    shopping01=ShoppingMode.shopping_message
    def __init__(self):
        self.order_of_goods=[]

    def buy_shopping(self):
        # while True:
        #     cid = int(input("请输入商品编号："))
        #     if cid in ShoppingMode.shopping_message:
        #         break
        #     else:
        #         print("该商品不存在")
        cid = int(input("请输入商品编号："))
        count = int(input("请输入购买数量："))
        self.order_of_goods.append({"cid": cid, "count": count})
        print("添加到购物车。")
        print(self.order_of_goods)
        print(ShoppingMode.shopping_message[cid])

    def open_of_purse(self):
        total_price = 0
        total_price = Shopping_Controller.shopping01(total_price)
        while True:
            real_pay = float(input("总价%d元，请输入金额：" % total_price))
            if real_pay >= total_price:
                print("购买成功，找回：%d元。" % (real_pay - total_price))
                self.order_of_goods.clear()
                break
            else:
                print("金额不足.")

class Shopping_view:
    def __init__(self):
        self.__shopping01 = ShoppingMode()
        self.__shopping02=Shopping_Controller()

    def display(self):
        while True:
            for key, value in self.__shopping01.shopping_message.items():
                print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))
            self.__shopping02.buy_shopping()
            self.__shopping02.open_of_purse()

shopping_of_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

stu=ShoppingMode()
# for key, value in stu.shopping_message.items():
#     print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))
# stu.shopping_message=shopping_of_info
st=Shopping_view()
st.display()


""""
shopping_of_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}
# 订单容器
order_of_goods = []
# 购买商品函数，需得到订单的编号和数量
def buy_shoppong():
    for key, value in shopping_of_info.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))
    while True:
        cid = int(input("请输入商品编号："))
        if cid in shopping_of_info:
            break
        else:
            print("该商品不存在")
    count = int(input("请输入购买数量："))
    order_of_goods.append({"cid": cid, "count": count})
    print("添加到购物车。")
# 结算函数,需将订单中容器的编号,找到对应商品的具体信息
def open_of_purse():
    total_price = 0
    total_price = shopping_info(total_price)
    while True:
        real_pay = float(input("总价%d元，请输入金额：" % total_price))
        if real_pay >= total_price:
            print("购买成功，找回：%d元。" % (real_pay - total_price))
            order_of_goods.clear()
            break
        else:
            print("金额不足.")


def shopping_info(total_price):
    for item in order_of_goods:
        per_of_shopping = shopping_of_info[item["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (per_of_shopping["name"], per_of_shopping["price"], item["count"]))
        total_price += per_of_shopping["price"] * item["count"]
    return total_price


def shopping():
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            buy_shoppong()
        elif item == "2":
            open_of_purse()

shopping()
"""