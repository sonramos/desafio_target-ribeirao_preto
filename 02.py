# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.



# IMPORTANTE:

# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;


# número a ser testado
NUMBER = 55

class fibonacci:
    SIZE = 30
    def __init__(self) -> None:
        self.fibonacci_sequence = []

    def fill_fibonacci(self) -> None:
        n1 = 0
        n2 = 1
        if len(self.fibonacci_sequence) < 2:
            self.fibonacci_sequence.append(n1)
            self.fibonacci_sequence.append(n2)
        current_size = len(self.fibonacci_sequence)
        while current_size < self.SIZE:
            n3 = n2 + n1
            self.fibonacci_sequence.append(n3)
            n1 = n2
            n2 = n3
            current_size += 1
        print(self.fibonacci_sequence)

    def run(self, value) -> None:
        self.fill_fibonacci()
        if value in self.fibonacci_sequence:
            print(f'O número {value} pertence a sequência de Fibonacci.')
        else:
            print(f'O número {value} não pertence a sequência de Fibonacci.')

app = fibonacci()
app.run(NUMBER)