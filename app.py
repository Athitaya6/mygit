import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import pickle


st.image("./pic/1.jpg")

html_8 = """
<div style="background-color:#99DF99;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายข้อมูลดอกไม้</h5></center>
</div>
"""

st.markdown(html_8, unsafe_allow_html=True)
st.markdown("")
st.header("การจำแนกข้อมูล")
st.subheader("1.ตัวอย่างการจำแนกข้อมูล")
st.balloons()

dt=pd.read_csv("./data/iris.csv")


st.write(dt.head(10))

dt1 = dt['petal.length'].sum()
dt2 = dt['petal.width'].sum()
dt3 = dt['sepal.length'].sum()
dt4 = dt['sepal.width'].sum()

dx = [dt1, dt2, dt3, dt4]
dx2 = pd.DataFrame(dx, index=["d1", "d2", "d3", "d4"])

if st.button("แสดงการจินตทัศน์ข้อมูล"):
   #st.write(dt.head(10))
   st.bar_chart(dx2)
   st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")

    html_8 = """
<div style="background-color:#6BD5DA;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>ทำนายข้อมูล</h5></center>
</div>
"""
st.markdown(html_8, unsafe_allow_html=True)
st.markdown("")

pt_len=st.slider("กรุณาเลือกข้อมูล petal.length")
pt_wd=st.slider("กรุณาเลือกข้อมูล petal.width")
sp_len=st.number_input("กรุณาเลือกข้อมูล sepal.length")
sp_wd=st.number_input("กรุณาเลือกข้อมูล sepal.width")

if st.button("ทำนายผล"):
   #st.markdown("ใส่โมเดล")
   
    pickle_in=open('./model/Knn_model1.pkl','rb')
    knnModel1=pickle.load(pickle_in)

    input_data =  (7,	1,	2,	1)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = knnModel1.predict(input_data_reshaped)
    st.write(prediction)

    st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")
