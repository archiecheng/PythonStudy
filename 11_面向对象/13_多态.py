#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/5 10:36
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 13_多态.py
# @Software: PyCharm
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def make_noise(animal: Animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)


# 演示抽象类

class AC:
    def cool_wind(self):
        pass

    def hot_wind(self):
        pass

    def swing_l_r(self):
        pass


class Media_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")

    def hot_wind(self):
        print("美的空调制热")

    def swing_l_r(self):
        print("美的空调左右摆风")

class GREE_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")

    def hot_wind(self):
        print("格力空调制热")

    def swing_l_r(self):
        print("格力空调左右摆风")


def make_cool(ac: AC):
    ac.cool_wind()

media = Media_AC()
gree = GREE_AC()

make_cool(media)
make_cool(gree)