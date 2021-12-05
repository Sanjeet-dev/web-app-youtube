# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 11:30:13 2021

@author: Monal Rai
"""
# imports
import streamlit as st
import pandas as pd
import seaborn as sns


# Title and Subheader
st.title('Data Analysis')
st.subheader('Data Analysis using Python & Streamlit')

# upload dataset
upload = st.file_uploader('Upload your dataset (In CSV format)')
if upload is not None:
    data=pd.read_csv(upload)

# show dataset
if st.checkbox('Preview Dataset'):
    if st.button('Head'):
        st.write(data.head())
    if st.button('Tail'):
        st.write(data.tail())


    
# Find shape of Our Dataset (Number of rows and columns)
if upload is not None:
    data_shape = st.radio('What dimension Do you want to check?',('Rows','Columns'))
    if data_shape== 'Rows':
        st.text('number of rows')
        st.write(data.shape[0])
    if data_shape == 'Columns':
        st.text('number of columns')
        st.write(data.shape[1])
        
            
# Find Duplicate Values in the dataset

if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning("This Dataset Contains Some Duplicate Values")
        dup=st.selectbox("Do You Want to Remove Duplicate Values?", \
                         ("Select One","Yes","No"))
        if dup=="Yes":
            data=data.drop_duplicates()
            st.text("Duplicate Values are Removed")
        if dup=="No":
            st.text("Ok No Problem")
            

# About Section

if st.button("About App"):
    st.text("Built With Streamlit")
    st.text("Thanks To Streamlit")


# By
if st.checkbox("By"):
    st.success("Sanjeet Rai")
            

            
        