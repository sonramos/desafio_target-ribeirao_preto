# 1) Observe o trecho de código abaixo:

# int INDICE = 13, SOMA = 0, K = 0;

# enquanto K < INDICE faça

# {

# K = K + 1;

# SOMA = SOMA + K;

# }

# imprimir(SOMA);


class app:
    INDICE = 13
    def __init__(self) -> None:
        self.soma = 0
        self.k = 0    

    def run(self) -> None:
        while self.k < self.INDICE:
            self.k += 1
            self.soma += self.k
        print(self.soma)

new_app = app()
new_app.run()