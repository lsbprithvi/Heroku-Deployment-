import streamlit as st

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")

dataset_loc = pd.read_csv("streamlit_dataset.csv")

def load_description(df):
        # Preview of the dataset

        st.header("Data Preview")
        preview = st.radio("Choose Head/Tail?", ("Top", "Bottom"))
        if(preview == "Top"):
            st.write(df.head())
        if(preview == "Bottom"):
            st.write(df.tail())

        # display the whole dataset
        if(st.checkbox("Show complete Dataset")):
            st.write(df)

        # Show shape
        if(st.checkbox("Display the shape")):
            st.write(df.shape)
            dim = st.radio("Rows/Columns?", ("Rows", "Columns"))
            if(dim == "Rows"):
                st.write("Number of Rows", df.shape[0])
            if(dim == "Columns"):
                st.write("Number of Columns", df.shape[1])

        # show columns
        if(st.checkbox("Show the Columns")):
            st.write(df.columns)


def visual(df):
    fig = plt.figure()
    sns.countplot(x='output', data=df)
    fig.set_figheight(3)
    fig.set_figwidth(5)
    st.pyplot(fig)
    st.title("Pair Plot")
    fig = sns.pairplot(df, hue="output")
    fig.fig.set_figheight(6)
    fig.fig.set_figwidth(10)
    st.pyplot(fig)
def main():



    # Title/ text
    st.title('Srtrealit Exam Data Analysis')






    # display description
    load_description(dataset_loc)
    visual(dataset_loc)



if(__name__ == '__main__'):
    main()
