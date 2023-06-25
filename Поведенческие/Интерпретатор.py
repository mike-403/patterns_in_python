"""
Позволяет интерпретировать язык и выполнять определенные действия на основе входных данных
"""


class Context:
    def __init__(self, input_text):
        self.input_text = input_text
        self.output = 0


class Expression:
    def interpret(self, context):
        pass


class AddExpression(Expression):
    def __init__(self, expression_left, expression_right):
        self.expression_left = expression_left
        self.expression_right = expression_right

    def interpret(self, context):
        self.expression_left.interpret(context)
        self.expression_right.interpret(context)
        context.output = self.expression_left.result + self.expression_right.result


class NumberExpression(Expression):
    def __init__(self, number):
        self.number = number

    def interpret(self, context):
        context.output = self.number


class SubtractExpression(Expression):
    def __init__(self, expression_left, expression_right):
        self.expression_left = expression_left
        self.expression_right = expression_right

    def interpret(self, context):
        self.expression_left.interpret(context)
        self.expression_right.interpret(context)
        context.output = self.expression_left.result - self.expression_right.result


# Пример использования:
context = Context("1 + 2 - 3")
expression = SubtractExpression(AddExpression(NumberExpression(1), NumberExpression(2)), NumberExpression(3))
expression.interpret(context)
print(context.output) # Выводит: 0


"""
    В этом примере мы создаем классы Context, Expression, AddExpression, SubtractExpression и NumberExpression.  
Context представляет контекст, в котором выполняется интерпретация выражения. Expression - это абстрактный класс для 
выражений, которые будут интерпретироваться. AddExpression, SubtractExpression и NumberExpression - это конкретные 
выражения, которые будут интерпретироваться. 

    Мы создаем экземпляр Context, который содержит строку с выражением. Затем мы создаем экземпляр SubtractExpression, 
который состоит из экземпляра AddExpression сложения чисел 1 и 2, и экземпляра NumberExpression числа 3. Затем мы 
вызываем метод interpret нашего выражения, передавая ему контекст, и выводим результат. В данном случае context.output 
будет равен 0, так как результат выражения 1 + 2 - 3 равен 0.
"""