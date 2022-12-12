from revChatGPT.revChatGPT import AsyncChatbot as Chatbot
import json


async def handle_response(prompt) -> str:
    chatbot.refresh_session()
    response = await chatbot.get_chat_response(prompt, output="text")
    responseMessage = response['message']

    return responseMessage


def get_config() -> dict:
    import os
    # get config.json path
    config_dir = os.path.abspath(__file__ + "/../../")
    config_name = 'config.json'
    config_path = os.path.join(config_dir, config_name)

    with open(config_path, 'r') as f:
        data = json.load(f)

    return data


data = get_config()

config = {
    "session_token": data['session_token'],
    "cf_clearance": "mfYac5nZa9LEbBstWcvmGxoEPIRTqWFvgqGE5lozFtM-1670818572-0-160",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}

chatbot = Chatbot(config, conversation_id=None)
