from abc import ABC, abstractmethod


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print("QUACK")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")


class Squeak(QuackBehavior):
    def quack(self):
        print("SQUEAK")
