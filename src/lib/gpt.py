import openai
from telegram import Message
from env import OPENAI_API_KEY
from lib.logger import debug

from lib.utils import try_get


class GPT:
    OPENAI_MODEL = "gpt-3.5-turbo-16k"

    def __init__(self, name, handle, type, personality, unleashed=False):
        openai.api_key = OPENAI_API_KEY
        self.model = self.OPENAI_MODEL
        self.name = name
        self.handle = handle
        self.type = type
        self.personality = personality
        self.messages = [dict(role="system", content=personality)]
        self.unleashed = unleashed
        self.started = True

    def __str__(self):
        return (
            f"GPT(model={self.model}, name={self.name}, personality={self.personality})"
        )

    def __repr__(self):
        return f"GPT(api_key=******, model={self.model}, name={self.name}, personality={self.personality}, messages={self.messages})"

    def start(self):
        self.started = True

    def stop(self):
        self.started = False

    def unleash(self):
        self.unleashed = True
        return self.unleashed

    def leash(self):
        self.unleashed = False
        return self.unleashed

    def update_messages(self, telegram_message: Message | str | dict):
        prompt = (
            try_get(telegram_message, "text")
            if type(telegram_message) == Message
            else telegram_message
        )
        message_dict = dict(role="user", content=prompt)
        self.messages.append(message_dict)

    def chat_completion(self):
        try:
            response = openai.ChatCompletion.create(
                model=self.model, messages=self.messages, tempature=0.5
            )
            return try_get(response, "choices", 0, "message", "content")
        except Exception as e:
            debug(f"Error: GPT => chat_completion => exception={e}")
            return None
