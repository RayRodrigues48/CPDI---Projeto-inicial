import streamlit as st
import pandas as pd
import os

# Define o arquivo onde os dados serão salvos permanentemente
ARQUIVO_DADOS = 'historico_financeiro.csv'

# Carrega o histórico existente ou cria uma estrutura vazia se for a primeira vez
if os.path.exists(ARQUIVO_DADOS):
    df = pd.read_csv(ARQUIVO_DADOS)
else:
    df = pd.DataFrame(columns=['Data', 'Tipo', 'Descrição', 'Valor'])

# Configuração da página
st.set_page_config(page_title="Controle Financeiro", layout="centered")
st.title("Controle Financeiro Simples")

# Seção 1: Formulário para adicionar novas transações
with st.form("nova_transacao"):
    st.subheader("Nova Transação")
    data = st.date_input("Data")
    tipo = st.selectbox("Tipo de Movimentação", ["Entrada", "Saída"])
    descricao = st.text_input("Descrição (ex: Venda de produto, Conta de luz)")
    valor = st.number_input("Valor (R$)", min_value=0.01, format="%.2f", step=10.0)
    
    submit = st.form_submit_button("Registrar")

    if submit:
        # Cria um novo registro e adiciona ao histórico
        novo_registro = pd.DataFrame({
            'Data': [data],
            'Tipo': [tipo],
            'Descrição': [descricao],
            'Valor': [valor]
        })
        df = pd.concat([df, novo_registro], ignore_index=True)
        df.to_csv(ARQUIVO_DADOS, index=False) # Salva no arquivo CSV
        st.success("Transação registrada com sucesso!")
        st.rerun() # Atualiza a tela para mostrar os novos dados

# Seção 2: Cálculo de Saldo e Resumo
if not df.empty:
    # Filtra e soma as entradas e saídas
    entradas = df[df['Tipo'] == 'Entrada']['Valor'].sum()
    saidas = df[df['Tipo'] == 'Saída']['Valor'].sum()
    saldo = entradas - saidas

    # Exibe os indicadores em três colunas visuais
    st.subheader("Resumo Geral")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Entradas", f"R$ {entradas:.2f}")
    col2.metric("Total de Saídas", f"R$ {saidas:.2f}")
    col3.metric("Saldo Atual", f"R$ {saldo:.2f}")

    # Seção 3: Histórico Detalhado
    st.subheader("Histórico de Movimentações")
    # Exibe a tabela formatada
    st.dataframe(
        df,
        column_config={
            "Valor": st.column_config.NumberColumn("Valor", format="R$ %.2f")
        },
        hide_index=True,
        use_container_width=True
    )
else:
    st.info("Nenhuma transação registrada ainda. Adicione uma movimentação acima.")