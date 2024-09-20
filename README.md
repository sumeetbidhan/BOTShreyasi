
# Python Assignment for BOT Shreyasith

## Overview
This project includes a Python function to aggregate weather data from records, a Python function for prime factorization, and a SQL query to update product prices in a database.

## Prerequisites

Before you begin, ensure you have the following installed:

### 1. **Python**
   - **Version**: 3.6 or higher
   - **Installation**: Download and install from the [official Python website](https://www.python.org/downloads/).

### 2. **Python IDE or Code Editor**
   - You can use any of the following:
     - **Visual Studio Code**: [Download here](https://code.visualstudio.com/)
       - Recommended Extensions:
         - Python extension by Microsoft
     - **PyCharm**: [Download here](https://www.jetbrains.com/pycharm/)
     - **Jupyter Notebook**: Optional for testing Python code interactively.

### 3. **MySQL Database**
   - **Server**: MySQL server should be installed and running. Download from [MySQL Community Server](https://dev.mysql.com/downloads/mysql/).
   - **Client**: Use MySQL Workbench or command line to interact with the database.

### 4. **SQL Client (Optional)**
   - **MySQL Workbench**: A GUI to manage MySQL databases. [Download here](https://www.mysql.com/products/workbench/).

### 5. **Database Setup**
   - Create a database (e.g., `WeatherData`).
   - Create a table for `products` with columns:
     - `id` (INT, PRIMARY KEY)
     - `name` (VARCHAR)
     - `price` (DECIMAL)

### 6. **Dependencies**
   - You may need to install additional Python libraries. Use the following command in your terminal:
     ```bash
     pip install mysql-connector-python
     ```

## Running the Code

### 1. Aggregate Weather Data Function
- **Create a Python file** (e.g., `WeatherData.py`).
- **Copy and paste the following function** into your Python file:
   ```python
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

   ```

### 2. Prime Factorization Function
- **Add the following function** to your Python file for prime factorization:
   ```python
   def primeFactors(n):
       factors = []
       for i in range(2, n + 1):
           count = 0
           while n % i == 0:
               n //= i
               count += 1
           if count > 0:
               factors.append((i, count))
       return factors
   ```

### 3. SQL Query
1. **Open your SQL client** (MySQL Workbench or command line).
2. **Run the following SQL commands** to update product prices:
   ```sql
   UPDATE products
   SET price = price * 1.10;

   SELECT name, price FROM products;
   ```

## Additional Information
- Make sure the MySQL server is running before executing the SQL queries.
- Test the Python functions with sample data to ensure they work as expected.
- Ensure that your database connection parameters (if using Python to connect to MySQL) are correct.

## Contact
For any questions or issues, please reach out to [sumeetbidhanwork@gmail.com].
Also, can see the reporistory at [Sumeet Bidhan](https://github.com/sumeetbidhan/BOTShreyasi)
---

Feel free to adjust any part of the README as needed!