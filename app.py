# APP COMPLETO COM YOUTUBE API - CREATOR HOOKS

import streamlit as st
import requests
import re
from collections import Counter
from datetime import datetime

# Sua chave de API (substitua pela sua)
YOUTUBE_API_KEY = "AIzaSyAYTbQ4AlTsCGZbmdR2bcTO7UMVNc1PUMM"
CHANNEL_ID = "UCUNyUhriEplPgCep5LkpdGg"

st.set_page_config(page_title="Creator Hooks Pro", page_icon="🎯", layout="wide")

st.title("🎯 Creator Hooks Pro")
st.subheader("Analisador Inteligente de Títulos do Seu Canal YouTube")

PALAVRAS_DE_PODER = [
    'secreto', 'segredo', 'revelado', 'descoberta', 'chocante', 'inacreditável',
    'melhor', 'pior', 'impossível', 'viral', 'medo', 'dica', 'truque', 'hack',
    'método', 'como', 'verdade', 'incrível', 'fantástico', 'realidade', 'verdadeiro'
]

PALAVRAS_CURIOSIDADE = [
    'segredo', 'descoberta', 'surpreendente', 'verdade', 'revelação', 'mistério',
    'por que', 'o que', 'será', 'desvendado', 'conspiração', 'choque', 'surpreender'
]

PALAVRAS_MEDO = [
    'cuidado', 'atenção', 'perigo', 'risco', 'pior', 'nunca', 'horror', 'pavor',
    'medo', 'aviso', 'antes que', 'errado', 'grave', 'urgente', 'arruinar', 'destruir'
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
    
    if '?' in titulo or 
