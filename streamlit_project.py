import streamlit as st

import streamlit_first as da
import streamlit_prediction as ma

import warnings
warnings.filterwarnings("ignore")
def main():
    # EDA
    da.main()

    st.header("SVM Model Predictor")

    # Predictor
    ma.main()

if(__name__ == '__main__'):
    main()
