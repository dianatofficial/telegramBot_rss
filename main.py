from pyrogram import Client, filters

# فرض می‌کنیم که فایل پلاگین شما message_listener.py نام دارد و در پوشه‌ای به نام plugins قرار دارد
plugins = dict(root="plugins")

app = Client(
    "my_account",  # نام نشانگر برای نمونه کلاینت شما
    api_id='22853762',  # جایگزین با api_id واقعی شما
    api_hash='847fb74edc5eb0e8c901cea8830eff80',  # جایگزین با api_hash واقعی شما
    plugins=plugins  # پوشه پلاگین‌ها
)

app.run()
