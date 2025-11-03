import streamlit as st
from collections import Counter

st.set_page_config(page_title="Creator Hooks Pro", page_icon="🎯", layout="wide")

st.title("🎯 Creator Hooks Pro")
st.subheader("Gerador Inteligente de Títulos Virais para YouTube")

PALAVRAS_DE_PODER = [
    'secreto', 'segredo', 'revelado', 'descoberta', 'chocante', 'inacreditável',
    'melhor', 'pior', 'impossível', 'viral', 'medo', 'dica', 'truque', 'hack',
    'método', 'como', 'verdade', 'incrível', 'fantástico', 'realidade'
]

PALAVRAS_CURIOSIDADE = [
    'segredo', 'descoberta', 'surpreendente', 'verdade', 'revelação', 'mistério',
    'por que', 'o que', 'será', 'desvendado', 'choque', 'surpreender'
]

PALAVRAS_MEDO = [
    'cuidado', 'atenção', 'perigo', 'risco', 'pior', 'nunca', 'horror',
    'medo', 'aviso', 'antes que', 'errado', 'grave', 'urgente'
]

PALAVRAS_DESEJO = [
    'melhor', 'ganhar', 'lucrar', 'rico', 'sucesso', 'crescer', 'aumentar',
    'dinheiro', 'renda', 'liberdade', 'poder', 'fácil', 'rápido', 'simples',
    'resultado', 'transformação', 'mudança', 'evolução'
]

def calcular_score(titulo):
    score = 0
    titulo_lower = titulo.lower()
    
    if 40 <= len(titulo) <= 65:
        score += 200
    
    if any(p in titulo_lower for p in PALAVRAS_DE_PODER):
        score += 300
    
    if any(p in titulo_lower for p in PALAVRAS_CURIOSIDADE):
        score += 150
    
    if any(p in titulo_lower for p in PALAVRAS_MEDO):
        score += 125
    
    if any(p in titulo_lower for p in PALAVRAS_DESEJO):
        score += 125
    
    if any(c.isdigit() for c in titulo):
        score += 100
    
    if '[' in titulo or '(' in titulo:
        score += 50
    
    if '?' in titulo or '!' in titulo:
        score += 75
    
    return min(1000, score)

def detectar_emocao(titulo):
    titulo_lower = titulo.lower()
    
    curiosidade = sum(1 for p in PALAVRAS_CURIOSIDADE if p in titulo_lower)
    medo = sum(1 for p in PALAVRAS_MEDO if p in titulo_lower)
    desejo = sum(1 for p in PALAVRAS
