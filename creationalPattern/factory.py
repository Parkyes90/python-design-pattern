from abc import ABCMeta, abstractmethod


class AbstractOperation(metaclass=ABCMeta):
    def __init__(self):
        self.first_number = 0
        self.second_number = 0

    def operate(self):
        first_number = self.get_first_number()
        second_number = self.get_second_number()
        operator = self.get_operator()

        operator_description = operator.get_description()

        answer = operator.get_answer(first_number, second_number)

        result = (
            f"{first_number}{operator_description}{second_number} = {answer}"
        )

        print(result)

    @abstractmethod
    def get_operator(self):
        pass

    def get_first_number(self):
        return self.first_number

    def set_first_number(self, first_number):
        self.first_number = first_number

    def get_second_number(self):
        return self.second_number

    def set_second_number(self, second_number):
        self.second_number = second_number


class AbstractOperator(metaclass=ABCMeta):
    @abstractmethod
    def get_answer(self, first_number, second_number):
        pass

    @abstractmethod
    def get_description(self):
        pass


class AddOperation(AbstractOperation):
    def get_operator(self):
        return AddOperator()


class SubtractOperation(AbstractOperation):
    def get_operator(self):
        return SubtractOperator()


class MultiplyOperation(AbstractOperation):
    def get_operator(self):
        return MultiplyOperator()


class DivideOperation(AbstractOperation):
    def get_operator(self):
        return DivideOperator()


class AddOperator(AbstractOperator):
    def get_answer(self, first_number, second_number):
        return first_number + second_number

    def get_description(self):
        return "+"


class SubtractOperator(AbstractOperator):
    def get_answer(self, first_number, second_number):
        return first_number - second_number

    def get_description(self):
        return "-"


class MultiplyOperator(AbstractOperator):
    def get_answer(self, first_number, second_number):
        return first_number * second_number

    def get_description(self):
        return "*"


class DivideOperator(AbstractOperator):
    def get_answer(self, first_number, second_number):
        return first_number / second_number

    def get_description(self):
        return "/"


if __name__ == "__main__":
    first_number = 100
    second_number = 20

    operations = [
        AddOperation(),
        SubtractOperation(),
        MultiplyOperation(),
        DivideOperation(),
    ]

    for operation in operations:
        operation.set_first_number(first_number)
        operation.set_second_number(second_number)

        operation.operate()
