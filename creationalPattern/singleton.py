class SingleTon:
    __instance = None

    ADD_OPERATION = 1
    SUBTRACT_OPERATION = 2
    MULTIPLY_OPERATION = 3
    DIVIDE_OPERATION = 4

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def __get_instance(cls):
        return cls.__instance

    @classmethod
    def get_instance(cls, *args, **kwargs):
        print(cls.__instance)
        if not cls.__instance:
            cls.__instance = cls(*args, **kwargs)
            print(cls.__instance)
        return cls.__instance

    def operate(self, operator_type, first, second):
        answer = 0
        operator = None

        if operator_type == SingleTon.ADD_OPERATION:
            answer = first + second
            operator = "+"
        elif operator_type == SingleTon.SUBTRACT_OPERATION:
            answer = first - second
            operator = "-"
        elif operator_type == SingleTon.MULTIPLY_OPERATION:
            answer = first * second
            operator = "*"
        elif operator_type == SingleTon.DIVIDE_OPERATION:
            answer = first / second
            operator = "/"
        result = f'{first}{operator}{second}={answer}'
        self.print_result(result)

    def print_result(self, result):
        print(result)


class Client:
    def main(self):
        singleton = SingleTon.get_instance()
        first = 200
        second = 20

        singleton.operate(SingleTon.ADD_OPERATION, first, second)
        second_singleton = SingleTon.get_instance()
        third_singleton = SingleTon.get_instance()
        print(singleton, second_singleton, third_singleton)


if __name__ == '__main__':
    client = Client()
    client.main()
