# Classes and Inheritance

```python
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

````

* @property
* @staticmethod
* 
# Data Classes

* No explisit init function

```python
from dataclasses import dataclass, field
from enum import Enum, auto


class FriendType(Enum):
    STRAAT = auto()
    SKOOL = auto()
    VARSITY = auto()


@dataclass
class myMetaClass:
    # There is no init method
    tipe_vriend: FriendType  # This value needs te be passed
    name: str = ""
    friends: list[str] = field(default_factory=list)

    def __post_init__(self):
        """The post init method is called after the variables above is initialised"""
        self.add_friend('default')

    def add_friend(self, friend: str) -> None:
        self.friends.append(friend)


Klass1 = myMetaClass(FriendType.SKOOL)
Klass2 = myMetaClass(FriendType.SKOOL, name='Tobie')
Klass3 = myMetaClass(FriendType.VARSITY, name='Sandra', friends=['Lukas', "Willie"])
Klass3.add_friend(friend='Jurie')

print(Klass1.tipe_vriend)
print(Klass1.name)
print(Klass2.name)
print(Klass3.friends)

```

# Protocol

* Defines an interface of an object it can receive
* If it doen not compeltely look like a duck, but it can quack like a duck then call the quack method

```python
from typing import Protocol


class Flyer(Protocol):
    def fly(self) -> None:
        """A Flyer can fly"""


class FlyingHero:
    """This hero can fly, which is BEAST."""

    def fly(self):
        print("flying")


class RunningHero:
    """This hero can run. Better than nothing!"""

    def run(self):
        print('running')

    def fly(self):
        print('running')


class Board:
    """An imaginary game board that doesn't do anything."""

    def make_fly(self, obj: Flyer) -> None:  # <- Here's the magic
        """Make an object fly."""
        return obj.fly()


def main() -> None:
    board = Board()
    board.make_fly(FlyingHero())
    board.make_fly(RunningHero())
```

# Abstract Base Classes

* Forces the subclasses of the main class to implement certain methods

```python

from abc import ABC, abstractmethod
from enum import Enum, auto


class Education(Enum):
    DEGREE = auto
    TECH = auto
    SCHOOL = auto


class Employee(ABC):
    def __init__(self, name: str, education_level: Education):
        self.name = name
        self.eudcation_level = education_level

    @abstractmethod
    def calculate_pay(self):
        pass


class Temp(Employee):
    def __init__(self, name: str, education_level: Education, hours: int, pay: int):
        Employee.__init__(self, name, education_level)
        self.hours = hours
        self.pay = pay

    @property
    def calculate_pay(self):
        return self.hours * self.pay


t1 = Temp(name="Tobie", education_level=Education.DEGREE, hours=2010, pay=100)

print(t1.calculate_pay)


```

# META

* Rewire the class at instantiation

```python

class SomeMetaClass(type):
    # overriding the new method of the metaclass
    def __new__(mcs, name, bases, dct):
        x = super().__new__(mcs, name, bases, dct)
        # defining that each class with this metaclass
        # should have a variable, x with a default value
        x.attr = 100
        return x


# defining a class with Meta as its metaclass instead
# of type
class Foo(metaclass=SomeMetaClass):
    pass


# printing the variables in our newly defined class
print(Foo.attr)
```
