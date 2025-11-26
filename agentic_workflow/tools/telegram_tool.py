from telegram_bot.bot import send_telegram_bot_msg

async def send_telegram_msg(chat_user_id : str, message : str) : 
    """
    send message to telegram user via bot
    
    Args:
        chat_id (str) : Telegram chat ID of the user
        message (str) : Message to be sent to user
        
        
    returns :
        dict : Response from Telegram API
     """
    
    response = await send_telegram_bot_msg(message=message)
    return {"notification_status": response}

    
    