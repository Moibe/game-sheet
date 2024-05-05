import time
import pandas as pd
import json
import datetime

def readExcel():

    print("Iniciando proceso de lectura de excel...")
    df = pd.read_excel('test.xlsx')
    
    print(df)
    print("Información extraída.")

    # Get the value at row 3 and column 2
    hour_value = df.loc[4, 'Hour']

    # Get the current date and time
    now = datetime.datetime.now()

    # Print the current time
    current_time = now.strftime("%H:%M")
    print(f"Current time: {current_time}")

    print("El tipo de currenttime es: ", type(current_time))
    print("El tipo de hourvalue es: ", type(hour_value))

    # Print the value
    print(hour_value)



    
    # print("Json de Resultados: ")

    # json_str = df.to_json(orient='records')  # Orient='records' for JSON array

    # json_array = json.loads(json_str)
    # print("Impresión de Registro Individual")
    # print(json_array[5])
    # time.sleep(5)

    # return json_array

if __name__ == "__main__":
    readExcel()