CommandHandler("unplug", admin_unplug),
CommandHandler("plugin", admin_plugin),
CommandHandler("kill", admin_kill),
CommandHandler("nap", admin_nap),
CommandHandler("status", admin_status),
from ..admin.admin_service import AdminService

admin = AdminService(THE_CREATOR, THE_CREATOR)
admin.status = "running"


async def admin_plugin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fn = "_admin_plugin:"
    chat_id: int = try_get(update, "message", "chat", "id")
    user_id: int = try_get(update, "message", "from_user", "id")
    if user_id != THE_CREATOR:
        return
    admin: AdminService = AdminService(user_id, chat_id)
    admin.stop_service()


async def admin_unplug(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fn = "admin_unplug:"
    chat_id: int = try_get(update, "message", "chat", "id")
    user_id: int = try_get(update, "message", "from_user", "id")
    admin: AdminService = AdminService(user_id, chat_id)
    admin.start_service()


async def admin_kill(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fn = "admin_kill:"
    message: Message = try_get(update, "message")
    chat: Chat = try_get(message, "chat")
    chat_id: int = try_get(chat, "id")
    user: User = try_get(message, "from_user")
    user_id: int = try_get(user, "id")
    if user_id != THE_CREATOR:
        return
    admin: AdminService = AdminService(user_id, chat_id)
    admin.kill_service()


async def admin_nap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fn = "admin_nap:"
    message: Message = try_get(update, "message")
    chat: Chat = try_get(message, "chat")
    chat_id: int = try_get(chat, "id")
    user: User = try_get(message, "from_user")
    user_id: int = try_get(user, "id")
    if user_id != THE_CREATOR:
        return
    admin: AdminService = AdminService(user_id, chat_id)
    admin.sleep_service()


async def admin_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fn = "admin_status:"
    message: Message = try_get(update, "message")
    chat: Chat = try_get(message, "chat")
    chat_id: int = try_get(chat, "id")
    user: User = try_get(message, "from_user")
    user_id: int = try_get(user, "id")
    if user_id != THE_CREATOR:
        return
    abbot: Abbot = Abbot(chat_id)
    status_data = json.dumps(abbot.get_config(), indent=4)
    bot_debug.log(f"statuses => {abbot} status_data={status_data}")
    await message.reply_text(status_data)
