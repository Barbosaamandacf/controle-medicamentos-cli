imimport sys
import os

pasta_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(pasta_raiz)

from controle_medicamentos import Medicamento

def pesquisar_medicamento(banco_de_dados, termo_busca):
    resultados = []
    termo_busca = termo_busca.lower()

    for med in banco_de_dados:
        dados_dicionario = med.to_dict()
        
        if any(termo_busca in str(valor).lower() for valor in dados_dicionario.values()):
            resultados.append(med)

    return resultados

def iniciar_programa():
    med1 = Medicamento(1, "Dipirona", 500.0, "08:00", "Todos os dias", 10, "1 comprimido")
    med2 = Medicamento(2, "Amoxicilina", 875.0, "08:00 e 20:00", "Segunda a Sexta", 7, "1 cápsula")
    med3 = Medicamento(3, "Ibuprofeno", 400.0, "12:00", "Dias alternados", 15, "1 comprimido")
    med4 = Medicamento(4, "Vitamina C", 1000.0, "09:00", "Todos os dias", 30, "1 comprimido efervescente")

    meus_medicamentos = [med1, med2, med3, med4]

    print("-" * 45)
    print("SISTEMA DE BUSCA DE MEDICAMENTOS")
    print("-" * 45)
    
    while True:
        busca = input("\nDigite o medicamento, dosagem ou horário para pesquisar (ou 'sair'): ")

        if busca.lower() == 'sair':
            print("Encerrando o programa...")
            break

        resultados_encontrados = pesquisar_medicamento(meus_medicamentos, busca)

        if resultados_encontrados:
            print(f"\n✅ Encontramos {len(resultados_encontrados)} resultado(s):")
            for res in resultados_encontrados:
                print(f" - {res.get_nome()} | Dosagem: {res.get_dosagem_mg()}mg | Horário: {res.get_horario()} | Duração: {res.get_duracao_dias()} dias")
        else:
            print("\n❌ Nenhum medicamento encontrado com esse termo.")

if __name__ == "__main__":
    iniciar_programa()