# Telegram Chatbot - COVID-19 Tracker

This project consists of a Telegram chatbot that provides COVID-19 statistics, specifically for India. The chatbot interacts with users, fetches the latest data from the COVID-19 API, and sends updates to the users.

## Files

### bot.py

This file contains the implementation of the `telegram_chatbot` class. It establishes a connection with the Telegram Bot API, retrieves updates from the chat, and sends messages to users. It reads the bot token from the `config.cfg` file.

### corona.py

This file defines the `country_details` class and the `corona_fetch` class. The `country_details` class encapsulates the COVID-19 statistics for a specific country, in this case, India. The `corona_fetch` class fetches the latest COVID-19 data from the API and extracts the information for India.

### server.py

This file is the main entry point of the application. It imports the `telegram_chatbot` and `corona_fetch` classes. It creates instances of these classes and handles the communication between the chatbot and the COVID-19 API. It continuously checks for updates from users, retrieves the messages, fetches the COVID-19 data, and sends the statistics as a reply.

## Usage

1. Obtain a bot token from the Telegram Bot API.
2. Create a `config.cfg` file and add the bot token in the following format:
```
[creds]
token=YOUR_BOT_TOKEN
```
3. Ensure that the required dependencies (such as `requests` and `beautifulsoup4`) are installed.
4. Run the `server.py` file to start the chatbot server.
5. Interact with the chatbot through the Telegram interface.

## Note

This project utilizes the COVID-19 API to fetch real-time data. Make sure the API is accessible and running to obtain accurate statistics. Additionally, the chatbot is currently configured to provide COVID-19 statistics for India. If you want to track data for a different country, modify the code accordingly.

Feel free to customize and extend this project as per your requirements.
