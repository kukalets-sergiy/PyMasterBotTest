"""Imports"""
import asyncio

from Handlers.exception_handler import handle_exception
from Handlers.help_functions import create_help_markup
from database.py_master_bot_database import PyMasterBotDatabase2
from decorators import Bot
from Handlers.callback_query_handler import callback_query_handler

# Creating an instance of the Bot class with the token provided from the "data/bot_token.txt" file.
bot = Bot("data/bot_token.txt")
# Initializing the bot database, PyMasterBotDatabase2 is a class used for working with the database.
bot_db = PyMasterBotDatabase2()

bot.run()
async def main():
    # Ініціалізація бази даних
    await bot.initialize_database()
    # Running the bot by calling the run() method of the Bot class.
    # await bot.run()

# Запуск основної функції
asyncio.run(main())

# # Creating an instance of the Bot class with the token provided from the "data/bot_token.txt" file.
# bot = Bot("data/bot_token.txt")
# # Initializing the bot database, PyMasterBotDatabase2 is a class used for working with the database.
# bot_db = PyMasterBotDatabase2()
# bot.initialize_database()
# # Running the bot by calling the run() method of the Bot class. This method initializes and starts the bot.
# bot.run()
# Getting the bot instance by calling the get_bot() method. This allows accessing the bot after it's been launched.
telebot_instance = bot.get_bot()

bot.inline_keyboard.add_button("🔘 Theory tests", callback_data="/testing")
bot.inline_keyboard.add_button("🔵 Coding tests ", callback_data="/coding")
bot.inline_keyboard.add_button("📚 Lessons", callback_data="/lesson")
bot.inline_keyboard.add_button("Check my code", callback_data="/check_code")
bot.inline_keyboard.add_button("Documentation", callback_data="/documentation")
bot.inline_keyboard.add_button("HELP", callback_data="/help")
bot.inline_keyboard.add_button("🏠 My account", callback_data="/account")
bot.inline_keyboard.add_button("🍓 Comments", callback_data="/comments")
bot.inline_keyboard.add_button("👑 Premium", callback_data="/premium")

bot.reply_keyboard = create_help_markup()

telebot_instance.message_handler(commands=["start"])(bot.start_handler)
telebot_instance.message_handler(commands=["add_lesson"])(bot.add_lesson_handler)
telebot_instance.message_handler(commands=["add_ai_lesson_tasks"])(bot.add_ai_lesson_handler)
telebot_instance.message_handler(commands=["add_admin"])(bot.add_admin_handler)
telebot_instance.message_handler(commands=["add_test_task"])(bot.add_test_task_handler)
telebot_instance.message_handler(commands=["add_ai_test_tasks"])(bot.add_ai_test_tasks_handler)
telebot_instance.message_handler(commands=["add_code_task"])(bot.add_code_task_handler)
telebot_instance.message_handler(commands=["add_ai_code_tasks"])(bot.add_ai_code_tasks_handler)
telebot_instance.message_handler(commands=["add_easy_test_task", "add_middle_test_task", "add_hard_test_task"])(
    bot.add_test_task_by_level_handler
)
telebot_instance.message_handler(commands=["add_easy_code_task", "add_middle_code_task", "add_hard_code_task"])(
    bot.add_code_task_by_level_handler
)
telebot_instance.message_handler(commands=["change_test_task"])(bot.change_test_task_handler)
telebot_instance.message_handler(commands=["change_code_task"])(bot.change_code_task_handler)
telebot_instance.message_handler(commands=["add_level"])(bot.add_level_handler)
telebot_instance.message_handler(content_types=["document"])(bot.csv_tables_names_lessons)
telebot_instance.callback_query_handler(func=lambda call: True)(bot.handle_callback_query)
telebot_instance.message_handler(func=lambda message: True)(bot.display_current_mode)
telebot_instance.callback_query_handler(func=lambda call: True)(callback_query_handler)


# start polling for new messages
if __name__ == "__main__":

    try:
        telebot_instance.polling(none_stop=True, timeout=60)

    except Exception as e:
        handle_exception(e, telebot_instance)


# import telebot
# import asyncio
#
# from Handlers.exception_handler import handle_exception
# from Handlers.help_functions import create_help_markup
# from database.py_master_bot_database import PyMasterBotDatabase2
# from decorators import Bot
# from Handlers.callback_query_handler import callback_query_handler
#
# # Creating an instance of the Bot class with the token provided from the "data/bot_token.txt" file.
# bot = Bot("data/bot_token.txt")
# # Initializing the bot database, PyMasterBotDatabase2 is a class used for working with the database.
# bot_db = PyMasterBotDatabase2()
#
# async def main():
#     # Ініціалізація бази даних
#     await bot.initialize_database()
#     # Отримання екземпляру бота
#     telebot_instance = bot.get_bot()
#
#     # Реєстрація обробників повідомлень і зворотних викликів
#     telebot_instance.message_handler(commands=["start"])(bot.start_handler)
#     telebot_instance.message_handler(commands=["add_lesson"])(bot.add_lesson_handler)
#     telebot_instance.message_handler(commands=["add_ai_lesson_tasks"])(bot.add_ai_lesson_handler)
#     # Додайте інші обробники повідомлень тут
#
#     telebot_instance.callback_query_handler(func=lambda call: True)(callback_query_handler)
#
#     # Створення кнопок інлайн клавіатури
#     inline_keyboard = telebot.types.InlineKeyboardMarkup()
#     inline_keyboard.add(telebot.types.InlineKeyboardButton("🔘 Theory tests", callback_data="/testing"))
#     # Додайте інші кнопки інлайн клавіатури тут
#
#     # Встановлення стартової інлайн клавіатури
#     bot.inline_keyboard = inline_keyboard
#
#     # Початок опитування нових повідомлень
#     telebot_instance.polling(none_stop=True, timeout=60)
#
#
# # Запуск основної функції
# if __name__ == "__main__":
#     asyncio.run(main())
