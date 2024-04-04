import config
import telebot

bot = telebot.TeleBot(config.token)

def generate_new_address():
    new_address = "New address generated"
    return new_address

def send_coins(sender_address, recipient_address, amount):
    commission = 0.001
    return f"Sent {amount} KZC from {sender_address} to {recipient_address} with commission {commission} KZC"

@bot.message_handler(commands=['getnewaddresses'])
def get_new_addresses(message):
    address1 = generate_new_address()
    address2 = generate_new_address()
    bot.send_message(message.chat.id, f"New addresses generated:\nAddress 1: {address1}\nAddress 2: {address2}")

@bot.message_handler(commands=['send1'])
def send_coins1(message):
    sender_address = "Your first address"
    recipient_address = "Recipient address 1"
    amount = 0.1
    result = send_coins(sender_address, recipient_address, amount)
    bot.send_message(message.chat.id, result)

@bot.message_handler(commands=['send2'])
def send_coins2(message):
    sender_address = "Your second address"
    recipient_address = "Recipient address 2"
    amount = 0.2
    result = send_coins(sender_address, recipient_address, amount)
    bot.send_message(message.chat.id, result)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.infinity_polling()
