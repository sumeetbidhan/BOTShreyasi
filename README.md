
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
       # Your implementation here
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