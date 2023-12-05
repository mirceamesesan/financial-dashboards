import streamlit as st
import pandas as pd
from services.payables import Payables
from services.receivables import Receivables

# Importing data

out_file = st.file_uploader('Upload your Payables here...')
in_file = st.file_uploader('Upload your Receivables here...')

if out_file:
    Payables.import_file(out_file)
    st.success('Data successfully imported!')

    payables = pd.read_excel(out_file)
    st.dataframe(payables)


if in_file:
    Receivables.import_file(in_file)
    st.success('Data successfully imported!')

    receivables = pd.read_excel(in_file)
    st.dataframe(receivables)