from workers import WorkerEntrypoint, Response
import json
from js import fetch


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        if request.method != "POST":
            return Response("Telegram bot is alive.")

        update = await request.json()

        message = update.get("message", {})
        chat = message.get("chat", {})
        text = message.get("text", "")

        if not chat:
            return Response("OK")

        chat_id = chat.get("id")

        if text == "/start":
            reply = "I'm alive! 🤖"
        elif text == "/help":
            reply = "/start — start the bot\n/help — show help"
        elif text:
            reply = f"You said: {text}"
        else:
            return Response("OK")

        token = self.env.TELEGRAM_BOT_TOKEN

        await fetch(
            f"https://api.telegram.org/bot{token}/sendMessage",
            {
                "method": "POST",
                "headers": {
                    "Content-Type": "application/json"
                },
                "body": json.dumps({
                    "chat_id": chat_id,
                    "text": reply
                })
            }
        )

        return Response("OK")
