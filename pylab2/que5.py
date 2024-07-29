import datetime

def create_weather_data(date, max_temp, min_temp, humidity):
    """Creates a dictionary representing weather data for a day."""
    return {
        "date": date,
        "max_temp": max_temp,
        "min_temp": min_temp,
        "humidity": humidity
    }

def find_highest_and_lowest_temps(weather_data):
    """Finds the highest and lowest temperatures in the given weather data."""
    max_temp = max(data["max_temp"] for data in weather_data)
    min_temp = min(data["min_temp"] for data in weather_data)
    return max_temp, min_temp

def count_hot_days(weather_data):
    """Counts the number of days with temperatures above 30°C."""
    hot_days = 0
    for data in weather_data:
        if data["max_temp"] > 30:
            hot_days += 1
    return hot_days

def calculate_average_humidity(weather_data):
    """Calculates the average humidity over the given period."""
    total_humidity = sum(data["humidity"] for data in weather_data)
    return total_humidity / len(weather_data)

def main():
    # Sample weather data (replace with actual data)
    weather_data = [
        create_weather_data(datetime.date(2024, 8, 1), 28, 22, 70),
        create_weather_data(datetime.date(2024, 8, 2), 32, 25, 65),
        # Add more data here...
    ]

    # Find highest and lowest temperatures
    max_temp, min_temp = find_highest_and_lowest_temps(weather_data)
    print(f"Highest temperature: {max_temp}°C")
    print(f"Lowest temperature: {min_temp}°C")

    # Count hot days
    hot_days = count_hot_days(weather_data)
    print(f"Number of days with temperatures above 30°C: {hot_days}")

    # Calculate average humidity
    average_humidity = calculate_average_humidity(weather_data)
    print(f"Average humidity: {average_humidity:.2f}%")

if __name__ == "__main__":
    main()
