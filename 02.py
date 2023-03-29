# número a ser testado
NUMBER = 10

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
            print(f'O número {value} pertence a sequencia de Fibonacci.')
        else:
            print(f'O número {value} não pertence a sequencia de Fibonacci.')

app = fibonacci()
app.run(NUMBER)