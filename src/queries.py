import pandas as pd

# Agrupo todas las filas por título de trabajo, y calcula la media salarial y el número de ofertas de cada uno. Luego ordena de mayor a menor salario y se queda con los N primeros. 
def top_roles_by_salary(df, n=10):

    return (
        df.groupby('job_title')['salary_in_usd']
        .agg(avg_salary='mean', total_offers='count')
        .round(0)
        .sort_values('avg_salary', ascending=False)
        .head(n)
        .reset_index() # Convierte el índice en una columna normal para que sea más fácil de usar después
    )

# Cuenta cuántas filas hay de cada modalidad (remote, hybrid, in-person) y lo convierte en porcentaje sobre el total. 
def work_setting_distribution(df): 
    # Distribución de modalidad de trabajo en porcentaje
    counts = df['work_setting'].value_counts()
    pct = (counts / counts.sum() * 100).round(1)
    return pd.DataFrame({'total': counts, 'percentage': pct}).reset_index() #devuelve una tabla con el número absoluto y el porcentaje

# Agrupa por año y cuenta cuántas filas hay en cada uno. 
def offers_by_year(df):
    # Número de ofertas por año
    return (
        df.groupby('work_year')
        .size() #Cuenta filas, no valores
        .reset_index(name='total_offers')
    )

# Calcula el salario medio por nivel de experiencia 
def salary_by_experience(df):
    # Salario medio por nivel de experiencia
    order = ['Junior', 'Mid', 'Senior', 'Executive']
    return (
        df.groupby('experience_group')['salary_in_usd']
        .mean()
        .round(0)
        .reindex(order) # Ordena de Junior a Executive (si no, pandas lo ordenaría por alfabético)
        .reset_index()
        .rename(columns={'salary_in_usd': 'avg_salary'})
    )

# is_remote es true/false. En pandas la media de un booleano es la proporción de true multiplicada por 100, da el porcentaje de trabajos remotos. Por eso se usa mean() y no sum()
def remote_trend_by_year(df):
    # Porcentaje de trabajo remoto por año
    return (
        df.groupby('work_year')['is_remote']
        .mean()
        .mul(100)
        .round(1)
        .reset_index()
        .rename(columns={'is_remote': 'pct_remote'})
    )