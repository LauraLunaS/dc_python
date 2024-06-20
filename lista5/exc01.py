lines = []
with open('lista5/discip.txt') as f:
    lines = f.readlines()


lines.pop(6)
lines.pop(6) 


lines[1] = "MA025 Topicos Avancados em ES II          5"
lines[6] = "MA143 Banco de Dados I                    5"


disciplinas = {}


def parse_disciplina(line):
    parts = line.split()
    codigo = parts[0]
    carga = parts[-1]
    nome = ' '.join(parts[1:-1])
    return codigo, nome, carga


for line in lines:
    codigo, nome, carga = parse_disciplina(line)
    disciplinas[codigo] = {
        'nome': nome,
        'carga': carga
    }


for codigo, info in disciplinas.items():
    print(f'Código: {codigo}, Nome: {info["nome"]}, Carga Horária: {info["carga"]}')
