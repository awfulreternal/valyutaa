from telegram import Update

from telegram.ext import ContextTypes

from database import User

import random



async def register(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    user_id = update.effective_user.id

    username = update.effective_user.username

    user, created = User.get_or_create(user_id=user_id, defaults={'username': username})

    if created:

        await update.message.reply_text("Вы успешно зарегистрировались! Ваш начальный баланс: 1000.")

    else:

        await update.message.reply_text("Вы уже зарегистрированы!")



async def show_balance(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    user = User.get(User.user_id == update.effective_user.id)

    await update.message.reply_text(f"Ваш текущий баланс: {user.balance}")



async def show_leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    top_users = User.select().order_by(User.balance.desc()).limit(10)

    leaderboard = "\n".join([f"{user.username or 'Unknown'}: {user.balance}" for user in top_users])

    await update.message.reply_text(f"Топ игроков:\n{leaderboard}")



async def trade(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    user = User.get(User.user_id == update.effective_user.id)

    amount = random.uniform(-100, 100)  # Симулируем торговлю

    user.balance += amount

    user.save()

    result = "прибыль" if amount > 0 else "убыток"

    await update.message.reply_text(f"Вы получили {result} в размере {abs(amount)}. Ваш новый баланс: {user.balance}")

