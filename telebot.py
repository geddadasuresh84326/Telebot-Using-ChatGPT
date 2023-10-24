import os 
from dotenv import load_dotenv
from aiogram import Bot,Dispatcher,executor,types
import openai
import sys


class Reference:
    """A class to store the previous response from ChatGPT API"""
    def __init__(self) -> None:
        self.response = ""

# load environment variables
load_dotenv()

# set up OpenAI api key
openai.api_key = os.getenv("OpenAI_API_KEY")

# Create reference class object to store the previous response
reference = Reference()

# Bot token
TOKEN = os.getenv("TOKEN")

# model we are using
MODEL_NAME = "gpt-3.5-turbo"

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#2
def clear_past():
    """
    This function will clear the previous conversation and context.
    """
    reference.response = ""

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """
    This handler to welcome the user and clear past conversation and context
    """
    clear_past()
    await message.reply("Hello!\n I am Telebot \n How can I assist you?")

@dp.message_handler(commands=['clear'])
async def clear (message:types.Message):
    """
    A handler to clear the previous conversation and context.
    """
    clear_past()
    await message.reply("I've cleared the past conversation and context.")
    
