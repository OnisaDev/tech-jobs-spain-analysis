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

#Guardamos el dataframe limpio
def save_processed(df, path):

    df.to_csv(path, index=False)
    print(f'Guardado: {len(df)} filas en {path}')
