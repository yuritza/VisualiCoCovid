import streamlit as st
##agregamos streamlit para nuestro servidor
import pandas as pd
## agregamos pandas para cargar los datos
import matplotlib.pyplot as plt
##importamos matplotlib
import numpy as np
#agregamos numpy
import seaborn as sns
#agregamos para embellecer con seaborns
sns.set_style("darkgrid")

## se agrega titulo a la app
st.title("Visualizacion datos Covid-19 Chile")

#Texto
st.markdown("## Bienvenido al visualizador")
df = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto3/TotalesPorRegion.csv")
##se agregan dos columnas :

columna1,columna2=st.columns(2)

#st.data.frame(dt)
with columna1:
    region = st.radio("Region",df.Region.unique())
    st.markdown("Su seleciion es :"+region)
with columna2:
    categoria = st.radio("Categoria",df.Categoria.unique())
    st.markdown("Su seleccion es :"+categoria)

ilocs=df.iloc[:,2:-1]
super_filtro=df[(df.Region==region)&(df.Categoria==categoria)]
st.table(ilocs.head(10))
st.dataframe(super_filtro)
fig,ax = plt.subplots()
to_plot=super_filtro.iloc[:,2:-1]
ax.plot(to_plot.T)
ax.set_title(region)
ax.set_xlabel("Fecha")
ax.set_ylabel(categoria)
xs=np.arange(0,super_filtro.shape[1]-2,30)
plt.xticks(xs,rotation=90)
st.pyplot(fig)