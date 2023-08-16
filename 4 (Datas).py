from datetime import datetime, timedelta


class DataBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()        # define uma variável que pega a data

    def __str__(self):
        return self.formata_data()                      # retorna o print já sendo a data formatada

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março", "abril", "maio", "junho",
            "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month - 1      # pega o mês de hoje e subtrai 1, pois a lista começa do 0
        return meses_do_ano[mes_cadastro]               # retorna o elemento da lista meses_do_ano do índice do mês

    def dia_semana(self):
        dias_da_semana = [
            "segunda", "terça", "quarta", "quinta", "sexta",
            "sábado", "domingo"
        ]
        dia_semana = self.momento_cadastro.weekday()    # pega o índice do dia de hoje, sendo 0 segunda
        return dias_da_semana[dia_semana]               # retorna o dia de hoje de acordo com a lista dias_da_semana

    def formata_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro  # timedelta: soma um período
        return tempo_cadastro           # calcula a data de hoje menos a data do cadastro              em uma data


cadastro = DataBr()
print(cadastro.tempo_cadastro())
