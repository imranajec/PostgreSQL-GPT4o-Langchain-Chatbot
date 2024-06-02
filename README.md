# LangChain-PostgreSQL-Chatbot

This project demonstrates a chatbot that interacts with a PostgreSQL database using LangChain and OpenAI's GPT-4. The chatbot can answer complex queries involving multiple tables.

## Features

- Interacts with a PostgreSQL database
- Handles complex SQL queries
- Provides a user-friendly web interface

## Setup

### Prerequisites

- Python 3.11
- PostgreSQL

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/imranajec/LangChain-PostgreSQL-Chatbot.git
    cd LangChain-PostgreSQL-Chatbot
    ```

2. **Set up the virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the environment variables:**

    Create a `.env` file and add your OpenAI API key:

    ```env
    openai_api_key=your_openai_api_key
    ```

5. **Run the application:**

    ```bash
    python app.py
    ```

## Usage

- Open your web browser and go to `http://127.0.0.1:5000`.
- Enter your SQL query in the input box and submit.
- The result will be displayed on the page.

## Technologies Used

- Flask
- LangChain
- OpenAI
- PostgreSQL

## Screenshots

![Homepage](path/to/homepage-screenshot.png)
![Query Result](path/to/query-result-screenshot.png)

