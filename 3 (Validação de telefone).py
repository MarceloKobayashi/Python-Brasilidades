import re


class TelefonesBR:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número inválido!")

    def __str__(self):
        return self.formata_telefone()                  # printa o número já formatado

    def valida_telefone(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, telefone)
        if resposta:                                        # se algum número da lista estiver dentro do padrão
            return True
        else:
            return False

    def formata_telefone(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.numero)               # procura o primeiro número que encaixa no padrão
        numero_formatado = "+{}({}){}-{}".format(               # formata ele de acordo com os grupos
            resposta.group(1),                                  # primeiro o país com o + na frente
            resposta.group(2),                                  # segundo o DDD entre parênteses
            resposta.group(3),                                  # a primeira parte do número
            resposta.group(4)                                   # a segunda parte do número depois do hífen
        )
        return numero_formatado


ska = "61999884748"
telefone_objeto = TelefonesBR(ska)
print(telefone_objeto)
