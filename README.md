### SkySync: A Weather Web App

**SkySync** is a sleek and intuitive weather web application designed to keep you informed about the weather conditions across cities around the world. With SkySync, you can effortlessly track temperature, humidity, wind speed, and visibility for any city you search for. Simply enter the city's name in the input box, and the webpage will display the related weather information. You can also view weather data for multiple cities simultaneously, making it easy to compare conditions across different locations.

#### Key Features:
- Real-time weather tracking for cities worldwide.
- Detailed information on temperature, humidity, wind speed, and visibility.
- User-friendly search functionality for quick city lookups.
- Ability to display weather data for multiple cities at once.

#### Tech Stack:
- **HTML**: For structuring the web pages.
- **CSS**: For styling and ensuring a visually appealing interface.
- **JavaScript**: For dynamic interactions and seamless user experience.
- **Bootstrap**: For responsive design and layout.
- **Django**: The powerful backend framework that drives the application.
- **SQLite**: For efficient and lightweight database management.
- **Python**: The core programming language used in conjunction with Django.
- **Open Weather Map API**: For fetching up-to-date weather data.

SkySync combines functionality with elegance, providing a reliable and beautiful tool for anyone looking to stay updated on weather conditions around the globe.

### Environment Variables Setup

Before running this project, ensure you set up the necessary environment variables in your `.env` file. The following variables are required:

- **`API_KEY`**: This variable should contain your API key for accessing the OpenWeatherMap API.


#### Environment Setup Steps:

1. **Create a Virtual Environment**: Start by creating a virtual environment using `python -m venv weather-env`.

2. **Activate the Virtual Environment**: Navigate to the `Scripts` folder within the environment directory and run the `activate` script to activate the environment. This step ensures that your project uses the isolated environment with its dependencies.

3. **Install Django and Dependencies**: Within the activated environment, install Django and any other required packages. You can use `pip` to install packages like `django` and `requests` for accessing the OpenWeatherMap API.

4. **Set Environment Variables**: In your project directory, create a file named `.env` if it doesn't already exist. Add the required environment variables (`API_KEY` and `ANOTHER_API_KEY`) along with their respective values.

5. **Accessing the Environment**: With the virtual environment activated and the environment variables set, your project will be able to access the API keys securely.

## API Reference

#### Get Current Weather Data

```http
  GET /api/current
```

| Parameter | Type     | Description                                    |
| :-------- | :------- | :--------------------------------------------- |
| `appid`   | `string` | **Required**. Your OpenWeatherMap API key      |
| `city`    | `string` | **Required**. Name of the city for weather data|

#### Description

This endpoint retrieves current weather data for a specified city using the OpenWeatherMap API. It returns information such as temperature, humidity, wind speed, and visibility.

#### Example Usage

```http
GET /api/current?appid=YOUR_API_KEY&city=New%20York
```

#### Response

```json
{
  "coord": {"lon": -73.9352, "lat": 40.7306},
  "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01n"}],
  "base": "stations",
  "main": {"temp": 25.45, "feels_like": 20.12, "humidity": 50},
  "visibility": 10000,
  "wind": {"speed": 3.5, "deg": 200},
  "clouds": {"all": 0},
  "dt": 1718506800,
  "sys": {"type": 1, "id": 4686, "country": "US", "sunrise": 1718108572, "sunset": 1718161078},
  "timezone": -18000,
  "id": 5128581,
  "name": "New York",
  "cod": 200
}
```

This response contains detailed information about the current weather conditions in the specified city.

## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

