from database import listar_medicamentos

lista = listar_medicamentos()

for med in lista:
    print(med.get_nome())