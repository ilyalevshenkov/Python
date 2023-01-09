#TOKEN Vasily3: 5900363631:AAEz3j2EuZBS_ehZgfQXJEEoiYqBUgiiu4E
# 1) Напишите Бота, удаляющего из текста все слова, содержащие "абв". (Ввод от пользователя)
# 2) Создайте Бота для игры с конфетами человек против бота.

#Для игры с конфетами наберите: /game


from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler
import Functions

app = ApplicationBuilder().token("5900363631:AAEz3j2EuZBS_ehZgfQXJEEoiYqBUgiiu4E").build()

app.add_handler(ConversationHandler(entry_points= [CommandHandler("game", Functions.game)],
states={Functions.my_turn:[MessageHandler(filters.TEXT, Functions.gamer_turn)], 
Functions.bot:[MessageHandler(filters.TEXT, Functions.bot_turn)]},
fallbacks=[CommandHandler("cancel", Functions.cancel)]))

app.add_handler(CommandHandler("hello", Functions.hello))
app.add_handler(MessageHandler(filters.TEXT, Functions.del_word))


app.run_polling()