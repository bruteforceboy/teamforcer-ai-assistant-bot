from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from telegram import Bot
from telegram import BotCommand
from handlers.message_handlers import echo, update_command, update_with_file
from handlers.command_handlers import start, help_command
from config import TELEGRAM_BOT_TOKEN
import asyncio

def setup_telegram_bot():
    """
    Setup and initialize the Telegram bot with the specified token and handlers.

    Returns:
        bot: The initialized Telegram bot application.
    """
    # Create a new application instance for the bot
    bot = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Register command handlers
    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(CommandHandler("help", help_command))
    bot.add_handler(CommandHandler("upd", update_command))

    # Register message handlers
    bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    bot.add_handler(MessageHandler(filters.Document.ALL, update_with_file))

    # Set the bot commands
    asyncio.run(set_commands(bot.bot))

    return bot


async def set_commands(bot: Bot):
    """
    Sets the commands list of the bot and to show them when typing a slash "/"

    Args:
        bot: an object of type telegram.bot
    """
    commands = [
        BotCommand("start", "Запустить бота"),
        BotCommand("help", "Показать информацию о помощи"),
        BotCommand("upd", "Обновить базу знаний бота \"/upd <текст>\""),
    ]
    await bot.set_my_commands(commands)