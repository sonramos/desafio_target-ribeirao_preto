# 5) Escreva um programa que inverta os caracteres de um string.



# IMPORTANTE:

# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

# b) Evite usar funções prontas, como, por exemplo, reverse;

class inversor:
    def __init__(self, phrase: str) -> None:
        self.inverted_str = ''
        self.normal_str = phrase  
        if type(self.normal_str) != str:
            self.normal_str = str(self.normal_str)

    def string_inverter(self) -> None:
        for i in range(len(self.normal_str)):
            self.inverted_str += self.normal_str[-1-i]

    def run(self) -> None:
        self.string_inverter()
        print(self.inverted_str)

string_to_be_inverted = input('Insira a string a ser invertida: ')
app = inversor(string_to_be_inverted)
app.run()