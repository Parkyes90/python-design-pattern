from abc import ABCMeta, abstractmethod


class AbstractOperationFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_operation_product(self):
        pass

    @abstractmethod
    def create_number_operand_product(self, value):
        pass


class AbstractOperationProduct(metaclass=ABCMeta):
    def __init__(self):
        self.first_number_operand_product = None
        self.second_number_operand_product = None

    def set_first_number_operand_product(self, first_number_operand_product):
        self.first_number_operand_product = first_number_operand_product

    def set_second_number_operand_product(self, second_number_operand_product):
        self.second_number_operand_product = second_number_operand_product

    def add(self):
        first_number = self.get_first_number()
        second_number = self.get_second_number()
        return first_number + second_number

    def divide(self):
        first_number = self.get_first_number()
        second_number = self.get_second_number()

        return first_number / second_number

    def multiply(self):
        first_number = self.get_first_number()
        second_number = self.get_second_number()

        return first_number * second_number

    def subtract(self):
        first_number = self.get_first_number()
        second_number = self.get_second_number()

        return first_number - second_number

    def get_first_number(self):
        return self.first_number_operand_product.get_number()

    def get_second_number(self):
        return self.second_number_operand_product.get_number()

    @abstractmethod
    def print_result(self):
        pass


class AbstractNumberOperandProduct(metaclass=ABCMeta):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def get_number(self):
        pass

    def get_value(self):
        return self.value


class DoubleOperationProduct(AbstractOperationProduct):
    def print_result(self):
        first_number = self.get_first_number()
        second_number = self.get_second_number()
        print(f"{first_number} + {second_number} = {self.add()}")
        print(f"{first_number} - {second_number} = {self.subtract()}")
        print(f"{first_number} * {second_number} = {self.multiply()}")
        print(f"{first_number} / {second_number} = {self.divide()}")


class DoubleNumberOperationProduct(AbstractNumberOperandProduct):
    def __init__(self, value):
        AbstractNumberOperandProduct.__init__(self, value)

    def get_number(self):
        value = self.get_value()
        return float(value)


class IntegerOperationProduct(AbstractOperationProduct):
    def print_result(self):
        first_number = self.get_first_number()
        second_number = self.get_second_number()
        print(f"{first_number} + {second_number} = {self.add()}")
        print(f"{first_number} - {second_number} = {self.subtract()}")
        print(f"{first_number} * {second_number} = {self.multiply()}")
        print(f"{first_number} / {second_number} = {self.divide()}")


class IntegerNumberOperandProduct(AbstractNumberOperandProduct):
    def __init__(self, value):
        AbstractNumberOperandProduct.__init__(self, value)

    def get_number(self):
        value = self.get_value()
        return int(float(value))


class IntegerOperationFactory(AbstractOperationFactory):
    def create_number_operand_product(self, value):
        print(value)
        return IntegerNumberOperandProduct(value)

    def create_operation_product(self):
        return IntegerOperationProduct()


class DoubleOperationFactory(AbstractOperationFactory):
    def create_operation_product(self):
        return DoubleOperationProduct()

    def create_number_operand_product(self, value):
        return DoubleNumberOperationProduct(value)


if __name__ == "__main__":
    first_number = "10.3"
    second_number = "20.2"

    operation_factory = IntegerOperationFactory()

    operation_product = operation_factory.create_operation_product()
    operation_product.set_first_number_operand_product(
        operation_factory.create_number_operand_product(first_number)
    )
    operation_product.set_second_number_operand_product(
        operation_factory.create_number_operand_product(second_number)
    )

    operation_product.print_result()

    operation_factory = DoubleOperationFactory()
    operation_product = operation_factory.create_operation_product()
    operation_product.set_first_number_operand_product(
        operation_factory.create_number_operand_product(first_number)
    )
    operation_product.set_second_number_operand_product(
        operation_factory.create_number_operand_product(second_number)
    )
    operation_product.print_result()
