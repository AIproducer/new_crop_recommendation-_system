# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 10:58:38 2022

@author: M_ISHFAQ
"""

import pandas as pd
from ipywidgets import interact
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


df1 = pd.read_csv('data.csv')


#loading the saved model
model_rf_1 = pickle.load(open('model_rf.pkl','rb'))

def main():
    with st.sidebar:
        selected = option_menu('Crop Recommendation System',
                               ['Crop Recommendation By Gredients',
                                'Recommend Grediends For Crops',
                                'Averge Level of Gredients for Crops',
                                'Crops Recommended by Season'],
                               default_index=0)
    
#Diabetes Prediction Page
    if(selected=='Crop Recommendation By Gredients'):
   
    
    # title
   
        st.title('Crop Recommendation By Gredients')
    # getting the data from the users
    

        N=st.text_input('Nitrogen Level')
        P=st.text_input('Phosphorse Level')
        K=st.text_input('Potassium Level')
        temp=st.text_input('Temprature Level')
        hum=st.text_input('Humidity Level')
        ph=st.text_input('PH Level')
    
    
    #code for Prediction
        crop=''
    
    
    
    
    # creating a button for prediction
        if st.button('Crop Recommendation'):
            crop= model_rf_1([N, P, K, temp, hum, ph])
    
        st.success(crop)
    
    if(selected=='Recommend Grediends For Crops'):
        st.title('Recommend Grediends For Crops' )

#  leat check the summary statistics for each of the crops 
    @interact 
    def summary(crops = list(df1['label'].value_counts().index)):
        x = df1[df1['label']==crops]
        print('-----------------------------------------------')
        print('Statistic for Nitrogen')
        print('Minimum Nitrogen required :',x['N'].min())
        print('Average Nitrogen required :',x['N'].mean())
        print('Maximum Nitrogen required :',x['N'].max())
        print("------------------------------------------------")
        print('Statistic for Nitrogen')
        print('Minimum phosphorous required :',x['P'].min())
        print('Average phosphorous required :',x['P'].mean())
        print('Maximum phosphorous required :',x['P'].max())
        print("------------------------------------------------")
        print('Statistic for Nitrogen')
        print('Minimum potassium required :',x['K'].min())
        print('Average potassium required :',x['K'].mean())
        print('Maximum potassium required :',x['K'].max())
        print("------------------------------------------------")
        print("Statistic for temperature")
        print("Minimum Temperature required : {0:2f}".format(x['temperature'].min()))
        print("Average Temperature required : {0:2f}".format(x['temperature'].mean()))
        print("Maximum Temperature required : {0:2f}".format(x['temperature'].max()))
        print("------------------------------------------------")
        print("Statistic for humidity")
        print("Minimum humidity required : {0:2f}".format(x['humidity'].min()))
        print("Average humidity required : {0:2f}".format(x['humidity'].mean()))
        print("Maximum humidity required : {0:2f}".format(x['humidity'].max()))
        print("------------------------------------------------")
        print("Statistic for rainfall")
        print("Minimum rainfall required : {0:2f}".format(x['rainfall'].min()))
        print("Average rainfall required : {0:2f}".format(x['rainfall'].mean()))
        print("Maximum rainfall required : {0:2f}".format(x['rainfall'].max()))
        print("Statistic for ph")
        print("Minimum ph required : {0:2f}".format(x['ph'].min()))
        print("Average ph required : {0:2f}".format(x['ph'].mean()))
        print("Maximum ph required : {0:2f}".format(x['ph'].max()))
    
    
    
    
    if(selected=='Averge Level of Gredients for Crops'):
        st.title('Averge Level of Gredients for Crops' )

    @interact
    def compare(conditions = ['N','P','K','temperature','ph','humidity','rainfall']):
        print('Average value for',conditions,'is {0:.2f}'.format(df1[conditions].mean()))
        print("------------------------------------------------------------------------")
        print('Rice : {0:2f}'.format(df1[(df1['label']=='rice')][conditions].mean()))
        print('lentil : {0:2f}'.format(df1[(df1['label']=='lentil')][conditions].mean()))
        print('cotton : {0:2f}'.format(df1[(df1['label']=='cotton')][conditions].mean()))
        print('mungbean : {0:2f}'.format(df1[(df1['label']=='mungbean')][conditions].mean()))
        print('jute : {0:2f}'.format(df1[(df1['label']=='jute')][conditions].mean()))
        print('muskmelon : {0:2f}'.format(df1[(df1['label']=='muskmelon')][conditions].mean()))
        print('blackgram : {0:2f}'.format(df1[(df1['label']=='blackgram')][conditions].mean()))
        print('papaya : {0:2f}'.format(df1[(df1['label']=='papaya')][conditions].mean()))
        print('orange : {0:2f}'.format(df1[(df1['label']=='orange')][conditions].mean()))
        print('apple : {0:2f}'.format(df1[(df1['label']=='apple')][conditions].mean()))
        print('pigeonpeas : {0:2f}'.format(df1[(df1['label']=='pigeonpeas')][conditions].mean()))
        print('coffee : {0:2f}'.format(df1[(df1['label']=='coffee')][conditions].mean())) 
        print('maize : {0:2f}'.format(df1[(df1['label']=='maize')][conditions].mean()))
        print('chickpea : {0:2f}'.format(df1[(df1['label']=='chickpea')][conditions].mean()))
        print('pomegranate : {0:2f}'.format(df1[(df1['label']=='pomegranate')][conditions].mean()))
        print('kidneybeans : {0:2f}'.format(df1[(df1['label']=='kidneybeans')][conditions].mean()))
        print('mango : {0:2f}'.format(df1[(df1['label']=='mango')][conditions].mean()))
        print('banana : {0:2f}'.format(df1[(df1['label']=='banana')][conditions].mean()))
        print('grapes : {0:2f}'.format(df1[(df1['label']=='grapes')][conditions].mean()))
        print('mothbeans : {0:2f}'.format(df1[(df1['label']=='mothbeans')][conditions].mean()))
        print('watermelon : {0:2f}'.format(df1[(df1['label']=='watermelon')][conditions].mean()))
        print('coconut : {0:2f}'.format(df1[df1['label']=='coconut'][conditions].mean()))
    
    
    if(selected=='Crops Recommended by Season'):
         st.title('Crops Recommended by Season' )

    @interact
    def compare(conditions = ['N','P','K','temperature','ph','humidity','rainfall']):
        print("crops which required grater than average",conditions,'\n')
        print(df1[df1[conditions]> df1[conditions].mean()]['label'].unique())
        print("-----------------------------------------------------------")
        print("crops which required less than average",conditions,'\n')
        print(df1[df1[conditions] <= df1[conditions].mean()]['label'].unique())
            

    
    
   
    
    
if __name__=='__main__':
    main()
    