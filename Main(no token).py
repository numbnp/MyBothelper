import telebot
import openai

bot = telebot.telebot("YOUR_TELEGRAM_BOT_TOKEN")
openai.api_key = "YOUR_OPENAI_API_KEY"

@bot.message_handler(content_types=["text"])
def handle_text(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{message.text}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    bot.send_message(message.chat.id, response.choices[0].text)

bot.polling()