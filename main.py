from controle_medicamentos import (
    Medicamento,
    carregar_medicamentos,
    salvar_medicamentos,
    buscar_info_api
)


if __name__ == '__main__':

    while True:
        print("\n MENU ")
        print("1 - Cadastrar medicamento")
        print("2 - Listar medicamentos")
        print("3 - Editar medicamento")
        print("4 - Remover medicamento")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Você escolheu cadastrar medicamento")

            nome = input("Nome do medicamento: ")
            if nome.strip() == "":
                print("Nome não pode ser vazio!")
                continue

            try:
                dosagem_mg = float(input("Dosagem (mg): "))
            except ValueError:
                print("Digite um valor numérico para a dosagem!")
                continue

            horario = input("Horário (ex: 08:00): ")
            if ":" not in horario:
                print("Formato de horário inválido! Use HH:MM")
                continue

            dias = input("Dias (ex: segunda a sexta): ")

            try:
                duracao_dias = int(input("Duração (dias): "))
            except ValueError:
                print("Digite um número inteiro para duração!")
                continue

            posologia = input("Posologia: ")

            med = Medicamento(
                nome=nome,
                dosagem_mg=dosagem_mg,
                horario=horario,
                dias=dias,
                duracao_dias=duracao_dias,
                posologia=posologia
            )

            lista = carregar_medicamentos()
            lista.append(med)
            salvar_medicamentos(lista)

            print("Medicamento cadastrado com sucesso!")

        elif opcao == "2":
            print("Você escolheu listar medicamentos")

            lista = carregar_medicamentos()

            if not lista:
                print("Nenhum medicamento cadastrado ainda.")
            else:
                print("\n MEDICAMENTOS ")
                for i, med in enumerate(lista, start=1):
                    print(f"{i}. Nome: {med.get_nome()}")
                    print(f"   Dosagem: {med.get_dosagem_mg()} mg")
                    print(f"   Horário: {med.get_horario()}")
                    print(f"   Dias: {med.get_dias()}")
                    print(f"   Duração: {med.get_duracao_dias()} dias")
                    print(f"   Posologia: {med.get_posologia()}")
                    print("------------------------")

                dados_api = buscar_info_api()

                if dados_api:
                    print("\n🌐 Informação externa da API:")
                    print(dados_api["title"])
                else:
                    print("\nNão foi possível obter dados da API.")

        elif opcao == "3":
            print("Você escolheu editar medicamento")

            lista = carregar_medicamentos()

            if not lista:
                print("Nenhum medicamento cadastrado.")
            else:
                print("\n MEDICAMENTOS ")
                for i, med in enumerate(lista, start=1):
                    print(f"{i} - {med.get_nome()}")

                try:
                    indice = int(
                        input("Escolha o número do medicamento: ")
                    ) - 1
                except ValueError:
                    print("Digite um número válido!")
                    continue

                if 0 <= indice < len(lista):
                    med = lista[indice]

                    print("\nDeixe vazio para não alterar")

                    novo_nome = input(
                        f"Novo nome ({med.get_nome()}): "
                    )
                    if novo_nome:
                        med.set_nome(novo_nome)

                    try:
                        nova_dosagem = input(
                            f"Nova dosagem ({med.get_dosagem_mg()}): "
                        )
                        if nova_dosagem:
                            med.set_dosagem_mg(float(nova_dosagem))
                    except ValueError:
                        print("Dosagem inválida!")

                    novo_horario = input(
                        f"Novo horário ({med.get_horario()}): "
                    )
                    if novo_horario:
                        if ":" in novo_horario:
                            med.set_horario(novo_horario)
                        else:
                            print("Horário inválido!")

                    novos_dias = input(
                        f"Novos dias ({med.get_dias()}): "
                    )
                    if novos_dias:
                        med.set_dias(novos_dias)

                    try:
                        nova_duracao = input(
                            f"Nova duração ({med.get_duracao_dias()}): "
                        )
                        if nova_duracao:
                            med.set_duracao_dias(int(nova_duracao))
                    except ValueError:
                        print("Duração inválida!")

                    nova_posologia = input(
                        f"Nova posologia ({med.get_posologia()}): "
                    )
                    if nova_posologia:
                        med.set_posologia(nova_posologia)

                    salvar_medicamentos(lista)
                    print("Medicamento atualizado com sucesso!")

                else:
                    print("Índice inválido!")

        elif opcao == "4":
            print("Você escolheu remover medicamento")

            lista = carregar_medicamentos()

            if not lista:
                print("Nenhum medicamento para remover.")
            else:
                print("\n MEDICAMENTOS ")
                for i, med in enumerate(lista, start=1):
                    print(f"{i} - {med.get_nome()}")

                try:
                    indice = int(
                        input("Digite o número do medicamento: ")
                    ) - 1
                except ValueError:
                    print("Digite um número válido!")
                    continue

                if 0 <= indice < len(lista):
                    lista.pop(indice)
                    salvar_medicamentos(lista)
                    print("Medicamento removido com sucesso!")
                else:
                    print("Índice inválido!")

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida")
