import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import warnings

# Suprimir os FutureWarnings relacionados ao parâmetro 'observed'
warnings.filterwarnings("ignore", category=FutureWarning)

# Carregar a base de dados a partir de um arquivo CSV
df = pd.read_csv('dados_com_profissoes.csv')

# Inicializar o arquivo PDF
pdf_pages = PdfPages('relatorio_graficos.pdf')

# Criar grupos etários
bins = [18, 30, 40, 50, 60, 100]
labels = ['18-29', '30-39', '40-49', '50-59', '60+']
df['Faixa_Etaria'] = pd.cut(df['Idade'], bins=bins, labels=labels)

# Análise superficial dos dados
fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(df['Idade'], bins=20, edgecolor='k', alpha=0.7)
ax.set_title('Distribuição de Idade')
ax.set_xlabel('Idade')
ax.set_ylabel('Frequência')
ax.annotate("Este gráfico mostra a distribuição da idade dos participantes da pesquisa.", 
              xy=(0.5, -0.15), xycoords='axes fraction', ha='center', fontsize=10)
pdf_pages.savefig(fig, bbox_inches='tight')
plt.close()

# Análise moderada com alguns insights
fig, ax = plt.subplots(figsize=(8, 6))
average_salary_by_education = df.groupby('Nivel_Educacao')['Salario'].mean().sort_values(ascending=False)
ax.bar(average_salary_by_education.index, average_salary_by_education, color='lightgreen')
ax.set_title('Média Salarial por Nível de Educação')
ax.set_xlabel('Nível de Educação')
ax.set_ylabel('Média Salarial')
ax.tick_params(axis='x', rotation=0)
ax.annotate("Este gráfico mostra a média salarial por nível de educação dos participantes da pesquisa.", 
              xy=(0.5, -0.30), xycoords='axes fraction', ha='center', fontsize=10)
pdf_pages.savefig(fig, bbox_inches='tight')
plt.close()

# Calcular a correlação entre Experiência e Salário
correlation = df['Experiencia_Anos'].corr(df['Salario'])

# Criar um gráfico de dispersão para a correlação entre Experiência e Salário
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(df['Experiencia_Anos'], df['Salario'], alpha=0.5)
ax.set_title('Correlação entre Experiência e Salário')
ax.set_xlabel('Experiência (Anos)')
ax.set_ylabel('Salário')
ax.annotate(f"Correlação: {correlation:.2f}", xy=(0.7, 0.85), xycoords='axes fraction', fontsize=12)
pdf_pages.savefig(fig, bbox_inches='tight')
plt.close()

# Encontrar as profissões com maior índice de satisfação
top_satisfaction_professions = df.groupby('Profissao')['Satisfeito_Trabalho'].value_counts(normalize=True).unstack().fillna(0)
top_satisfaction_professions['Satisfacao_Relativa'] = top_satisfaction_professions['Sim'] * 100

# Calcular a média salarial por profissão
average_salary_by_profession = df.groupby('Profissao')['Salario'].mean()

# Gráfico de barras lado a lado da distribuição de satisfação no trabalho por profissão (Top 10)
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(top_satisfaction_professions.index, top_satisfaction_professions['Sim'], label='Satisfeito', width=0.4, align='center')
ax.bar(top_satisfaction_professions.index, top_satisfaction_professions['Não'], label='Não Satisfeito', width=0.4, align='edge')
ax.set_title('Distribuição de Satisfação no Trabalho por Profissão (Top 10)')
ax.set_xlabel('Profissão')
ax.set_ylabel('Contagem')
ax.legend(title='Satisfação no Trabalho')
ax.tick_params(axis='x', rotation=90)
ax.annotate("Distribuição de satisfação no trabalho por profissão (Top 10).", 
              xy=(0.5, -0.70), xycoords='axes fraction', ha='center', fontsize=10)
pdf_pages.savefig(fig, bbox_inches='tight')
plt.close()

# Gráfico de barras horizontais da média salarial por profissão (Top 10)
fig, ax = plt.subplots(figsize=(8, 6))
ax.barh(average_salary_by_profession.index, average_salary_by_profession, color='skyblue')
ax.set_title('Média Salarial por Profissão (Top 10)')
ax.set_xlabel('Média Salarial')
ax.set_ylabel('Profissão')
ax.annotate("Média salarial por profissão (Top 10).", 
              xy=(0.5, -0.15), xycoords='axes fraction', ha='center', fontsize=10)
pdf_pages.savefig(fig, bbox_inches='tight')
plt.close()

# Calcular a distribuição de satisfação no trabalho por sexo
satisfaction_by_gender = df.groupby(['Sexo', 'Satisfeito_Trabalho'])['Satisfeito_Trabalho'].count().unstack().fillna(0)

# Gráfico de barras empilhadas da distribuição de satisfação no trabalho por sexo
fig, ax = plt.subplots(figsize=(8, 6))
width = 0.4  # Largura das barras
x = range(len(satisfaction_by_gender.index))

ax.bar(x, satisfaction_by_gender['Sim'], width=width, label='Satisfeito', align='center')
ax.bar(x, satisfaction_by_gender['Não'], width=width, label='Não Satisfeito', align='edge')
ax.set_title('Distribuição de Satisfação no Trabalho por Sexo')
ax.set_xlabel('Sexo')
ax.set_ylabel('Contagem')
ax.set_xticks(x)
ax.set_xticklabels(satisfaction_by_gender.index, rotation=0)
ax.legend(title='Satisfação no Trabalho')
ax.annotate("Distribuição de satisfação no trabalho por sexo.", 
              xy=(0.5, -0.2), xycoords='axes fraction', ha='center', fontsize=10)
pdf_pages.savefig(fig, bbox_inches='tight')
plt.close()

# Converter 'Sim' e 'Não' para valores numéricos (0 e 1)
df['Satisfeito_Num'] = df['Satisfeito_Trabalho'].map({'Não': 0, 'Sim': 1})

# Calcular a média de satisfação das profissões entre os sexos
satisfaction_by_profession_gender = df.groupby(['Profissao', 'Sexo'])['Satisfeito_Num'].mean().unstack()

# Gráfico de barras empilhadas da média de satisfação das profissões entre os sexos
fig, ax = plt.subplots(figsize=(10, 6))
colors = ['lightblue', 'lightpink']  # Cores personalizadas para 'Homem' e 'Mulher'
satisfaction_by_profession_gender.plot(kind='bar', ax=ax, color=colors)
ax.set_title('Média de Satisfação das Profissões entre os Sexos')
ax.set_xlabel('Profissão')
ax.set_ylabel('Média de Satisfação')
ax.legend(title='Sexo')
ax.tick_params(axis='x', rotation=90)
ax.annotate("Média de satisfação das profissões entre os sexos.", 
              xy=(0.5, -0.70), xycoords='axes fraction', ha='center', fontsize=10)
pdf_pages.savefig(fig, bbox_inches='tight')
plt.close()

# Análise de satisfação no trabalho por faixa etária
satisfaction_by_age = df.groupby('Faixa_Etaria')['Satisfeito_Trabalho'].value_counts(normalize=True).unstack().fillna(0)

# Gráfico de barras empilhadas da distribuição de satisfação no trabalho por faixa etária
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(satisfaction_by_age.index, satisfaction_by_age['Sim'], label='Satisfeito', width=0.4, align='center')
ax.bar(satisfaction_by_age.index, satisfaction_by_age['Não'], label='Não Satisfeito', width=0.4, align='edge')
ax.set_title('Distribuição de Satisfação no Trabalho por Faixa Etária')
ax.set_xlabel('Faixa Etária')
ax.set_ylabel('Contagem')
ax.legend(title='Satisfação no Trabalho')
ax.tick_params(axis='x', rotation=0)
ax.annotate("Distribuição de satisfação no trabalho por faixa etária.", 
              xy=(0.5, -0.15), xycoords='axes fraction', ha='center', fontsize=10)
pdf_pages.savefig(fig, bbox_inches='tight')
plt.close()

# Análise de média salarial por faixa etária
average_salary_by_age = df.groupby('Faixa_Etaria')['Salario'].mean()

# Gráfico de barras da média salarial por faixa etária
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(average_salary_by_age.index, average_salary_by_age, color='skyblue')
ax.set_title('Média Salarial por Faixa Etária')
ax.set_xlabel('Faixa Etária')
ax.set_ylabel('Média Salarial')
ax.annotate("Média salarial por faixa etária.", 
              xy=(0.5, -0.15), xycoords='axes fraction', ha='center', fontsize=10)
pdf_pages.savefig(fig, bbox_inches='tight')
plt.close()

# Fechar o arquivo PDF
pdf_pages.close()
