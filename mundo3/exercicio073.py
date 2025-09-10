#Tabela 17/08/2025
times = ("Flamengo", "Cruzeiro", "Palmeiras", "Bahia", "Botafogo", "São Paulo", "Mirassol", "Fluminense", "RB Bragantino", "Ceara",
         "Atlético-MG", "Internacional", "Corinthians", "Santos", "Gremio", "Vitoria", "Vasco DA Gama", "Juventude", "Fortaleza EC", "Sport Recife")

print("--- Times do Brasileirão ---\n")
print(f"{times}")

print("\n--- 5 Primeiros Times ---\n")
print(f"{times[:5]}")

print(f"\n--- 4 Últimos Times ---\n")
print(f"{times[-4:]}")

print("\n--- Times em Ordem Alfabética ---\n")
print(f"{sorted(times)}")

print("\n--- Posição \'Fluminense\' ---\n")
print(f"{times.index('Fluminense') + 1}ª Posição")
