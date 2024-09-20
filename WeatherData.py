def aggregateWeatherData(records):
    cityData = {}
    
    # Go through each record
    for record in records:
        city = record['city']
        
        # If city is not in cityData, create an empty dictionary for it
        if city not in cityData:
            cityData[city] = {'totalTemp': 0, 'tempCount': 0, 'totalHumidity': 0, 'humidityCount': 0}
        
        # Add temperature to the city's data if it exists
        if 'temperature' in record:
            cityData[city]['totalTemp'] += record['temperature']
            cityData[city]['tempCount'] += 1
        
        # Add humidity to the city's data if it exists
        if 'humidity' in record:
            cityData[city]['totalHumidity'] += record['humidity']
            cityData[city]['humidityCount'] += 1
    
    # Initialize an empty result dictionary
    result = {}
    
    # Loop through each city in cityData
    for city in cityData:
        # Get the total temperature and count for the city
        totalTemp = cityData[city]['totalTemp']
        tempCount = cityData[city]['tempCount']
        
        # Get the total humidity and count for the city
        totalHumidity = cityData[city]['totalHumidity']
        humidityCount = cityData[city]['humidityCount']
        
        # Calculate the average temperature if there's data, otherwise None
        if tempCount > 0:
            avgTemp = totalTemp / tempCount
        else:
            avgTemp = None
        
        # Calculate the average humidity if there's data, otherwise None
        if humidityCount > 0:
            avgHumidity = totalHumidity / humidityCount
        else:
            avgHumidity = None
        
        # Store the results for the city
        result[city] = {'averageTemperature': avgTemp, 'averageHumidity': avgHumidity}
    
    return result
