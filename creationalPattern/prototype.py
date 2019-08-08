from abc import ABCMeta, abstractmethod


class AbstractOperationPrototype(metaclass=ABCMeta):
    def __init__(self, operation=None):
        if operation is not None:
            self.first_number = operation.first_number
            self.second_number = operation.second_number
        else:
            self.first_number = 0
            self.second_number = 0

    @abstractmethod
    def get_clone(self):
        pass

    def get_first_number(self):
        return self.first_number

    def get_second_number(self):
        return self.second_number

    def set_first_number(self, first_number):
        self.first_number = first_number

    def set_second_number(self, second_number):
        self.second_number = second_number

    @abstractmethod
    def get_answer(self, first_number, second_number):
        pass

    @abstractmethod
    def get_operator(self):
        pass

    def operate(self):
        first_number = self.get_first_number()
        second_number = self.get_second_number()

        operator = self.get_operator()

        answer = self.get_answer(first_number, second_number)
        print(f"{first_number}{operator}{second_number}={answer}")


class AddOperationPrototype(AbstractOperationPrototype):
    def get_clone(self):
        return AddOperationPrototype(self)

    def get_answer(self, first_number, second_number):
        return first_number + second_number

    def get_operator(self):
        return "+"

    def __init__(self, operation=None):
        AbstractOperationPrototype.__init__(self, operation)


class SubtractOperationPrototype(AbstractOperationPrototype):
    def get_clone(self):
        return SubtractOperationPrototype(self)

    def get_answer(self, first_number, second_number):
        return first_number - second_number

    def get_operator(self):
        return "-"

    def __init__(self, operation=None):
        AbstractOperationPrototype.__init__(self, operation)


class MultiplyOperationPrototype(AbstractOperationPrototype):
    def get_clone(self):
        return MultiplyOperationPrototype(self)

    def get_answer(self, first_number, second_number):
        return first_number * second_number

    def get_operator(self):
        return "*"

    def __init__(self, operation=None):
        AbstractOperationPrototype.__init__(self, operation)


class DivideOperationPrototype(AbstractOperationPrototype):
    def get_clone(self):
        return DivideOperationPrototype(self)

    def get_answer(self, first_number, second_number):
        return first_number / second_number

    def get_operator(self):
        return "/"

    def __init__(self, operation=None):
        AbstractOperationPrototype.__init__(self, operation)


class Client:
    def __init__(self):
        self.operation_prototype = None
        self.operation_prototype_map = {}
        self.__init_operation_map()

    def operate(self):
        self.operation_prototype.operate()

    def set_operation(self, operator, first_number, second_number):
        self.operation_prototype = self.get_operation_clone(operator)
        self.operation_prototype.set_first_number(first_number)
        self.operation_prototype.set_second_number(second_number)

    def __init_operation_map(self):
        self.operation_prototype_map["+"] = AddOperationPrototype()
        self.operation_prototype_map["-"] = SubtractOperationPrototype()
        self.operation_prototype_map["*"] = MultiplyOperationPrototype()
        self.operation_prototype_map["/"] = DivideOperationPrototype()

    def get_operation_clone(self, operator):
        operation = self.operation_prototype_map[operator]
        return operation.get_clone()


if __name__ == "__main__":
    client = Client()
    first_number = 100
    second_number = 20
    operators = ("+", "-", "*", "/")
    for operator in operators:
        client.set_operation(operator, first_number, second_number)
        client.operate()
