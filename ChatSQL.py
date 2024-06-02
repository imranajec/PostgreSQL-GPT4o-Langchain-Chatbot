# importing the lib
import os
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit

# Load environment variables from the .env file
load_dotenv(r"/Users/imran/Desktop/PROJECTS USING LANGCHAIN AND SQL/dotenv.env")

class ChatWithSql:
    """ChatWithSql class is used for chat and query user questions with the SQL database."""
    def __init__(self, db_user, db_password, db_host, db_name):
        """Constructor method of the ChatWithSql class."""
        os.environ["OPENAI_API_KEY"] = os.getenv("openai_api_key")
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_name = db_name

    def connect_to_db(self):
        """Connect to the SQL database."""
        try:
            db_uri = f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}/{self.db_name}"
            db = SQLDatabase.from_uri(db_uri)
            return db
        except Exception as e:
            print(f"Failed to connect to the database. Error: {e}")
            return None

    def message(self, query):
        """Process the query from the user and return the response."""
        # Initialize the LLM
        llm = ChatOpenAI(model_name="gpt-4o")

        # Connect to the database
        db = self.connect_to_db()
        if not db:
            return "Failed to connect to the database."

        # Initialize the toolkit
        toolkit = SQLDatabaseToolkit(db=db, llm=llm)

        # Create the agent executor
        agent_executor = create_sql_agent(
            llm=llm,
            toolkit=toolkit,
            verbose=True,
            handle_parsing_errors=True  # Add this to handle parsing errors
        )

        response = agent_executor.run(query)
        return response

# Create an instance of the class
chat_with_sql = ChatWithSql("postgres", "", "localhost", "Olympics")
print(chat_with_sql.message("How many tables are there?"))
