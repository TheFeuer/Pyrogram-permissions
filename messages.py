
async def send_access_message(app, chat_id, access):
    """Отправка сообщения о доступе"""
    if access == "allowed":
        message = "Доброе утро!☀️Чат открыт, ждём ваши вопросы🤗"
        await app.send_message(chat_id=chat_id, text=message)
    elif access == "restricted":
        message = "Спасибо за ваши вопросы! Чат закрыт, до скорой встречи👋 \n " \
                  "(Если при закрытии чата остались неотвеченные вопросы - " \
                  "не переживайте, кураторы на них ответят)"
        await app.send_message(chat_id=chat_id, text=message)
