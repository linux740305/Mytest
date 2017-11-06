#-*- cofing : utf-8 -*-
class Cat:
    def eat(self):
        print("貓在吃魚")
    def drink(self):
        print("貓喝可樂")
    def uu(self):
        print("%s的年齡是%d"%(self.name, self.age))
tom = Cat()
tom.eat()
tom.drink()
tom.name = "湯姆"
tom.age = 40
tom.uu()

lanmao = Cat()
lanmao.name = "藍貓"
lanmao.age = 10
lanmao.uu()
