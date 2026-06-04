import os
import psycopg2
from dotenv import load_dotenv
from controle_medicamentos import Medicamento

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


def conectar():
    return psycopg2.connect(DATABASE_URL)

def inserir_medicamento(
        nome,
        dosagem_mg,
        horario,
        dias,
        duracao_dias,
        posologia
):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO medicamentos
        (nome, dosagem_mg, horario, dias, duracao_dias, posologia)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        nome,
        dosagem_mg,
        horario,
        dias,
        duracao_dias,
        posologia
    ))

    conn.commit()
    cursor.close()
    conn.close()

def listar_medicamentos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT nome,
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
            item[0],
            item[1],
            item[2],
            item[3],
            item[4],
            item[5]
        )
        lista.append(med)

    cursor.close()
    conn.close()

    return lista