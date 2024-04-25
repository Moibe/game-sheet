import time
import pandas as pd
import json

def readExcel():

    print("Iniciando proceso de lectura de excel...")
    #Con sheet_name=None extrae las dos, ver como acceder a ellas para hacerles a ambas el fix de fechas. 
    df = pd.read_excel('test.xlsx')
    
    print(df)
    print("Información extraída.")
    
    print("Json de Resultados: ")

    json_str = df.to_json(orient='records')  # Orient='records' for JSON array

    json_array = json.loads(json_str)
    print("Impresión de Registro Individual")
    print(json_array[5])
    time.sleep(5)

    return json_array

    # años = range(1956, 1957)
   
    # for año in años:
    #     print("Estoy en el año: ", año)
    #     #Filtro las filas que pertenecen a ese año.           
    #     df_anio = df[df['FECHA'].dt.year == año]
    #     print("La longitud del dataframe es: ", len(df_anio))
        
    #     if (len(df_anio)) < 1: 
    #         print("No hay datos para trabajar con, extender el parámetro nrows en read_excel.")
    #         time.sleep(5)
    #     else: 
    #         print("Obtuve el dataset del año: ", año)
    #         #Arreglo de formato de fecha antes de cargar en el archivo de excel.
    #         df_anio['FECHA'] = df_anio['FECHA'].dt.strftime('%Y/%m/%d')
    #         print("Se arregló fecha correctamente...")
    #         df_anio.to_excel(f"excels/a{año}.xlsx", index=False)

    # return "Tarea completada"

if __name__ == "__main__":
    readExcel()