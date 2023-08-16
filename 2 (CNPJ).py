from validate_docbr import CNPJ
from validate_docbr import CPF


class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)
        if tipo_documento == "cpf":
            if self.validacao_cpf(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido!")
        elif tipo_documento == "cnpj":                  # verifica se é cnpj e implementa a variável self.cnpj
            if self.validacao_cnpj(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ inválido!")
        else:
            raise ValueError("Documento inválido!")

    def __str__(self):
        if self.tipo_documento == "cpf":
            return self.formatacao_cpf()
        elif self.tipo_documento == "cnpj":             # verifica se é cnpj e printa o cnpj já formatado
            return self.formatacao_cnpj()

    def validacao_cpf(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos inválida!")

    def formatacao_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def validacao_cnpj(self, cnpj):
        if len(cnpj) == 14:                                 # verifica se o número de dígitos é válido
            validador_cnpj = CNPJ()
            return validador_cnpj.validate(cnpj)            # verifica se o cnpj existe no banco de dados
        else:
            raise ValueError("Quantidade de dígitos inválida!")

    def formatacao_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)                      # formata o cnpj para o padrão


exmplo_cnpj = "09055134000184"
documentos = CpfCnpj(exmplo_cnpj, "cnpj")
print(documentos)
