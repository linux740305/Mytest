#-*- cofing : utf-8 -*-
class Cat:
    def __init__(self, new_name, new_age):
        self.name = new_name
        self.age = new_age
    def eat(self):
        print("貓在吃魚")
    def drink(self):
        print("貓喝可樂")
    def introduce(self):
        print("%s的年齡是%d"%(self.name, self.age))
tom = Cat("湯姆", 40)
tom.eat()
tom.drink()
#tom.name = "湯姆"
#tom.age = 40
tom.introduce()

lanmao = Cat("藍貓", 10)
#lanmao.name = "藍貓"
#lanmao.age = 10
lanmao.introduce()
#print("%s的年齡是%d"%(tom.name,tom.age))
