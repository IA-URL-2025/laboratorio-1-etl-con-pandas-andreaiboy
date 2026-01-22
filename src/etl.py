import pandas as pd

def run_etl():
    
    df = pd.read_csv('data/citas_clinica.csv')
    #Normalización de texto (paciente y especialidad)
    df["paciente"] = df["paciente"].str.title()
    df["especialidad"] = df["especialidad"].str.upper()

    #Fechas (conversión y filtro de invalidas)
    df["fecha_cita"] = pd.to_datetime(df["fecha_cita"], errors = "coerce")
    df = df[df["fecha_cita"].notna()].copy()

    #Reglas de negocio
    df = df[df["estado"] == "CONFIRMADA"]
    df = df[df["costo"]> 0]

    #Valores nulos
    df["telefono"] = df["telefono"].fillna("NO REGISTRA")
    df.to_csv('data/output.csv', index = False)
    pass


if __name__ == "__main__":
    run_etl()
