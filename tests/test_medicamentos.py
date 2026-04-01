import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controle_medicamentos import Medicamento

def test_criar_medicamento():
    med = Medicamento(
        "Dipirona", 500, "08:00", "segunda", 7, "Tomar 1 comprimido"
    )

    assert med.get_nome() == "Dipirona"
    assert med.get_dosagem_mg() == 500


def test_dosagem_invalida():
    med = Medicamento("Teste", 500, "08:00", "segunda", 7, "Teste")

    med.set_dosagem_mg(-10)

    assert med.get_dosagem_mg() == 500


def test_nome_vazio():
    med = Medicamento("Remedio", 500, "08:00", "segunda", 7, "Teste")

    med.set_nome("")

    assert med.get_nome() == "Remedio"