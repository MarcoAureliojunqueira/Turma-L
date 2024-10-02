import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import os

# Função para adicionar texto com quebra de linha
def draw_multiline_text(c, text, x, y, max_width, line_height):
    for line in text.splitlines():
        words = line.split(" ")
        current_line = ""
        for word in words:
            # Verifica se adicionar a próxima palavra excede a largura máxima
            if c.stringWidth(current_line + word, "Helvetica", 10) < max_width:
                current_line += f"{word} "
            else:
                c.drawString(x, y, current_line)
                y -= line_height
                current_line = f"{word} "  # Começa uma nova linha
        if current_line:  # Desenha a última linha
            c.drawString(x, y, current_line)
            y -= line_height
    return y  # Retorna a nova posição Y

# Função para centralizar texto
def draw_centered_text(c, text, font, size, y_position):
    c.setFont(font, size)
    text_width = c.stringWidth(text, font, size)
    c.drawString((width - text_width) / 2, y_position, text)

# Carregar o arquivo CSV baixado do MEC
df = pd.read_csv("PDA_Dados_Cursos_Graduacao_Brasil (1).csv")

# Exibir as primeiras 5 linhas do dataset
print(df.head())

# Exibir estatísticas básicas dos dados
print(df.describe())

# Verifique as colunas disponíveis no DataFrame
print(df.columns)

# Filtrar dados
filtro = df[df["QT_VAGAS_AUTORIZADAS"] > 30]
print(df.isnull().sum())
df = df.drop_duplicates()

# Contagem de cursos por região
cursos_por_regiao = df["REGIAO"].value_counts()

# Plotar gráfico de barras para cursos por região
plt.figure(figsize=(10, 6))
sns.barplot(x=cursos_por_regiao.index, y=cursos_por_regiao.values)
plt.title("Número de Cursos por Região")
plt.xlabel("Região")
plt.ylabel("Número de Cursos")
plt.tight_layout()
plt.savefig("grafico_cursos_por_regiao.png")  # Salva o gráfico como imagem
plt.close()  # Fecha a figura

# Selecionar os 10 primeiros cursos e suas vagas autorizadas
df_top_cursos = df[["NOME_CURSO", "QT_VAGAS_AUTORIZADAS"]].head(10)

# Plotar gráfico de barras para os 10 cursos
plt.figure(figsize=(12, 6))
sns.barplot(x="NOME_CURSO", y="QT_VAGAS_AUTORIZADAS", data=df_top_cursos)
plt.title("Vagas Autorizadas para os 10 Primeiros Cursos")
plt.xlabel("Nome do Curso")
plt.ylabel("Quantidade de Vagas Autorizadas")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("grafico_vagas_top_cursos.png")  # Salva o gráfico como imagem
plt.close()  # Fecha a figura

# Criar o PDF
c = canvas.Canvas("Projeto Python.pdf", pagesize=A4)
width, height = A4

# Página 1: Capa de Apresentação
draw_centered_text(
    c, "Relatório de Análise de Cursos", "Helvetica-Bold", 24, height - 150
)
draw_centered_text(c, "Ministério da Educação - Brasil", "Helvetica", 18, height - 200)
draw_centered_text(c, "Projeto Python", "Helvetica", 18, height - 220)
draw_centered_text(c, "Autor: Marco Aurélio Junqueira Alcino", "Helvetica", 16, height - 300)
draw_centered_text(c, "Data: Outubro de 2024", "Helvetica", 16, height - 350)

# Adicionar uma borda ao redor da página (opcional)
c.setStrokeColor(colors.black)
c.rect(50, 50, width - 100, height - 100, stroke=1)

# Salvar a primeira página (capa)
c.showPage()

# Página 2: Título e Introdução
c.setFont("Helvetica-Bold", 16)
c.drawString(100, height - 50, "Relatório de Análise de Cursos")

# Adicionar Texto de Introdução
c.setFont("Helvetica", 10)
texto_introducao = """Este relatório apresenta uma análise detalhada dos dados relacionados aos cursos de 
graduação no Brasil, com ênfase na distribuição de cursos por região e na quantidade 
de vagas autorizadas para os principais cursos disponíveis. Os dados foram extraídos 
da base de dados do Ministério da Educação (MEC) e abrangem diversas instituições de 
ensino superior em todo o país."""

# Ajuste de linha
y = height - 80
y = draw_multiline_text(c, texto_introducao, 100, y, width - 200, 15)

# Adicionar mais texto se necessário
texto_anexo = (
    "A análise revela que a região Sudeste concentra o maior número de cursos, refletindo um acesso mais amplo à "
    "educação superior em comparação com outras regiões. Essa desigualdade na oferta educacional é um ponto de "
    "preocupação, uma vez que pode impactar as oportunidades de formação e desenvolvimento regional.\n\n"
    "Além disso, ao focar nos 10 cursos com mais vagas autorizadas, observamos que a demanda por áreas específicas, "
    "como saúde e engenharia, continua elevada, indicando tendências de mercado que podem guiar políticas de educação "
    "e formação profissional."
)

# Adiciona o texto anexo
y = draw_multiline_text(c, texto_anexo, 100, y, width - 200, 15)

# Página 3: Gráfico de Cursos por Região
c.showPage()
c.setFont("Helvetica-Bold", 16)
c.drawString(100, height - 50, "Cursos por Região")

# Adicionar Gráfico de Cursos como Imagem
grafico_caminho_regiao = "grafico_cursos_por_regiao.png"
if os.path.exists(grafico_caminho_regiao):
    c.drawImage(grafico_caminho_regiao, 50, height - 400, width=500, height=300)
else:
    print(f"Erro: O gráfico '{grafico_caminho_regiao}' não foi encontrado.")

# Página 4: Gráfico de Vagas dos 10 Cursos
c.showPage()
c.setFont("Helvetica-Bold", 16)
c.drawString(100, height - 50, "Vagas Autorizadas para os 10 Primeiros Cursos")

# Adicionar Gráfico de Vagas como Imagem
grafico_caminho_vagas = "grafico_vagas_top_cursos.png"
if os.path.exists(grafico_caminho_vagas):
    c.drawImage(grafico_caminho_vagas, 50, height - 400, width=500, height=300)
else:
    print(f"Erro: O gráfico '{grafico_caminho_vagas}' não foi encontrado.")

# Página 5: Comentários
c.showPage()
c.setFont("Helvetica-Bold", 16)
c.drawString(100, height - 50, "Comentários")

# Adicionar seção de comentários
comentarios = (
    "Este relatório buscou analisar a oferta de cursos de graduação no Brasil, "
    "considerando a quantidade de vagas autorizadas e a distribuição dos cursos entre as regiões. "
    "Os gráficos apresentados ilustram claramente as desigualdades regionais na educação superior. "
    "A concentração de cursos na região Sudeste indica um maior acesso à educação em comparação com outras regiões, "
    "sugerindo a necessidade de políticas públicas que incentivem a criação de cursos em áreas menos atendidas. "
    "Além disso, a forte demanda por cursos na área de saúde e engenharia destaca as tendências de mercado e a importância "
    "de adequar a formação acadêmica às necessidades do setor produtivo."
)

# Ajustar o tamanho da fonte para comentários
c.setFont("Helvetica", 10)

# Adiciona o texto de comentários
y = height - 80  # Posição inicial para os comentários
y = draw_multiline_text(c, comentarios, 100, y, width - 200, 15)

# Salvar e fechar o PDF
c.showPage()
c.save()

print("Relatório com capa gerado com sucesso: relatorio_com_capa.pdf")
