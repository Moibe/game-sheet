import datetime

hour_value = "18:45"

def is_in_time_range(hour_value):

    #La función regresará True o False dependiendo si cae o no en el rango.

    # Convert hour_value and current_time to datetime objects for comparison
    #Combinación para que la hora convertida sea del día de hoy y no de 1900.
    hour_value_datetime = datetime.datetime.combine(datetime.date.today(), datetime.datetime.strptime(hour_value, "%H:%M").time())

    #El tiempo de éste momento.
    now = datetime.datetime.now()

    # Calculate the start and end times of the range
    start_time = now - datetime.timedelta(hours=2)
    end_time = now + datetime.timedelta(hours=1)

    print("Tiempo inicial: ", start_time)
    print("Tiempo Final: ", end_time)

    #Check if hour_value_datetime falls within the range
    is_in_range = start_time <= hour_value_datetime <= end_time

    print(is_in_range)

    return is_in_range

if __name__ == "__main__":
    is_in_time_range(hour_value)