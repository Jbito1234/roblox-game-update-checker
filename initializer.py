import os
import importlib.util
import asyncio

# Lê o token do arquivo
with open("token.txt", "r") as f:
    DISCORD_BOT = f.read().strip()

# Pasta atual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Função para importar e executar todos os .py
for filename in os.listdir(current_dir):
    if filename.endswith(".py") and filename != "initializer.py":
        filepath = os.path.join(current_dir, filename)
        spec = importlib.util.spec_from_file_location(filename[:-3], filepath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

# Procura um client do Discord no módulo main.py e roda
try:
    from main import client
    client.run(DISCORD_BOT)
except ImportError:
    print("Nenhum client encontrado em main.py. Certifique-se de ter um bot inicializado.")