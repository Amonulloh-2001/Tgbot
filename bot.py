from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv

# Бор кардани токен аз .env
load_dotenv()
BOT_TOKEN = os.getenv('TOKEN') or "7903594220:AAFmX5U35CahQ7TqCn04B_I0I46SB8jK4DE"

# ID чати Telegram-и шумо
ADMIN_CHAT_ID = 5607622404

# Функсияи "start"  
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["✨ Как сделать заказ", "🚚 Доставка"],
        ["↔️ Обмен и Возврат", "💸 Оплата"],
        ["📲 ВК Сообщество", "📲 Telegram"],
        ["📞 Связь со мной", "📝 Отзывы"],
        ["⬅️ Назад"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Добро пожаловать! Выберите нужное меню:", reply_markup=reply_markup
    )

# Функсия барои "Как сделать заказ"
async def order_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """✨ Как сделать заказ?

1. Присылайте нам фото товара, который хотите заказать, и желаемое количество.
2. Мы проконсультируем вас по наличию изделий.
3. Составим чек на оплату.
4. После оплаты сразу отправим заказ (или отложим до вашего приезда к нам в магазин).
5. Наши данные для оплаты:
   ✅ Сбербанк: +7(925)-111-50-97
   ✅ Имя: Амонуллох Балачонович М
   ✅ Тинькофф
6. После оплаты пришлите фото чека.

📸 После отправки фото чека заказ будет подтвержден, и вы получите уведомление."""
    await update.message.reply_text(text)

# Функсия барои "Доставка"
async def delivery_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """🚚 Доставка: по ВСЕЙ России и СНГ.
Отправить заказ можем любой транспортной компанией:
СДЭК, ПЭК, Деловые линии, Почта России, Байкал-сервис, Виктория и т.д.

Сроки и тарифы доставки до вашего города вы можете узнать, позвонив на горячую линию ТК или на сайте ТК!

🚌 Отправляем автобусами!
Для этого вы должны предоставить данные водителя, время отъезда и номер стоянки!
От нас грузчик 100-200₽ от веса посылки и до ТК 100-300₽ от веса!"""
    await update.message.reply_text(text)

# Функсия барои "Оплата"
async def payment_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """💸 Оплата
Оплату мы принимаем на карту тиныкоф .
Онлайн расчёт. Для оплаты менеджер выставляет счёт и отправляет вам ссылку на оплату."""
    await update.message.reply_text(text)

# Функсия барои "Обмен и Возврат"
async def exchange_return_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """↔️ Обмен
В случае фабричного брака в течение 7 дней после выкупа.

🛑 Возврат
К сожалению, возврата нет."""
    await update.message.reply_text(text)

# Функсия барои "ВК Сообщество"
async def vk_community(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "📲 Наше ВК Сообщество: https://vk.com/fashionstyl01\nПодписывайтесь, чтобы быть в курсе новых товаров!"
    await update.message.reply_text(text)

# Функсия барои "Telegram"
async def telegram_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "📲 Наш Telegram канал: https://t.me/italiakorea01\nПодписывайтесь, чтобы не пропустить новинки!"
    await update.message.reply_text(text)

# Функсия барои "Связь со мной"
async def contact_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """📞 Для связи с нами, пожалуйста, используйте следующие контактные данные:
    
    WhatsApp: +7 (925) 111-50-97
    Telegram: @Sadovodru6112
    ВК: https://vk.com/i606703932
    """
    await update.message.reply_text(text)

# Функсия барои "Отзывы"
async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "📝 Ваши отзывы очень важны для нас! Пожалуйста, оставьте ваш отзыв и поделитесь опытом."
    await update.message.reply_text(text)

# Функсия барои "Назад"
async def back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["✨ Как сделать заказ", "🚚 Доставка"],
        ["↔️ Обмен и Возврат", "💸 Оплата"],
        ["📲 ВК Сообщество", "📲 Telegram"],
        ["📞 Связь со мной", "📝 Отзывы"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Вы вернулись в основное меню. Выберите нужное действие:", reply_markup=reply_markup
    )

# Функсия барои "Сделать заказ"
async def place_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Маълумоти фиристодаи корбар
    user_data = update.message.text if update.message.text else "Нет текста"
    user_name = update.message.from_user.username or update.message.from_user.first_name
    
    # Хабар ба корбар
    await update.message.reply_text(
        f"Мы приняли ваш заказ, {user_name}! В ближайшее время с вами свяжется наш менеджер."
    )

    # Хабар ба Telegram (чати канала ё ID чат)
    order_info = f"Новый заказ от {user_name} (@{update.message.from_user.username if update.message.from_user.username else 'No username'}):\n{user_data}"
    
    # Фиристодани хабари фармоиш ба чати Telegram-и шумо
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=order_info)

# Танзими боти Telegram
def main():
    app = Application.builder().token(BOT_TOKEN).build()
 
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^✨ Как сделать заказ$"), order_info))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^🚚 Доставка$"), delivery_info))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^💸 Оплата$"), payment_info))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^↔️ Обмен и Возврат$"), exchange_return_info))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^📲 ВК Сообщество$"), vk_community))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^📲 Telegram$"), telegram_info))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^📞 Связь со мной$"), contact_info))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^📝 Отзывы$"), feedback))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^⬅️ Назад$"), back))
    # Функсияи place_order танҳо барои паёмҳои дигар кор мекунад
    app.add_handler(MessageHandler(filters.TEXT & ~filters.Regex("|".join([
        "^✨ Как сделать заказ$", "^🚚 Доставка$", "^💸 Оплата$", "^↔️ Обмен и Возврат$",
        "^📲 ВК Сообщество$", "^📲 Telegram$", "^📞 Связь со мной$", "^📝 Отзывы$", "^⬅️ Назад$"
    ])), place_order))

    print("Бот успешно запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
