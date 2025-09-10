from math import radians, sin, cos, tan

angulo = int(input("Digite um Ângulo (30°, 45° ou 60°): "))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f"\nO ângulo de {angulo}° tem: ")
print(f"SENO = {seno:.2f}")
print(f"COSSENO = {cosseno:.2f}")
print(f"TANGENTE = {tangente:.2f}")
