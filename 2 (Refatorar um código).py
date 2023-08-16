from validate_docbr import CNPJ, CPF


class Documento:                                    # cria uma classe para escolher qual classe ele deve usar
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos inválida!")


class DocCpf:
    def __init__(self, documento):
        if self.valida_cpf(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def __str__(self):
        return self.formata_cpf(self.cpf)

    def valida_cpf(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def formata_cpf(self, documento):
        mascara = CPF()
        return mascara.mask(documento)


class DocCnpj:
    def __init__(self, documento):
        if self.valida_cnpj(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!")

    def __str__(self):
        return self.formata_cnpj(self.cnpj)

    def valida_cnpj(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def formata_cnpj(self, documento):
        mascara = CNPJ()
        return mascara.mask(documento)


exmplo_cnpj = "09055134000184"
documentos = Documento.cria_documento(exmplo_cnpj)
print(documentos)

exemplo_cpf = "07228257146"
doc = Documento.cria_documento(exemplo_cpf)
print(doc)
