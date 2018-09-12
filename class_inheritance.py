# -*-coding:utf-8
class Cars():
    def __init__(self, manufactor, model, years):
        self.manufactor = manufactor
        self.model = model
        self.years = years

    def get_info(self):
        """获取完整的车辆生产信息"""
        print('车辆简要信息如下：')
        print('生厂产商：%-s' % self.manufactor)
        print('车辆型号：%-s' % self.model)
        print('车辆出产年份：%-s' % str(self.years))


my_car = Cars('上海汽车', 'MG6', 2014)
my_car.get_info()
print('\n')


class ElectoricCar(Cars):
    """定义类的继承"""

    def __init__(self, manufactor, model, years):  # 初始化主类的属性。
        super(ElectoricCar, self).__init__(manufactor, model, years)  # 初始化子类的特有属性。
        self.battery_size = 16

    def get_battery(self):
        print("该车配备" + str(self.battery_size) + "KWh的里程电池.")


my_ecar = ElectoricCar('上海汽车', '荣威E550', 2018)
my_ecar.get_info()
my_ecar.get_battery()
print('\n')
