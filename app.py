import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

st.image("./pic/images.jpg")


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