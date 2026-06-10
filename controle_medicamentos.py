import requests


class Medicamento:
    def __init__(
            self,
            id: int,
            nome: str,
            dosagem_mg: float,
            horario: str,
            dias: str,
            duracao_dias: int,
            posologia: str
    ):
        self.id = id
        self.nome = nome
        self.dosagem_mg = dosagem_mg
        self.horario = horario
        self.dias = dias
        self.duracao_dias = duracao_dias
        self.posologia = posologia

    def get_nome(self):
        return self.nome

    def get_id(self):
        return self.id

    def get_dosagem_mg(self):
        return self.dosagem_mg

    def get_horario(self):
        return self.horario

    def get_dias(self):
        return self.dias

    def get_duracao_dias(self):
        return self.duracao_dias

    def get_posologia(self):
        return self.posologia

    def set_nome(self, nome):
        if nome.strip() != "":
            self.nome = nome
        else:
            print("Nome inválido!")

    def set_dosagem_mg(self, dosagem_mg):
        if dosagem_mg > 0:
            self.dosagem_mg = dosagem_mg
        else:
            print("Dosagem inválida!")

    def set_horario(self, horario):
        if horario.strip() != "":
            self.horario = horario
        else:
            print("Horário inválido!")

    def set_dias(self, dias):
        if dias.strip() != "":
            self.dias = dias
        else:
            print("Dias inválidos!")

    def set_duracao_dias(self, duracao_dias):
        if duracao_dias > 0:
            self.duracao_dias = duracao_dias
        else:
            print("Duração inválida!")

    def set_posologia(self, posologia):
        if posologia.strip() != "":
            self.posologia = posologia
        else:
            print("Posologia inválida!")

    def to_dict(self):
        return {
            "nome": self.nome,
            "dosagem_mg": self.dosagem_mg,
            "horario": self.horario,
            "dias": self.dias,
            "duracao_dias": self.duracao_dias,
            "posologia": self.posologia
        }


def buscar_info_api():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return None

    except Exception:
        return None
