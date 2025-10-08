import os
import importlib.util
import asyncio

# Caminho fixo do token
token_path = "code/bot/data/token.txt"

# Lê o token
with open(token_path, "r") as f:
    DISCORD_BOT = f.read().strip()

# Importa e executa todos os .py na pasta code/bot (exceto initializer.py)
for filename in os.listdir("code/bot"):
    if filename.endswith(".py") and filename != "initializer.py":
        filepath = os.path.join("code/bot", filename)
        spec = importlib.util.spec_from_file_location(filename[:-3], filepath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

# Inicializa o bot principal
try:
    from main import client  # main.py precisa estar em code/bot
    client.run(DISCORD_BOT)
except ImportError:
    print("Nenhum client encontrado em main.py")
    exit(1)