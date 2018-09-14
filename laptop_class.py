# -*-coding:utf-8 -*-
class laptop():
    def __init__(self, vendor, model, ram_config):
        self.vendor = vendor
        self.model = model
        self.ram_config = ram_config

    def check_memory(self): # 检查内存操作。
        if self.ram_config <= 4:
            print("This computer has so less memory usage, we need add memory")
        else:
            print("The computer has more free memory there.")

    def lap_info(self):  # 显示电脑基本参数。
        print("This laptop was made by " + self.vendor + ". It's model is " + self.model + ". It has " \
              + str(self.ram_config) + "GB memory.")


my_lap = laptop('Thinkpad', 'T460', 8)
my_lap.lap_info()
my_lap.check_memory()