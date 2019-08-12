class TextStyleFlyWeight:
    def __init__(self, font_info, color):
        self.font_info = font_info
        self.color = color

    def get_font(self):
        return self.font_info

    def get_color(self):
        return self.color

    def to_string(self):
        return f"({self.font_info.to_string()},{self.color})"


class TextStyleFlyweightFactory:
    __instance = None

    pool = {}

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def __get_instance(cls):
        return cls.__instance

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = cls(*args, **kwargs)

        return cls.__instance

    @classmethod
    def get_text_style_flyweight(cls, name):
        text_style = cls.pool.get(name)
        return text_style

    @classmethod
    def put_text_style_flyweight(cls, name, text_style):
        cls.pool[name] = text_style


class FontInfo:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def to_string(self):
        return f"({self.name}, {self.size})"


class FlyweightConstants:
    NUMBER_STYLE_NAME = "number"
    ANSWER_STYLE_NAME = "answer"

    COLUMN_WIDTH = 50
    ROW_HEIGHT = 50
    OPERATORS = ("+", "-", "*", "/")
    EQUAL_CHAR = "="

    DEFAULT_NUMBER_FONT_INFO = FontInfo("Times", 18)
    DEFAULT_ANSWER_FONT_INFO = FontInfo("Times", 26)


class PrintAnswer:
    def __init__(self):
        self.text_style_flyweight_factory = (
            TextStyleFlyweightFactory().get_instance()
        )
        self.first_number = 0
        self.second_number = 0

    def print_result(self):
        answers = [0, 0, 0, 0]

        answers[0] = self.first_number + self.second_number
        answers[1] = self.first_number - self.second_number
        answers[2] = self.first_number * self.second_number
        answers[3] = self.first_number / self.second_number
        i = 0

        for answer in answers:
            operator = FlyweightConstants.OPERATORS[i]
            text_array = ["", "", "", "", ""]
            text_array[0] = (
                ""
                + str(self.first_number)
                + self.__get_text_style(
                    FlyweightConstants.NUMBER_STYLE_NAME
                ).to_string()
            )
            text_array[1] = operator
            text_array[2] = (
                ""
                + str(self.second_number)
                + self.__get_text_style(
                    FlyweightConstants.NUMBER_STYLE_NAME
                ).to_string()
            )
            text_array[3] = FlyweightConstants.EQUAL_CHAR
            text_array[4] = (
                ""
                + str(answers)
                + self.__get_text_style(
                    FlyweightConstants.ANSWER_STYLE_NAME
                ).to_string()
            )

            print("".join(text_array))
            i += 1

    def __get_text_style(self, name):
        return self.text_style_flyweight_factory.get_text_style_flyweight(name)

    def set_first_number(self, first_number):
        self.first_number = first_number

    def set_second_number(self, second_number):
        self.second_number = second_number


class Client:
    def set_up_text_style_flyweight_factory(self):
        text_style_flyweight_factory = (
            TextStyleFlyweightFactory().get_instance()
        )

        name = FlyweightConstants.NUMBER_STYLE_NAME
        text_style = TextStyleFlyWeight(
            FlyweightConstants.DEFAULT_NUMBER_FONT_INFO, "red"
        )
        text_style_flyweight_factory.put_text_style_flyweight(name, text_style)
        name = FlyweightConstants.ANSWER_STYLE_NAME
        text_style = TextStyleFlyWeight(
            FlyweightConstants.DEFAULT_ANSWER_FONT_INFO, "black"
        )
        text_style_flyweight_factory.put_text_style_flyweight(name, text_style)

    def main(self):
        client = Client()
        client.set_up_text_style_flyweight_factory()
        print_answer = PrintAnswer()
        print_answer.set_first_number(10)
        print_answer.set_second_number(20)
        print_answer.print_result()


if __name__ == "__main__":
    client = Client()
    client.main()
