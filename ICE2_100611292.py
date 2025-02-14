# Author: Shibin Shaji
# Date: January 30, 2025
# Description: This program does boundary analysis using inputs from the user.
import statistics

# Valid temperature range
MIN_TEMP = -50
MAX_TEMP = 150

def validate_temperature(value):
    if value == "":
        return None
    try:
        temp = float(value)
        if MIN_TEMP <= temp <= MAX_TEMP:
            return temp
        else:
            return f"Out of range value has been detected: {value}"
    except ValueError:
        return f"Invalid input detected: {value}"

def process_temperatures(temp_list):
    min_temp = min(temp_list)
    max_temp = max(temp_list)
    avg_temp = statistics.mean(temp_list)

    min_temp = int(min_temp) if min_temp.is_integer() else min_temp
    max_temp = int(max_temp) if max_temp.is_integer() else max_temp
    avg_temp = int(round(avg_temp))

    return f"Min: {min_temp}°C, Max: {max_temp}°C, Avg: {avg_temp}°C"

def main():
    print("Please enter 3 temperature readings:")
    temperatures = []
    errors = []

    for i in range(3):
        value = input(f"Enter temperature {i + 1}: ")
        result = validate_temperature(value)

        if isinstance(result, str):
            errors.append(result)
        else:
            temperatures.append(result)

    if errors:
        for error in errors:  #
            print(error)

    valid_temps = [t for t in temperatures if t is not None]  #
    if valid_temps:
        print(process_temperatures(valid_temps))
    else:
        print("No input provided, Please try again.")  #


if __name__ == "__main__":
    main()



