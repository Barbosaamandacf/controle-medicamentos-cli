import os
import psycopg2
from dotenv import load_dotenv
from controle_medicamentos import Medicamento

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


def conectar():
    return psycopg2.connect(DATABASE_URL)


def inserir_medicamento(nome, dosagem_mg, horario, 
                        dias, duracao_dias, posologia):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO medicamentos
        (nome, dosagem_mg, horario, dias, duracao_dias, posologia)
        VALUES (%s, %s, %s, %s, %s, %s)
    """,
        (nome, dosagem_mg, horario, dias, duracao_dias, posologia),
    )

    conn.commit()
    cursor.close()
    conn.close()


def listar_medicamentos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id,
               nome,
               dosagem_mg,
               horario,
               dias,
               duracao_dias,
               posologia
        FROM medicamentos
    """)

    dados = cursor.fetchall()

    lista = []

    for item in dados:
        med = Medicamento(
            item[0],  # id
            item[1],  # nome
            item[2],  # dosagem
            item[3],  # horario
            item[4],  # dias
            item[5],  # duracao
            item[6],  # posologia
        )
        lista.append(med)

    cursor.close()
    conn.close()

    return lista


def atualizar_medicamento(id, nome, dosagem_mg, horario, dias, duracao_dias, posologia):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE medicamentos
        SET nome = %s,
            dosagem_mg = %s,
            horario = %s,
            dias = %s,
            duracao_dias = %s,
            posologia = %s
        WHERE id = %s
    """,
        (nome, dosagem_mg, horario, dias, duracao_dias, posologia, id),
    )

    conn.commit()
    cursor.close()
    conn.close()


def remover_medicamento(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM medicamentos
        WHERE id = %s
    """,
        (id,),
    )

    conn.commit()
    cursor.close()
    conn.close()
