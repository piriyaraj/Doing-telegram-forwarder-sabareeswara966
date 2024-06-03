
import json
from pyrogram import Client
from pyrogram.errors import UserAlreadyParticipant, FloodWait
from colorama import Fore, Style, init
import threading
import time

from ExcelHandler import ExcelHandler
from MessageHandler import MessageHandler

# Define a global flag to control the script
script_running = False
def run_script_1():
    init(autoreset=True)

    # Read credentials from JSON file
    with open('src/credentials/telegram.json') as json_file:
        credentials = json.load(json_file)

    # Extract values
    api_id = credentials.get('api_id')
    api_hash = credentials.get('api_hash')
    phone_number = credentials.get('phone_number')
    
    app = Client(
        'pj',
        api_id=api_id,
        api_hash=api_hash,
        phone_number=phone_number,
    )

    app.start()

    # custom_caption = "Your Caption" #-- Your Caption you can use "" for no caption
    # replace_text = "Replace Text" #-- Enter the text you want to replace.
    # your_text = "Your Text" #-- Enter your text that you want to replace other's text with your own.

    # # Enter Source Channel and Your Channel - Also support multiple source and destination.
    # # 
    with open('forward_data.json') as json_file:
        channel_mapping = json.load(json_file)
    # channel_mapping = {
    #     'sourcegroup132': ['destrinationchannel'], #public group to public channel
    #     'https://t.me/+dEet52AjhxAwNDk1': ['destrinationchannel'], #private group to public channel
    #     }

    # try:
    #     for source_chat, dest_chats in channel_mapping.items():
    #         try:
    #             print(f"{Fore.GREEN}Joining source chat: {source_chat}")
    #             app.join_chat(source_chat)
    #         except Exception as e:
    #             print(f"{Fore.RED}Error joining source chat '{source_chat}': {e}")
                
    #         for dest_chat in dest_chats:
    #             try:
    #                 print(f"{Fore.CYAN}Joining destination chat: {dest_chat}")
    #                 app.join_chat(dest_chat)
    #             except Exception as e:
    #                 print(f"{Fore.RED}Error joining destination chat '{dest_chat}': {e}")
    # except UserAlreadyParticipant:
    #     pass
    # except Exception as e:
    #     print(f"{Fore.RED}Error: {e}")

    try:
        sources = [app.get_chat(source_chat) for source_chat in channel_mapping.keys()]
        destinations = [
            [app.get_chat(dest_chat) for dest_chat in dest_chats]
            for dest_chats in channel_mapping.values()
        ]
    except Exception as e:
        print(f"{Fore.RED}Error getting chat objects: {e}")
    app.stop()
    print("Started......")

    message_handler = MessageHandler()
    handler = ExcelHandler()
    @app.on_message()
    async def my_handler(client, message):
        # final_caption = custom_caption

        for source, dests in zip(sources, destinations):
            try:
                if message.chat.id == source.id:
                    is_required_message = False
                    # print(f"{Fore.YELLOW}{message}")
                    channel = message.chat.title

                    if message.caption:
                        # edited_caption = message.caption.replace(replace_text, your_text)
                        final_caption = message.caption
                        for dest in dests:
                            try:
                                status, formatted_message,data = message_handler.check_message(final_caption)
                                if status:
                                    is_required_message = True
                                    print(f"{Fore.YELLOW}{formatted_message}")
                                    await message.copy(dest.id, caption=formatted_message)
                                    print(f"{Fore.BLUE}Message copied to {dest.id} with caption: {final_caption}")
                            except Exception as e:
                                print(f"{Fore.RED}Error copying message to {dest.id}: {e}")
                    elif message.text:
                        # edited_text = message.text.replace(replace_text, your_text)
                        final_caption = message.text
                        for dest in dests:
                            try:
                                status, formatted_message, data = message_handler.check_message(final_caption)
                                if status:
                                    is_required_message = True
                                    print(f"{Fore.YELLOW}{formatted_message}")
                                    await app.send_message(dest.id, text=formatted_message)
                                    print(f"{Fore.BLUE}Message sent to {dest.id} with text: {final_caption}")
                            except Exception as e:
                                print(f"{Fore.RED}Error sending message to {dest.id}: {e}")
                    else:
                        for dest in dests:
                            try:
                                status, formatted_message, data = message_handler.check_message(final_caption)
                                if status:
                                    is_required_message = True
                                    print(f"{Fore.YELLOW}{formatted_message}")
                                    await message.copy(dest.id, caption=formatted_message)
                                    print(f"{Fore.BLUE}Message copied to {dest.id} with caption: {final_caption}")
                            except Exception as e:
                                print(f"{Fore.RED}Error copying message to {dest.id}: {e}")
                    if is_required_message:
                        handler.save_to_excel([final_caption, channel]+data)
            except Exception as e:
                print(f"{Fore.RED}Error in message handling: {e}")
    app.run()

run_script_1()