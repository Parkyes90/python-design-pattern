from abc import ABCMeta, abstractmethod


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_first_number()
        self.builder.build_operator()
        self.builder.build_second_number()
        self.builder.build_answer()

        result = self.builder.get_result()

        print(result)


class AbstractOperationBuilder(metaclass=ABCMeta):
    def __init__(self, first_number, second_number):
        self.result = ""
        self.first_number = first_number
        self.second_number = second_number

    @abstractmethod
    def operate(self, first_number, second_number):
        pass

    @abstractmethod
    def build_operator(self):
        pass

    def build_first_number(self):
        self.result += str(self.first_number)

    def build_second_number(self):
        self.result += str(self.second_number)

    def build_answer(self):
        answer = self.operate(self.first_number, self.second_number)
        self.result += " = "
        self.result += str(answer)

    def get_result(self):
        return self.result


class AddOperationBuilder(AbstractOperationBuilder):
    def __init__(self, first_number, second_number):
        AbstractOperationBuilder.__init__(self, first_number, second_number)

    def operate(self, first_number, second_number):
        return first_number + second_number

    def build_operator(self):
        self.result += " + "


class SubtractOperationBuilder(AbstractOperationBuilder):
    def __init__(self, first_number, second_number):
        AbstractOperationBuilder.__init__(self, first_number, second_number)

    def operate(self, first_number, second_number):
        return first_number - second_number

    def build_operator(self):
        self.result += " - "


class MultiplyOperationBuilder(AbstractOperationBuilder):
    def __init__(self, first_number, second_number):
        AbstractOperationBuilder.__init__(self, first_number, second_number)

    def operate(self, first_number, second_number):
        return first_number * second_number

    def build_operator(self):
        self.result += " * "


class DivideOperationBuilder(AbstractOperationBuilder):
    def __init__(self, first_number, second_number):
        AbstractOperationBuilder.__init__(self, first_number, second_number)

    def operate(self, first_number, second_number):
        return first_number / second_number

    def build_operator(self):
        self.result += " / "


if __name__ == "__main__":
    first_number = 100
    second_number = 20
    operation_builders = [
        AddOperationBuilder(first_number, second_number),
        SubtractOperationBuilder(first_number, second_number),
        MultiplyOperationBuilder(first_number, second_number),
        DivideOperationBuilder(first_number, second_number),
    ]

    for operation_builder in operation_builders:
        operation_director = Director(operation_builder)
        operation_director.construct()
