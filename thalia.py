# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 15:35:32 2025

@author: alexa
"""

import streamlit as st

def calcular_otimo(a, b, c):
    if a == 0:
        return "Coeficiente 'a' não pode ser zero."
    
    x_otimo = -b / (2 * a)
    tipo = "mínimo" if a > 0 else "máximo"
    return f"O valor de x que {tipo} a função é: {x_otimo:.4f}"

st.title("Thalia - Otimização de Função Quadrática")

st.write("Informe os coeficientes da função f(x) = ax² + bx + c:")

a = st.number_input("Coeficiente AA", format="%.4f")
b = st.number_input("Coeficiente BB", format="%.4f")
c = st.number_input("Coeficiente CC", format="%.4f")

if st.button("Otimizar"):
    resultado = calcular_otimo(a, b, c)
    st.success(resultado)
    
    
