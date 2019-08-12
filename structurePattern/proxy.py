from abc import ABCMeta, abstractmethod


class AbstractOperationSubject(metaclass=ABCMeta):
    @abstractmethod
    def operate(self, first_number, second_number):
        pass


class AddOperationSubject(AbstractOperationSubject):
    def operate(self, first_number, second_number):
        return first_number + second_number


class SubtractOperationSubject(AbstractOperationSubject):
    def operate(self, first_number, second_number):
        return first_number - second_number


class MultiplyOperationSubject(AbstractOperationSubject):
    def operate(self, first_number, second_number):
        return first_number * second_number


class DivideOperationSubject(AbstractOperationSubject):
    def operate(self, first_number, second_number):
        return first_number / second_number


class OperationException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class DivideOperationProxy(AbstractOperationSubject):
    def __init__(self, real_operation_subject):
        self.real_operation_subject = real_operation_subject

    def operate(self, first_number, second_number):
        if second_number == 0:
            raise OperationException("NonZeroDivideException")
        return self.real_operation_subject.operate(first_number, second_number)


if __name__ == "__main__":
    first_number = 100
    second_number = 20
    operation_subject = AddOperationSubject()
    result = operation_subject.operate(first_number, second_number)
    print(f"{first_number}+{second_number}={result}")
    operation_subject = SubtractOperationSubject()
    result = operation_subject.operate(first_number, second_number)
    print(f"{first_number}-{second_number}={result}")
    operation_subject = MultiplyOperationSubject()
    result = operation_subject.operate(first_number, second_number)
    print(f"{first_number}*{second_number}={result}")
    operation_subject = DivideOperationProxy(DivideOperationSubject())
    result = operation_subject.operate(first_number, second_number)
    print(f"{first_number}/{second_number}={result}")

    operation_subject = DivideOperationProxy(DivideOperationSubject())
    first_number = 10
    second_number = 0

    try:
        result = operation_subject.operate(first_number, second_number)
    except OperationException as e:
        print(e)
