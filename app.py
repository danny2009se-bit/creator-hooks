import streamlit as st

st.set_page_config(page_title="Creator Hooks", page_icon="🎯")

st.title("🎯 Creator Hooks")
st.subheader("Gerador Automático de Títulos Virais para YouTube")

PALAVRAS_PODER = ['secreto', 'segredo', 'revelado', 'descoberta', 'chocante', 'melhor', 'pior', 'impossível', 'viral', 'medo']

def calcular_score(titulo):
    score = 0
    if 40 <= len(titulo) <= 65: score += 200
    if any(p in titulo.lower() for p in PALAVRAS_PODER): score += 300
    if '?' in titulo or '!' in titulo: score += 75
    return min(1000, score)

tipo_titulo = st.selectbox("Escolha o tipo:", ["Motivacional", "Educativo", "Histórias", "Tutorial", "Saúde", "Negócios", "Humor", "Tendências"])

if st.button("🔍 Gerar Títulos"):
    titulos = {
        'Motivacional': ['Como Transformar Sua Vida em trinta dias', 'O Segredo que Ninguém te Contou', 'Você está Fazendo Errado. Aprenda Agora', 'Cinco Passos para Sucesso Garantido', 'A Verdade que Mudará Sua Perspectiva', 'Isto é Revolucionário', 'Antes que Seja Tarde, Veja Isto'],
        'Educativo': ['Como Aprender Rápido: Guia Completo', 'Entenda de Uma Vez por Todas', 'Explicado em Dez Minutos', 'O Método Mais Eficaz Revelado', 'Domínio Total em Quarenta Minutos', 'Desvende o Mistério Agora', 'Tudo que Você Precisa Saber'],
        'Histórias': ['A Verdade que Ninguém Sabia', 'Isso Que Aconteceu Vai te Chocar', 'Você não Acreditará no Final', 'Uma História que Mudou Tudo', 'O Segredo Está Revelado', 'Prepare-se: Revelação Chocante', 'Esse Final Vai te Deixar em Choque'],
        'Tutorial': ['Como Fazer em Cinco Minutos', 'Método Infalível: Siga Agora', 'Passo a Passo Completo e Fácil', 'Resultado Garantido', 'Assim fica Muito Mais Fácil', 'Saiba Como Fazer Corretamente', 'Entenda a Técnica Profissional'],
        'Saúde': ['Dez Hábitos que Mudam Sua Saúde', 'Médicos Escondem Esta Verdade', 'Como Viver Mais Saudável Agora', 'Isto Vai Mudar Sua Vida', 'O Que Ninguém Quer que Você Saiba', 'Antes de Tomar, Veja Isto', 'Segredo Centenário Revelado'],
        'Negócios': ['Como Lucrar Cinco Mil por Mês', 'Empreendedor Revela Seu Segredo', 'De Zero a Herói em Noventa Dias', 'Isto Gera Dinheiro Passivo', 'Método Testado para Crescer Rápido', 'Erro Fatal que Custou Milhões', 'Você Pode Ganhar Assim Também'],
        'Humor': ['Isto É Hilariante', 'Você Vai Morrer de Rir', 'Reação Verdadeira', 'Algo Extremamente Engraçado Aconteceu', 'Prepare-se para Rir Muito', 'Isso é Tão Ridículo', 'Confira a Parte Mais Divertida'],
        'Tendências': ['A Tendência Viral que Explodiu', 'Todos Estão Fazendo Isto Agora', 'Viral: Milhões de Pessoas Assistindo', 'Isto É Bombando Neste Momento', 'Novo Desafio que Virou Febre', 'Resultado Surpreendente: Veja Agora', 'Isto Deixou a Internet em Choque']
    }
    
    lista = titulos.get(tipo_titulo, [])
    scored = [(t, calcular_score(t)) for t in lista]
    scored.sort(key=lambda x: x[1], reverse=True)
    
    st.success("✅ Títulos gerados!")
    for i, (titulo, score) in enumerate(scored, 1):
        st.write(f"**{i}. {titulo}**")
        st.caption(f"📊 Score: {score}/1000")
