import logging

class Repr:
    def __repr__(self):
        return f"{type(self).__name__}({self.x!r}, {self.y!r})"


class LoggerMixin:

    def log(self, y, x):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler("app.log")
        logger.addHandler(file_handler)

        logger.info(f"{type(self).__name__}:{y} = {x}")


class LogMixin:
    def log1(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(levelname)s: %(message)s",
            filename="app_log.log"
        )

class PrintInfoMixin:
    def print_info(self):
        return f"{type(self).__name__}: count:{self.count}, size print:{self.size}"


class Print:

    def __init__(self, name, size, count):
        self.name = name
        self.size = size
        self.count = count


class PrintA4(Print, PrintInfoMixin):
    pass


a4 = PrintA4("sql_tut", "A4", "23")

print(a4.print_info())


# --------------------

class MathOperationsMixin(LoggerMixin):
    def plus(self):
        x = self.x + self.y
        self.log("plus" ,x)
        return x

    def multiplication(self):
        x = self.x * self.y
        self.log("multiplication", x)
        return x

    def divison(self):
        x = self.x / self.y
        self.log("divison", x)
        return x

    def subtraction(self):
        if self.x >= self.y:
            x = self.x - self.y
            self.log("subtraction", x)
            return x
        else:
            x = self.y - self.x
            self.log("subtraction", x)
            return x


class Mt(MathOperationsMixin, LogMixin):
    
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.log1()

    # def __repr__(self):
    #     return f""


mt = Mt("2", "4")

print(mt.plus())
print(mt.multiplication())
print(mt.divison())
print(mt.subtraction())