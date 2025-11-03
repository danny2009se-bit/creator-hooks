import streamlit as st

st.set_page_config(page_title="Creator Hooks", page_icon="🎯")
st.title("🎯 Creator Hooks Pro")

# Palavras poderosas
poder = ['secreto', 'segredo', 'revelado', 'chocante', 'melhor', 'viral', 'incrível']
curiosidade = ['verdade', 'por que', 'mistério', 'revelação', 'desvendado']
medo = ['cuidado', 'perigo', 'aviso', 'grave', 'urgente']
desejo = ['ganhar', 'sucesso', 'rápido', 'fácil', 'dinheiro']

def score(titulo):
    pontos = 0
    t = titulo.lower()
    
    if 40 <= len(titulo) <= 65:
        pontos += 200
    if any(p in t for p in poder):
        pontos += 300
    if any(p in t for p in curiosidade):
        pontos += 150
    if any(p in t for p in medo):
        pontos += 125
    if any(p in t for p in desejo):
        pontos += 125
    if any(c.isdigit() for c in titulo):
        pontos += 100
    if '[' in titulo or '(' in titulo:
        pontos += 50
    if '?' in titulo or '!' in titulo:
        pontos += 75
    
    return min(1000, pontos)

st.subheader("📝 Modo Um: Analisar Títulos")
titulos = st.text_area("Cole seus títulos (um por linha):", height=120)

if st.button("🔍 Analisar", key="analisa"):
    if titulos:
        lista = [t.strip() for t in titulos.split('\n') if t.strip()]
        st.success(f"✅ {len(lista)} títulos analisados")
        
        for i, t in enumerate(lista[:5], 1):
            st.write(f"**{i}. {t}** - Score: {score(t)}/1000")

st.markdown("---")
st.subheader("✨ Modo Dois: Gerar Títulos")

tema = st.text_input("Digite o tema:")

sugestoes = [
    "Como {tema} em trinta dias",
    "O Segredo de {tema} Revelado",
    "{tema}: Verdade ou Mentira?",
    "Você Está Fazendo {tema} Errado!",
    "Cinco Dicas para {tema}",
    "Antes de {tema}, Veja Isto",
    "[IMPORTANTE] {tema} que Ninguém Sabe",
    "Descubra o Segredo de {tema}",
]

if st.button("🎯 Gerar", key="gera"):
    if tema:
        st.success("✅ Títulos gerados!")
        for i, sugestao in enumerate(sugestoes, 1):
            titulo = sugestao.format(tema=tema)
            st.write(f"**{i}. {titulo}** - Score: {score(titulo)}/1000")
    else:
        st.error("❌ Digite o tema!")

st.markdown("---")
st.caption("🚀 Creator Hooks Pro - Gerador de Títulos Virais")
