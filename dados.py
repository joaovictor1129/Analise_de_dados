import pandas as pd
import random

# Lista de profissões fictícias
profissoes = ['Engenheiro', 'Médico', 'Professor', 'Designer', 'Analista', 'Advogado', 'Arquiteto', 'Enfermeiro', 'Técnico', 'Gerente']

# Profissões atualmente em alta demanda (lista fictícia)
profissoes_em_alta_demanda = [
    'Desenvolvedor de Software',
    'Engenheiro de Dados',
    'Cientista de Dados',
    'Enfermeiro(a)',
    'Analista de Segurança da Informação',
    'Engenheiro DevOps',
    'Médico Cirurgião',
    'Gerente de Projetos de TI',
    'Especialista em Inteligência Artificial',
    'Designer de Experiência do Usuário',
    # Adicione outras profissões em alta demanda aqui
]

# Adicionar profissões em alta demanda à lista de profissões
profissoes.extend(profissoes_em_alta_demanda)

# Mapear profissões para salários fictícios condizentes com a realidade
salarios_por_profissao = {
    'Engenheiro': 8000,
    'Médico': 12000,
    'Professor': 4000,
    'Designer': 4500,
    'Analista': 5500,
    'Advogado': 7000,
    'Arquiteto': 7500,
    'Enfermeiro': 6000,
    'Técnico': 3500,
    'Gerente': 9000,
    'Desenvolvedor de Software': 7000,
    'Engenheiro de Dados': 8500,
    'Cientista de Dados': 9000,
    'Enfermeiro(a)': 6000,
    'Analista de Segurança da Informação': 8000,
    'Engenheiro DevOps': 7500,
    'Médico Cirurgião': 14000,
    'Gerente de Projetos de TI': 10000,
    'Especialista em Inteligência Artificial': 9500,
    'Designer de Experiência do Usuário': 6000,
}

# Criar dados fictícios com profissões e sexo
data = {
    'Idade': [random.randint(25, 60) for _ in range(500)],
    'Salario': [salarios_por_profissao[profissao] for profissao in random.choices(profissoes, k=500)],
    'Nivel_Educacao': [random.choice(['Bacharelado', 'Mestrado', 'Doutorado', 'Pos graduado', 'Tecnologo']) for _ in range(500)],
    'Experiencia_Anos': [random.randint(0, 30) for _ in range(500)],
    'Satisfeito_Trabalho': [random.choice(['Sim', 'Não']) for _ in range(500)],
    'Profissao': [random.choice(profissoes) for _ in range(500)],
    'Sexo': [random.choice(['Masculino', 'Feminino']) for _ in range(500)]  # Adicione o sexo aqui
}

# Criar DataFrame a partir dos dados
df = pd.DataFrame(data)

# Salvar o DataFrame em um arquivo CSV
df.to_csv('dados_com_profissoes.csv', index=False)

print("Base de dados CSV 'dados_com_profissões.csv' criada com sucesso.")
