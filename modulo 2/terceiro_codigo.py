from datetime import datetime

# Solicitando o nome do usuário
nome = input("Por favor, digite o seu nome: ")

# Obtendo a hora atual formatada (Apenas Hora:Minuto)
hora_atual = datetime.now().strftime("%H:%M")

# Exibindo a saudação com o nome e a hora
print(f"Olá, {nome}! Seja bem-vindo(a)! Agora são exatamente {hora_atual}.")
