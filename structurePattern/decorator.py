import math

from structurePattern.composite import (
    AbstractExpression,
    Calculator,
    AddOperationExpression,
    NumberExpression,
)


class AbstractDecoratorExpression(AbstractExpression):
    def __init__(self, expression):
        self.expression = expression

    def set_expression(self, expression):
        self.expression = expression

    def operate(self):
        pass


class FracDecoratorExpression(AbstractDecoratorExpression):
    def __init__(self, expression):
        AbstractDecoratorExpression.__init__(self, expression)

    def operate(self):
        return 1 / self.expression.operate()


class PowDecoratorExpression(AbstractDecoratorExpression):
    def __init__(self, expression, exponent):
        AbstractDecoratorExpression.__init__(self, expression)
        self.exponent = exponent

    def operate(self):
        return math.pow(self.expression.operate(), self.exponent)


class SqrtDecoratorExpress(AbstractDecoratorExpression):
    def __init__(self, expression):
        AbstractDecoratorExpression.__init__(self, expression)

    def operate(self):
        return math.sqrt(self.expression.operate())


if __name__ == "__main__":
    calculator = Calculator()

    first_number = 80
    second_number = 20

    first_number_equation = NumberExpression(first_number)
    second_number_equation = NumberExpression(second_number)

    addOperationEquation = AddOperationExpression()
    addOperationEquation.add_operand_expression(first_number_equation)
    addOperationEquation.add_operand_expression(second_number_equation)
    calculator.set_expression(SqrtDecoratorExpress(addOperationEquation))
    print(f"SQRT({first_number}, {second_number}) = {calculator.calculate()}")
    calculator.set_expression(FracDecoratorExpression(addOperationEquation))
    print(f"FRAC({first_number}, {second_number}) = {calculator.calculate()}")
    calculator.set_expression(PowDecoratorExpression(addOperationEquation, 2))
    print(f"POW({first_number}, {second_number}) = {calculator.calculate()}")
