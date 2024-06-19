lines = []
with open('lista5/discip.txt') as f:
    lines = f.readlines()

count = 0
disciplina = {}

for i in lines:
    count += 1
    print(f'linha {count}: {i}')

lines.pop(6)
lines.pop(7)

lines[1] = "MA025 Topicos Avancados em ES II          5"
lines[6] = "MA143 Banco de Dados I                    5"

print(lines)

# with open('discip_new.txt', 'w') as f:
#     f.write('primeiro arquivo criado')
