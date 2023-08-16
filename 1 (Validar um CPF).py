from validate_docbr import CPF


class Cpf:
    def __init__(self, documento):
        documento = str(documento)              # transforma o cpf em string para ser lido
        if self.validacao_cpf(documento):       # verifica se o cpf é válido
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def __str__(self):                          # faz com que o print do documento já saia formatado
        return self.formatacao_cpf()

    def validacao_cpf(self, cpf):         # verifica se o cpf tem 11 dígitos
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos inválida!")

    def formatacao_cpf(self):                   # formata o cpf com os pontos e o hífen
        mascara = CPF()
        return mascara.mask(self.cpf)           # faz a mesma função do .format(self.cpf[:3]...


cpf = "07228257146"
objeto_cpf = Cpf(cpf)

print(objeto_cpf)
