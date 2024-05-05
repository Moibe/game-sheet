import datetime

hour_value = "18:45"
current_time = "20:23"

def is_in_time_range(hour_value):
    # Convert hour_value and current_time to datetime objects for comparison
    hour_value_datetime = datetime.datetime.strptime(hour_value, "%H:%M")
    print("Ésto es hour_value_datetime: ", hour_value_datetime)

    now = datetime.datetime.now()
    print("Ésto es now: ", now)

    #current_time_datetime = datetime.datetime.strptime(current_time, "%H:%M")

    # Calculate the start and end times of the range
    start_time = now - datetime.timedelta(hours=2)
    end_time = now + datetime.timedelta(hours=1)

    print(start_time)
    print(end_time)

# #     # Check if hour_value_datetime falls within the range
    is_in_range = start_time <= hour_value_datetime <= end_time

    print(is_in_range)

    return is_in_range

# # # Example usage
# # hour_value = "19:30"  # Example value
# # current_time = "20:15"  # Example value

# # is_within_range = is_in_time_range(hour_value, current_time)

# # if is_within_range:
# #     print(f"Hour value '{hour_value}' is within the time range centered on {current_time}")
# # else:
# #     print(f"Hour value '{hour_value}' is outside the time range centered on {current_time}")

if __name__ == "__main__":
    is_in_time_range(hour_value)