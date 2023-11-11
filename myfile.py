import streamlit as st
st.title("**COVID 19**")
st.subheader('El Perú se encuentra entre los países con menor tasa de enfermos confirmados del mundo.')
st.caption("**En este momento hay 221.727 personas fallecidas por coronavirus.**")
import pandas as pd
import numpy as np
import streamlit as st
import streamlit as st


# Enlace a un video de YouTube y su miniatura
video_link = "https://www.youtube.com/watch?v=ySRu9_R3jGM"
thumbnail_link = "https://i.ytimg.com/vi/ySRu9_R3jGM/maxresdefault.jpg"

# Mostrar la miniatura del video
st.image(thumbnail_link, caption="fuernte:AFP", use_column_width=True)

# Mostrar el enlace como un hipervínculo
st.markdown(f"[Ver video]( {video_link} )")



st.divider() 
st.write("Información en base a las edades")

st.caption("Desde los 0 hasta los 114")






my_range = range(1,115)

number = st.select_slider("Mueve el punto rojo en la edad que te interese", options=my_range)


import datetime
d = st.date_input(
"Fecha de decenso",
datetime.date(2019, 11, 6))
st.write('feha de fallecimiento:', d)

from datetime import datetime

st.link_button("ver en linea", "https://www.datosabiertos.gob.pe/dataset/fallecidos-por-covid-19-ministerio-de-salud-minsa") 
st.divider()

start_time = st.slider("Cifras de mortalidad", value=datetime(2022, 10, 1), format="DD/MM/YY")




chart_data = pd.DataFrame(
   {
       "col1": np.random.randn(20),
       "col2": np.random.randn(20),
       "col3": np.random.choice(["Mujeres", "Hombre", "Niños"], 20),
   }
)

st.line_chart(chart_data, x="col1", y="col2", color="col3")

st.write("Diversas ubicaciones")
# Crear un DataFrame con coordenadas de Perú (usando las coordenadas aproximadas de Lima)
peru_coordinates = pd.DataFrame({
    'lat': [-12.0464],  # Latitud de Lima
    'lon': [-77.0428]   # Longitud de Lima
})


# Visualizar los datos en un mapa centrado en Perú
st.map(peru_coordinates)






st.caption("**Datos sacados de repositorios del estado e INEI**")