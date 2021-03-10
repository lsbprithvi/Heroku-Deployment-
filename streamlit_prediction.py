import streamlit as st

from pickle import dump, load


import numpy as np

import warnings

warnings.filterwarnings("ignore")

def predicts(arr):
     # Loading pretrained logistic classifier from pickle file
    classifier = load(open('p_model.pkl', 'rb'))
    print("working")
    prediction =classifier.predict(arr)
    print(prediction)
    return prediction



def main():

    col1 = st.number_input('Test', value=1.)

    col2= st.number_input('Test1', value=1.)

    print(col1 + col2)

    arr = np.array([col1, col2]).reshape(1,-1)
    arr = arr.astype('float64')

    prediction = predicts(arr)

    if(prediction==1):

            st.write("Yes :sunglasses:")

            st.write(prediction)

    else:

            st.write("No :cry:")

            st.write(prediction)


if(__name__ == '__main__'):

    main()
