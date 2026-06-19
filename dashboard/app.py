import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st #importa con alias. Todos los componentes visuales del dashboard se crean con st.algo()
import pandas as pd
from src.transform import load_raw, clean, engineer_features #Importa las tres funciones que ya construí (cargar, limpiar  y enriquecer los datos)
from src.queries import ( #Importa las cinco funciones de análisis que construimos en queries.py
    top_roles_by_salary,
    work_setting_distribution,
    offers_by_year,
    salary_by_experience,
    remote_trend_by_year
)
import matplotlib.pyplot as plt #librerias de visualización
import seaborn as sns

# Configuración de la página
st.set_page_config(
    page_title='Tech Jobs Analysis', #aparece en la pestaña del navegador
    page_icon='📊', #icono de la pestaña
    layout='wide' #hace que el dashboard use todo el ancho de la pantalla en lugar de centrarse en una columna estrecha
)

# Cargamos los datos una sola vez y los guardamos en caché
# sin caché, streamlit recarga los datos cada vez que el usuario interactúa. Esto hace el dashboard mucho más rápido
@st.cache_data
def load_data():
    df = load_raw('data/raw/jobs_in_data.csv')
    df = clean(df)
    df = engineer_features(df)
    return df

df = load_data() #llama a la función y guarda el dataframe en df. A partir de aqui todos los componentes del dashboard usan este df.

# Título y descripción
st.title('📊 Tech Jobs — Análisis del Mercado Laboral Tech') #Muestra el título principal del dashboard en grande
st.markdown('Exploración interactiva de 9.355 ofertas de empleo tech (2020–2023)') #Muestra el texto debajo del título. markdown acepta formato (negrita, cursiva...) igual que un README

# Dibuja una línea horizontal de separación. Puramente visual
st.divider()

# KPIs en la parte superior
col1, col2, col3 = st.columns(3) #Divide la pantalla en tres columnas iguales y les asigna nombres. Lo que se ponga dentro de cada with col1 aparece en esa columna

with col1:
    st.metric('Total ofertas', f"{len(df):,}") 

with col2:
    avg = int(df['salary_in_usd'].mean())
    st.metric('Salario medio', f"${avg:,}") #Calcula la media de salarios, la convierte a entero y la muestra con símbolo de dolar y separadores de miles.

with col3:
    pct = round(df['is_remote'].mean() * 100, 1)
    st.metric('% Trabajo remoto', f"{pct}%") #is_remote es true/false. La media de booleanos da la proporcion de true, multiplicada por 100 es el porcentaje
    
# Separador
st.divider()

# Sidebar con filtros
st.sidebar.header('Filtros') #Todo lo que aparece por st.sidebar. aparece en el panel lateral izquierdo, no en el área principal.

# Filtro por año
años = sorted(df['work_year'].unique())
año_seleccionado = st.sidebar.multiselect( #Crea un selector múltiple
    'Año',
    options=años, #opciones disponibles
    default=años #las que aparecen seleccionadas por defecto
)

# Filtro por modalidad
modalidades = sorted(df['work_setting'].unique())
modalidad_seleccionada = st.sidebar.multiselect(
    'Modalidad',
    options=modalidades,
    default=modalidades
)

# Filtro por experiencia
experiencias = ['Junior', 'Mid', 'Senior', 'Executive']
experiencia_seleccionada = st.sidebar.multiselect(
    'Nivel de experiencia',
    options=experiencias,
    default=experiencias
)

# Aplicamos los filtros al dataframe
df_filtered = df[
    (df['work_year'].isin(año_seleccionado)) &
    (df['work_setting'].isin(modalidad_seleccionada)) &
    (df['experience_group'].isin(experiencia_seleccionada))
]

# Aviso si no hay datos con los filtros aplicados
if df_filtered.empty:
    st.warning('No hay datos con los filtros seleccionados.')
    st.stop() #Detiene la ejecución del dashboard si no hay datos. Evita que los gráficos den error con un dataframe vacío.
    
# Configuración visual
sns.set_theme(style='whitegrid') #Establece el estilo visual global.

# Dividimos la pantalla en dos columnas para los gráficos
col_izq, col_der = st.columns(2)

# Gráfico 1 — Top roles por salario
with col_izq:
    st.subheader('Top 10 roles por salario medio')
    data = top_roles_by_salary(df_filtered) #Llama a la función de queries con el dataframe filtrado, no el original. Así cuando el usuario cambia un filtro en el sidebar, se actualiza.
    fig, ax = plt.subplots() #crea el lienzo y los ejes
    sns.barplot(data=data, x='avg_salary', y='job_title', ax=ax, color='steelblue') #dibuja el gráfico de barras horizontal
    ax.set_xlabel('Salario medio (USD)') #etiquetas de los ejes
    ax.set_ylabel('')
    plt.tight_layout() #Ajusta los márgenes automáticamente para que nada se corte
    st.pyplot(fig) #Le pasamos la figura y streamlit la renderiza dentro de la aplicación web
    plt.close() #cierra la figura y libera la memoria

# Gráfico 2 — Distribución modalidad
with col_der:
    st.subheader('Modalidad de trabajo')
    data = work_setting_distribution(df_filtered)
    fig, ax = plt.subplots()
    sns.barplot(data=data, x='work_setting', y='percentage', ax=ax, color='steelblue')
    ax.set_xlabel('')
    ax.set_ylabel('Porcentaje (%)')
    for i, row in data.iterrows(): #Añade el porcentaje por encima de cada barra
        ax.text(i, row['percentage'] + 0.5, f"{row['percentage']}%", ha='center')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

# Gráfico 3 — Evolución ofertas
with col_izq:
    st.subheader('Evolución de ofertas por año') #ocupa todo el ancho de la pantalla
    data = offers_by_year(df_filtered)
    fig, ax = plt.subplots()
    sns.lineplot(data=data, x='work_year', y='total_offers', ax=ax,
                 marker='o', linewidth=2.5, color='steelblue')
    ax.set_xlabel('')
    ax.set_ylabel('Número de ofertas')
    ax.set_xticks(data['work_year'])
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

# Gráfico 4 — Salario por experiencia
with col_der:
    st.subheader('Salario medio por experiencia')
    data = salary_by_experience(df_filtered)
    fig, ax = plt.subplots()
    sns.barplot(data=data, x='experience_group', y='avg_salary', ax=ax, color='steelblue')
    ax.set_xlabel('')
    ax.set_ylabel('Salario medio (USD)')
    for i, row in data.iterrows():
        ax.text(i, row['avg_salary'] + 1000, f"${int(row['avg_salary']):,}", ha='center')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

# Gráfico 5 — Tendencia remoto
st.subheader('Evolución del trabajo remoto por año')
data = remote_trend_by_year(df_filtered)
fig, ax = plt.subplots()
sns.lineplot(data=data, x='work_year', y='pct_remote', ax=ax,
             marker='o', linewidth=2.5, color='steelblue')
ax.set_xlabel('')
ax.set_ylabel('% trabajos remotos')
ax.set_xticks(data['work_year'])
plt.tight_layout()
st.pyplot(fig)
plt.close()

# Al final del dashboard añadimos una tabla interactiva con los datos filtrados. st.dataframe renderiza un dataframe de pandas como tabla HTML con scroll, 
# ordenación por columnas y búsqueda. Solo mostramos las columnas más relevantes para no saturar.
st.divider()
st.subheader('Datos filtrados')
st.dataframe(df_filtered[['job_title', 'job_category', 'salary_in_usd', 
                           'experience_group', 'work_setting', 'work_year']])

