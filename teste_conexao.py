from database import conectar

try:
    conn = conectar()
    print("Conexão realizada com sucesso!")
    conn.close()

except Exception as erro:
    print("Erro:", erro)