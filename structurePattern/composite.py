from abc import ABCMeta, abstractmethod


class AbstractExpression(metaclass=ABCMeta):
    @abstractmethod
    def operate(self):
        pass


class AbstractOperationExpression(AbstractExpression):
    def __init__(self):
        self.operand_list = []

    def add_operand_expression(self, operand_expression):
        self.operand_list.append(operand_expression)

    def operate(self):
        pass


class NumberExpression(AbstractExpression):
    def __init__(self, value):
        self.value = value

    def operate(self):
        return self.value


class AddOperationExpression(AbstractOperationExpression):
    def __init__(self):
        AbstractOperationExpression.__init__(self)

    def operate(self):
        first_operand_expression = self.operand_list[0]
        second_operand_expression = self.operand_list[1]

        first_result = first_operand_expression.operate()
        second_result = second_operand_expression.operate()

        return first_result + second_result


class SubtractOperationExpression(AbstractOperationExpression):
    def __init__(self):
        AbstractOperationExpression.__init__(self)

    def operate(self):
        first_operand_expression = self.operand_list[0]
        second_operand_expression = self.operand_list[1]

        first_result = first_operand_expression.operate()
        second_result = second_operand_expression.operate()

        return first_result - second_result


class MultiplyOperationExpression(AbstractOperationExpression):
    def __init__(self):
        AbstractOperationExpression.__init__(self)

    def operate(self):
        first_operand_expression = self.operand_list[0]
        second_operand_expression = self.operand_list[1]

        first_result = first_operand_expression.operate()
        second_result = second_operand_expression.operate()

        return first_result * second_result


class DivideOperationExpression(AbstractOperationExpression):
    def __init__(self):
        AbstractOperationExpression.__init__(self)

    def operate(self):
        first_operand_expression = self.operand_list[0]
        second_operand_expression = self.operand_list[1]

        first_result = first_operand_expression.operate()
        second_result = second_operand_expression.operate()

        return first_result / second_result


class Calculator:
    def __init__(self):
        self.expression = None

    def calculate(self):
        return self.expression.operate()

    def set_expression(self, expression):
        self.expression = expression


if __name__ == "__main__":
    calculator = Calculator()

    first_number = 100
    second_number = 20

    first_number_equation = NumberExpression(first_number)
    calculator.set_expression(first_number_equation)
    print(f"firstNumber={calculator.calculate()}")

    second_number_equation = NumberExpression(second_number)

    calculator.set_expression(second_number_equation)
    print(f"second_number={calculator.calculate()}")

    add_operation_expression = AddOperationExpression()
    add_operation_expression.add_operand_expression(first_number_equation)
    add_operation_expression.add_operand_expression(second_number_equation)
    calculator.set_expression(add_operation_expression)
    print(f"{first_number}+{second_number}={calculator.calculate()}")

    subtract_operation_expression = SubtractOperationExpression()
    subtract_operation_expression.add_operand_expression(first_number_equation)
    subtract_operation_expression.add_operand_expression(
        second_number_equation
    )
    calculator.set_expression(subtract_operation_expression)
    print(f"{first_number}-{second_number}={calculator.calculate()}")

    multiply_operation_expression = MultiplyOperationExpression()
    multiply_operation_expression.add_operand_expression(first_number_equation)
    multiply_operation_expression.add_operand_expression(
        second_number_equation
    )
    calculator.set_expression(multiply_operation_expression)
    print(f"{first_number}*{second_number}={calculator.calculate()}")

    divide_operation_expression = DivideOperationExpression()
    divide_operation_expression.add_operand_expression(first_number_equation)
    divide_operation_expression.add_operand_expression(second_number_equation)
    calculator.set_expression(divide_operation_expression)
    print(f"{first_number}/{second_number}={calculator.calculate()}")
