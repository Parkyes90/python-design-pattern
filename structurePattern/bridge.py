import math
from abc import ABCMeta, abstractmethod


class IBaseOperationImplementor(metaclass=ABCMeta):
    @abstractmethod
    def add(self, first_number, second_number):
        pass

    @abstractmethod
    def subtract(self, first_number, second_number):
        pass

    @abstractmethod
    def multiply(self, first_number, second_number):
        pass

    @abstractmethod
    def divide(self, first_number, second_number):
        pass


class BaseOperation(IBaseOperationImplementor):
    def __init__(self):
        pass

    def add(self, first_number, second_number):
        return first_number + second_number

    def subtract(self, first_number, second_number):
        return first_number - second_number

    def multiply(self, first_number, second_number):
        return first_number * second_number

    def divide(self, first_number, second_number):
        return first_number / second_number


class OperationAbstraction:
    def __init__(self, impl):
        self.impl = impl

    def add(self, first_number, second_number):
        return self.impl.add(first_number, second_number)

    def subtract(self, first_number, second_number):
        return self.impl.subtract(first_number, second_number)

    def multiply(self, first_number, second_number):
        return self.impl.multiply(first_number, second_number)

    def divide(self, first_number, second_number):
        return self.impl.divide(first_number, second_number)


class RefinedOperationAbstraction(OperationAbstraction):
    def __init__(self, impl):
        OperationAbstraction.__init__(self, impl)

    def sqrt(self, a):
        return math.sqrt(a)

    def pow(self, a, b):
        return math.pow(a, b)


if __name__ == "__main__":
    first_number = 100
    second_number = 20
    operation_abstraction = RefinedOperationAbstraction(BaseOperation())
    print(
        f"{first_number}+{second_number}={operation_abstraction.add(first_number, second_number)}"
    )
    print(
        f"{first_number}-{second_number}={operation_abstraction.subtract(first_number, second_number)}"
    )
    print(
        f"{first_number}*{second_number}={operation_abstraction.multiply(first_number, second_number)}"
    )
    print(
        f"{first_number}/{second_number}={operation_abstraction.divide(first_number, second_number)}"
    )
    print(operation_abstraction.sqrt(100))
    print(operation_abstraction.pow(10, 2))
