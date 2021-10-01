from abc import ABC, abstractmethod

from Strategy.FlyBehavior import FlyBehavior, FlyWithWings, FlyNoWay
from Strategy.QuackBehavior import QuackBehavior, Quack, MuteQuack


class Duck(ABC):
    flyBehavior: FlyBehavior
    quackBehavior: QuackBehavior

    def perform_fly(self):
        self.flyBehavior.fly()

    def perform_quack(self):
        self.quackBehavior.quack()

    def perform_swim(self):
        print("I can swim!")

    @abstractmethod
    def display(self):
        pass


class MallardDuck(Duck):
    def __init__(self):
        self.flyBehavior = FlyWithWings()
        self.quackBehavior = Quack()

    def display(self):
        print("I'm real MallardDuck")


class ModelDuck(Duck):
    def __init__(self):
        self.flyBehavior = FlyNoWay()
        self.quackBehavior = MuteQuack()

    def display(self):
        print("I'm the Model")
