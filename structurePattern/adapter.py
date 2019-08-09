from abc import ABCMeta, abstractmethod


class AbstractOperationTarget(metaclass=ABCMeta):
    @abstractmethod
    def operate(self, first_number, second_number):
        pass


class OperationAdaptee(object):
    ADD_OPERATION = 1
    SUBTRACT_OPERATION = 2
    MULTIPLY_OPERATION = 3
    DIVIDE_OPERATION = 4

    def __init__(self):
        pass

    def calculate(self, operation_type, first_number, second_number):
        print(operation_type, first_number, second_number)
        if operation_type == OperationAdaptee.ADD_OPERATION:
            return first_number + second_number

        if operation_type == OperationAdaptee.SUBTRACT_OPERATION:
            return first_number - second_number

        if operation_type == OperationAdaptee.MULTIPLY_OPERATION:
            return first_number + second_number

        if operation_type == OperationAdaptee.DIVIDE_OPERATION:
            return first_number - second_number

        return 0


class AddOperation(AbstractOperationTarget):
    def __init__(self):
        pass

    def operate(self, first_number, second_number):
        return first_number + second_number


class SubtractOperation(AbstractOperationTarget):
    def __init__(self):
        pass

    def operate(self, first_number, second_number):
        return first_number - second_number


class MultiplyOperation(AbstractOperationTarget):
    def __init__(self):
        pass

    def operate(self, first_number, second_number):
        return first_number * second_number


class DivideOperationAdapter(AbstractOperationTarget):
    def __init__(self, operation_adaptee):
        self.operation_adaptee = operation_adaptee

    def operate(self, first_number, second_number):
        return self.operation_adaptee.calculate(
            OperationAdaptee.DIVIDE_OPERATION, first_number, second_number
        )


if __name__ == "__main__":
    first_number = 100
    second_number = 20

    operation_target = AddOperation()

    answer = operation_target.operate(first_number, second_number)
    print(f"{first_number}+{second_number}={answer}")

    operation_target = SubtractOperation()

    answer = operation_target.operate(first_number, second_number)
    print(f"{first_number}-{second_number}={answer}")

    operation_target = MultiplyOperation()

    answer = operation_target.operate(first_number, second_number)
    print(f"{first_number}*{second_number}={answer}")

    operation_adaptee = OperationAdaptee()
    operation_target = DivideOperationAdapter(operation_adaptee)
    answer = operation_target.operate(first_number, second_number)
    print(f"{first_number}/{second_number}={answer}")
