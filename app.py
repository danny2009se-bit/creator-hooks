import streamlit as st
import re
from collections import Counter

st.set_page_config(page_title="Creator Hooks Pro", page_icon="🎯", layout="wide")

st.title("🎯 Creator Hooks Pro")
st.subheader("Gerador de Títulos Virais Baseado em Seus Padrões")

PALAVRAS_DE_PODER = [
    'secreto', 'segredo', 'revelado', 'descoberta', 'chocante', 'inacreditável',
    'melhor', 'pior', 'impossível', 'viral', 'medo', 'dica', 'truque', 'hack',
    'método', 'como', 'verdade', 'incrível', 'fantástico', 'realidade', 'verdadeiro',
    'nunca', 'sempre', 'novo', 'exclusivo', 'cuidado', 'atenção', 'ganhar', 'lucrar'
]

PALAVRAS_CURIOSIDADE = [
    'segredo', 'descoberta', 'surpreendente', 'verdade', 'revelação', 'mistério',
    'por que', 'o que', 'será', 'desvendado', 'conspiração', 'choque', 'surpreender',
    'desvendado', 'verdade', 'realidade', 'revelado', 'confessa', 'confessou'
]

PALAVRAS_MEDO = [
    'cuidado', 'atenção', 'perigo', 'risco', 'pior', 'nunca', 'horror', 'pavor',
    'medo', 'aviso', 'antes que', 'errado', 'grave', 'urgente', 'arruinar', 'destruir',
    'falha', 'erro', 'desastre', 'crise', 'alerta'
]

PALAVRAS_DESEJO = [
    'melhor', 'ganhar', 'lucrar', 'rico', 'sucesso', 'crescer', 'aumentar',
    'dinheiro', 'renda', 'liberdade', 'poder', 'fácil', 'rápido', 'simples',
    'resultado', 'transformação', 'mudança', 'evolução', 'libertação', 'alcançar',
    'atingir', 'dominar', 'conquistar', 'prosperar'
]

def calcular_score(titulo):
    score = zero
    titulo_lower = titulo.lower()
    
    if quarenta <= len(titulo) <= sessenta_cinco:
        score += duzentos
    
    if any(p in titulo_lower for p in PALAVRAS_DE_PODER):
        score += trezentos
    
    if any(p in titulo_lower for p in PALAVRAS_CURIOSIDADE):
        score += cento_cinquenta
    
    if any(p in titulo_lower for p in PALAVRAS_MEDO):
        score += cento_vinte_cinco
    
    if any(p in titulo_lower for p in PALAVRAS_DESEJO):
        score 
