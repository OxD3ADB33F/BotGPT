import telebot
import requests
import json

class BotGPT:
    def __init__(self, endpoint, headers, token):
        self._endpoint = endpoint
        self._headers = headers
        self._token = token
        self._bot = telebot.TeleBot(token)
        self._bot.message_handler(commands=['gpt'])(self.reply)

    def start(self):
        self._bot.polling()

    def reply(self, msg):
        d = {
            'model': 'text-davinci-003',
            'prompt': msg.text[5:],
            'max_tokens': 2048,
            'temperature': 0
        }
        
        res = requests.post(self._endpoint, headers = self._headers, json = d)
        response = json.loads(res.text)
        if 'choices' in response:
            text = response['choices'][0]['text']
            print("Usuário: " + msg.from_user.first_name + "\nPergunta: " + msg.text[5:] + "\nResposta: " + text + "\n\n")
        else:
            print("Nenhum texto foi encontrado.")

        self._bot.reply_to(msg, text)

if __name__ == "__main__":
    endpoint = 'https://api.openai.com/v1/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer #ChatGPT TOKEN'
    }
    token = '#BotFather TOKEN'

    bot = BotGPT(endpoint, headers, token)
    bot.start()
