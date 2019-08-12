from abc import ABCMeta, abstractmethod


class NumberOperand:
    def __init__(self, value):
        self.value = value
        # self.operator_token = operator_token

    def get_number(self):
        return int(self.value)


class ExpressionParser:
    def __init__(self):
        self.operators = ("+", "-", "*", "/")
        self.operator_token = ""
        self.first_number_token = ""
        self.second_number_token = ""

    def get_operator_token(self):
        return self.operator_token

    def get_first_number_token(self):
        return self.first_number_token

    def get_second_number_token(self):
        return self.second_number_token

    def parser(self, expression):
        operator_index = -1

        for operator in self.operators:
            operator_index = expression.find(operator)
            if operator_index != -1:
                self.operator_token = operator
                break

        self.first_number_token = expression[0:operator_index]

        self.second_number_token = expression[operator_index + 1]


class AbstractOperationProduct(metaclass=ABCMeta):
    @abstractmethod
    def operate(self, first_number, second_number):
        pass


class AddOperationProduct(AbstractOperationProduct):
    def __init__(self):
        pass

    def operate(self, first_number, second_number):
        answer = first_number + second_number

        print(f"{first_number}+{second_number}={answer}")


class SubtractOperationProduct(AbstractOperationProduct):
    def __init__(self):
        pass

    def operate(self, first_number, second_number):
        answer = first_number - second_number

        print(f"{first_number}-{second_number}={answer}")


class MultiplyOperationProduct(AbstractOperationProduct):
    def __init__(self):
        pass

    def operate(self, first_number, second_number):
        answer = first_number * second_number

        print(f"{first_number}*{second_number}={answer}")


class DivideOperationProduct(AbstractOperationProduct):
    def __init__(self):
        pass

    def operate(self, first_number, second_number):
        answer = first_number / second_number

        print(f"{first_number}/{second_number}={answer}")


class OperationFactory:
    def create_operation_product(self, operator):
        if operator == "+":
            return AddOperationProduct()

        if operator == "-":
            return SubtractOperationProduct()

        if operator == "*":
            return MultiplyOperationProduct()

        if operator == "/":
            return DivideOperationProduct()


class CalculatorFacade:
    def __init__(self):
        pass

    def calculate(self, expression):
        expression_parser = ExpressionParser()
        expression_parser.parser(expression)

        operator_token = expression_parser.get_operator_token()
        first_number_token = expression_parser.get_first_number_token()
        second_number_token = expression_parser.get_second_number_token()

        first_number_operand = NumberOperand(first_number_token)
        second_number_operand = NumberOperand(second_number_token)

        first_number = first_number_operand.get_number()
        second_number = second_number_operand.get_number()

        operation_factory = OperationFactory()
        operation_product = operation_factory.create_operation_product(
            operator_token
        )
        operation_product.operate(first_number, second_number)


if __name__ == "__main__":
    calculator = CalculatorFacade()
    expressions = ("100+20", "100-20", "100*20", "100/20")
    for expression in expressions:
        calculator.calculate(expression)
