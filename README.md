# PostgreSQL-GPT4o-Langchain-Chatbot

This project demonstrates a chatbot that interacts with a PostgreSQL database using LangChain and OpenAI's GPT-4o. The chatbot can answer complex queries involving multiple tables.

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
    git clone https://github.com/imranajec/PostgreSQL-GPT4o-Langchain-Chatbot.git
    cd PostgreSQL-GPT4o-Langchain-Chatbot
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

**Homepage**

![Screenshot 2024-06-02 at 11 08 50 PM (2)](https://github.com/imranajec/PostgreSQL-Langchain-Chatbot/assets/136712125/4c05f6bd-1e3f-4a09-9262-f01ea32f63d7)

**Database Result**

![Screenshot 2024-06-02 at 11 06 38 PM (2)](https://github.com/imranajec/PostgreSQL-Langchain-Chatbot/assets/136712125/42322fc5-b563-4fbd-be7c-df4a77ed2980)

 **Query Result**
 
![Screenshot 2024-06-02 at 11 07 23 PM (2)](https://github.com/imranajec/PostgreSQL-Langchain-Chatbot/assets/136712125/e16567ef-a853-4753-9173-1d237af4a116)

**Working**

![Screenshot 2024-06-02 at 11 07 10 PM (2)](https://github.com/imranajec/PostgreSQL-Langchain-Chatbot/assets/136712125/077c257b-c7cd-435d-966f-230303c2c437)


