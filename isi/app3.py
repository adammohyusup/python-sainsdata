# import module
import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
from matplotlib import pyplot as plt
from PIL import Image
import plotly_express as px
import time


test = st.sidebar.radio("Navigation", ['Home', 'Columns', 'Tabs', 'expander & container'])

if test == "Home":
    st.subheader("Data Covid 19")
    st.write(
            """
           - 10122206 - Farhan Fahrezi Santosa (Kontribusi : Scrapping)
           - 10122208 - Fila Desta Andanda (Kontribusi : Visualisasi)
           - 10122212 - Kevin Juniawan (Kontribusi : Tampilan Aplikasi)
           - 10122220 - Adam Mohamad Yusup Hanapi (Kontribusi : Geographic Information system)
           - 10122224 – JEC FAREN SITUMORANG (Kontribusi : visualisasi)


          """
        )
    

    st.write("---")

    st.write(
            """
            latar belakang : Pada 2020, pandemi COVID-19 melanda dunia, termasuk Indonesia. 
            Penyebaran virus ini memicu respons pemerintah dan masyarakat untuk mengatasi dampaknya
            Tujuan : Pembuatan data COVID-19 di Indonesia bertujuan untuk memberikan informasi akurat dan terkini tentang perkembangan pandemi. 
            Tujuannya meliputi pemantauan, pengambilan keputusan, kesadaran masyarakat, dan keterbukaan pemerintah dalam menangani situasi ini. 
            Data ini menjadi dasar untuk langkah-langkah pencegahan dan penanganan yang efektif..


          """
        )

# Halaman Columns

# Contoh (data berupa dataset)
if test == "Columns":
    st.subheader("Data Covid 19")
    st.write("Menampilkan Grafik")

    col1, col2 = st.columns([3, 1])
    data = pd.read_csv("dataset/datagaji1.csv") 


    col1.subheader("Menapilkan data dengan grafik")
    col1.line_chart(data)

    col2.subheader("Menapilkan data dengan tabel")
    col2.write(data)

# Halaman Tabs

if test == "Tabs":
    st.subheader("GAMBAR")
    st.write("tabs")

    # Contoh yang pertama (data berupa gambar)
    tab1, tab2, tab3 = st.tabs(["Gambar 1", "Gambar 2", "Gambar 3"])

    # Pengambilan data
    gambar2 = Image.open('img/img1.png')
    gambar3 = Image.open('img/img2.png')
    gambar4 = Image.open('img/img3.png')

    with tab1:
        st.header("Gambar 1")
        st.image(gambar2, width=200)
    with tab2:
        st.header("Gambar 2")
        st.image(gambar3, width=200)

    with tab3:
        st.header("Gambar 3")
        st.image(gambar4, width=200)

    
    st.write("---")
    
    
    tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
    data = pd.read_csv("dataset/datagaji1.csv") 

    tab1.subheader("Menapilkan data dengan chart")
    tab1.line_chart(data)

    tab2.subheader("Menapilkan data dengan tabel")
    tab2.write(data)



if test == "expander & container":
    st.subheader("Map Dan Diagram")
    st.write(" Map & container")
    # Pemngambilan data
    data = pd.read_csv("dataset/datagaji1.csv")
    gambar = Image.open('img/map1.png')

    # Contoh Expander
    st.bar_chart(data)
    with st.expander(" expander"):
        st.write("""
        expander dan
       visualisasikan 
        """)
        st.image(gambar)

    # Contoh Container
    with st.container():
        st.write("Map")
        st.bar_chart(data)

    st.write("container")
    



