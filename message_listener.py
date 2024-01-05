from pyrogram import Client, filters
from pyrogram.types import Message
from googletrans import Translator

# جایگزین کردن این مقادیر با مقادیر واقعی
source_channel = 'SOURCE_CHANNEL_ID'  # ID کانال مبدا
destination_channel = 'DESTINATION_CHANNEL_ID'  # ID کانال مقصد
custom_text = 'متن دلخواه شما'  # متن سفارشی که می‌خواهید در پایین هر پست قرار دهید
custom_link = 'http://link-to-your-content'  # لینک دلخواه شما

translator = Translator()

@Client.on_message(filters.channel & filters.chat(source_channel))
def from_channel(client, message):
    # ترجمه متن پیام
    if message.text:
        translated_text = translator.translate(message.text, dest='fa').text
        text_to_send = f"**متن انگلیسی:**\n{message.text}\n\n**متن فارسی:**\n{translated_text}\n\n{custom_text}\n{custom_link}"
    else:
        # اگر پیام متن نداشته باشد، مثلا عکس یا ویدئو باشد، فقط یک پیغام ساده ارسال می‌کنیم
        text_to_send = f"{custom_text}\n{custom_link}"

    # ارسال پیام به کانال مقصد
    client.send_message(destination_channel, text_to_send, disable_web_page_preview=True)
