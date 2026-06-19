import pandas as pd

#Cargamos el csv raw y devuelve un dataframe

def load_raw(path):
    return pd.read_csv(path)

#La siguiente función recibe el dataframe sucio y lo devuelve limpio
def clean(df):
    
    #Convierte todos los nombres de columnas a minúsculas y reemplaza espacios por guiones bajos (Python distingue mayúsculas)
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    
    #Dos operaciones encadenadas: eliminamos espacios al inicio y al final de cada valor, y luego se pone la primera letra en mayúscula y el resto en minúscula
    df['work_setting'] = df['work_setting'].str.strip().str.title()
    
    #Quitamos espacios para no tener errores
    df['experience_level'] = df['experience_level'].str.strip()
    
    return df 

# Feature engineering: creamos nuevas columnas a partir de datos que ya tenemos, para que el análisis sea más rico y más fácil de visualizar después

# Crea columnas derivadas para enriquecer el análisis
def engineer_features(df):

    # Categoriza salarios en rangos: Junior (<70k), Mid (70-120k), Senior (>120k)
    bins = [0, 70000, 120000, float('inf')]
    labels = ['Junior', 'Mid', 'Senior']
    df['salary_range'] = pd.cut(df['salary_in_usd'], bins=bins, labels=labels) #salary_range = El salario es un número, lo hemos convertido en una categoría legible, eso permite agrupar y comparar

    # Agrupa niveles de experiencia en etiquetas legibles
    experience_map = {
        'Entry-level': 'Junior',
        'Mid-level': 'Mid',
        'Senior': 'Senior',
        'Executive': 'Executive'
    }
    df['experience_group'] = df['experience_level'].map(experience_map) #experience_group = Tenía los niveles de experiencia en inglés formal, lo he mapeado a etiquetas más limpias

    # Marca si el trabajo es remoto (True) o no (False)
    df['is_remote'] = df['work_setting'] == 'Remote' #is_remote = Convierte texto en un booleano, así es más fácil de filtrar

    #year_group = toma valores numéricos o de fecha, define unos límites y asigna una eqtiqueta a cada valor segun en qué tramo cae.
    df['year_group'] = pd.cut(
        df['work_year'],
        bins=[2019, 2021, 2023, float('inf')],
        labels=['2020-2021', '2022-2023', '2024+']
    )

    return df

#Guardamos el dataframe limpio
def save_processed(df, path):

    df.to_csv(path, index=False)
    print(f'Guardado: {len(df)} filas en {path}')
