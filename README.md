# Telebot Using ChatGPT API

## Tech Stack Used
1. Python==3.7
2. FastAPI 
3. ChatGPT "gpt-3.5-turbo"
4. aiogram



## How to run?
Before we run the project, we need OpenAI account and Telegram account.


### Step 1: Clone the repository
```bash
git clone https://github.com/geddadasuresh84326/NLP-chat-bot-project.git
```

### Step 2- Create a conda environment after opening the repository

```bash
conda create -n telebot python==3.7-y
```

```bash
conda activate telebot
```

### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```

### Step 4 -   Create environment file
create .env file and setup OpenAI API KEY and Telegram custom bot API TOKEN
```bash
 OPENAI_API_KEY = "paste here your OpenAI API KEY"

 TOKEN = "paste here your Telegram bot API TOKEN"

```

### Step 5 - Run the application server
```bash
python main.py
```
