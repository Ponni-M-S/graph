import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#title
st.title("acer")


#Image
st.image("streamlit.gif",width=250)
st.title("case study on acer laptop front page")

data=sns.load_dataset("diamonds")
st.write("shape of a dataset",data.shape)
menu=st.sidebar.radio("menu",["home","prediction price"])
st.header("tabular data of a diamond")
if st.checkbox("tablur data"):
   st.table(data.head(5))
   st.header("statistical summary of a dataframe")
   if st.checkbox("statistics"):
       st.table(data.describe())

       st.title("graphs")
       graph=st.selectbox("different types of graphs",["scatter plot","bar graph","histogram"])
       if graph=="scatter plot":
           value=st.slider("filter data using carat",0,6)
           data= data.loc[data["carat"]>=value]
           fig,ax=plt.subplots(figsize=(4,5))
           
           sns.scatterplot(data=data,x="carat",y="price",hue="cut")
           st.pyplot(fig)
           if graph=="bar graph":
               fig,ax=plt.subplots(figsize=(2,3))
               sns.barplot(x="cut",y="data.cut.index,data=data")
               st.pyplot(fig)
           if graph=="histogram":
                figax=plt.subplots(figsize=(5,3))
                sns.displot(data.price,kde=True)
                st.pyplot(fig)
                if menu=="prediction price":
                    st.title("prediction price of a diamond")
                from sklearn.linear_model import LinearRegression
                lr=LinearRegression
                x=np.array(data["carat"]).reshape(-1,1)
                y=np.array(data["price"].reshape-1,1)
                lr.fit(x,y)
                st.number_input("carrot",0.20,5.01,step=0.15)
                value=np.array(value).reshape(1,-1)
                prediction=lr.predict(value)[0]
                if  st.button("price prediction($)"):
                   st.write(f"{prediction}")

                
           
       
       

