import streamlit as st
import pandas as pd


st.title("Financial Dashboard")

# Add sidebar
st.sidebar.header("Upload your documents")

# 
# Looking into the Revenue data
#
st.sidebar.header("Revenue")
in_doc = st.sidebar.file_uploader("Upload your IN document", type=("xlsx"))

if in_doc:
    in_doc_df = pd.read_excel(in_doc)
    total_income = in_doc_df['Amount'].sum()

    st.write(f"Revenue: {total_income:,.2f}")
    st.dataframe(in_doc_df)


# 
# Looking into the Expenses data
#
st.sidebar.header("Expenses")
out_doc = st.sidebar.file_uploader("Upload your OUT document", type=("xlsx"))

if out_doc:
    out_doc_df = pd.read_excel(out_doc)
    total_expenses = out_doc_df['Amount'].sum()

    st.write(f"Expenses: {total_expenses:,.2f}")
    st.dataframe(out_doc_df)


