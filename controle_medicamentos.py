import json


class Medicamento:

    def __init__(
        self,
        nome: str,
        dosagem_mg: float,
        horario: str,
        dias: str,
        duracao_dias: int,
        posologia: str
    ):
        self.nome = nome
        self.dosagem_mg = dosagem_mg
        self.horario = horario
        self.dias = dias
        self.duracao_dias = duracao_dias
        self.posologia = posologia

    def get_nome(self):
        return self.nome

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


def carregar_medicamentos():
    try:
        with open("medicamentos.json", "r") as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        return []

    lista_objetos = []

    for med_dict in dados:
        novo_med = Medicamento(
            med_dict["nome"],
            med_dict["dosagem_mg"],
            med_dict["horario"],
            med_dict["dias"],
            med_dict["duracao_dias"],
            med_dict["posologia"]
        )
        lista_objetos.append(novo_med)

    return lista_objetos


def salvar_medicamentos(lista):
    lista_dict = []

    for med in lista:
        lista_dict.append(med.to_dict())

    with open("medicamentos.json", "w") as arquivo:
        json.dump(lista_dict, arquivo, indent=4)
