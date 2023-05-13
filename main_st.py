import streamlit as st

from funciones import *
from tablaHash import HashTable

archivo = st.file_uploader("Cargar archivo", type=['csv', 'txt'])

if archivo is not None:
    datos=leerArchivo(archivo)
    st.write(datos)

    tamanio=st.number_input(label="Seleccione el tamaño", min_value=len(datos), max_value=None)

    if tamanio:
        tabla=HashTable(tamanio, 0)
        for i in range(len(datos)):
            tabla.ingresarDatos(int(datos[i][0]))
        st.write(tabla.getTabla())
        st.write(f"\nTamaño: {tabla.getTamanio()}")
        st.write(f"\nOcupación: {tabla.getOcupacion()*100:.2f}%")
        st.write(f"\nColisiones: {tabla.getColisiones()}")