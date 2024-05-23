import tkinter as tk
from tkinter import ttk

# from utils.ForwardHandler import start_message_forwards
from utils.forward_thread import start_script, stop_script

# from utils.ForwardHandler import MessageForwarder
config_file = "src/credentials/telegram.json"
# forwarder = MessageForwarder(config_file)
# forwarder.join_chats()

channel_mapping = {
        "OptionsTrading_Stocks_Index":["destrinationchannel"],
        "iiiinnnndddeeeexxxkkkkiii":["destrinationchannel"],
        "Buls7":["destrinationchannel"],
        "accuratrtrading":["destrinationchannel"],
        "https://https://t.me/+U9cmwkJ6tWgyZTI1":["destrinationchannel"]
    }
import json
import tkinter as tk
from tkinter import ttk
import threading
class GUIHandler:
    def __init__(self, width=600, height=400):
        self.data = {}
        self.root = tk.Tk()
        self.root.title("Telegram Message Forwarder")
        self.width = width
        self.height = height
        self.root.geometry(f"{self.width}x{self.height}")

        self.channel_frame = ttk.LabelFrame(self.root, text="Channels")
        self.channel_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.selected_channels = {}
        self.channel_widgets = {}

        self.start_button = ttk.Button(self.root, text="Start Forwarding", command=self.start_forwarding)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.stop_button = ttk.Button(self.root, text="Stop Forwarding", command=self.stop_forwarding)
        self.stop_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.stop_button.config(state="disabled")  # Disable stop button initially

    def add_channel(self, channel_name):
        channel_var = tk.BooleanVar(value=False)  # Set default value to False
        
        def callback(var_name, index, mode):
            self.stop_forwarding()
            data ={}
            enabled_channels = [channel for channel, var in self.channel_widgets.items() if var["checkbox"].get()]
            for i in enabled_channels:
                if i == 'OPTIONS TRADING':
                    data["OptionsTrading_Stocks_Index"]=["https://t.me/+1GiUfQZOPK5jYTI0"]
                if i == 'STOCK/INDEX':
                    data["https://t.me/iiiinnnndddeeeexxxkkkkiii"]=["https://t.me/+1GiUfQZOPK5jYTI0"]
                if i == 'STOCK EXPERT':
                    data["Buls7"]=["https://t.me/+1GiUfQZOPK5jYTI0"]
                if i == 'ACCURATE TRADING':
                    data["accuratrtrading"]=["https://t.me/+1GiUfQZOPK5jYTI0"]
                if i == 'MY':
                    data["https://t.me/+U9cmwkJ6tWgyZTI1"]=["destrinationchannel"]
            self.data = data
            with open('forward_data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
                
        channel_var.trace_add("write", callback)
        channel_frame = ttk.Frame(self.channel_frame)
        channel_frame.pack(anchor="w", fill="x", padx=5, pady=5)

        channel_label = ttk.Checkbutton(channel_frame, text=channel_name, variable=channel_var)
        channel_label.pack(side=tk.LEFT, padx=(0, 10))

        sl_entry = ttk.Entry(channel_frame)
        sl_entry.pack(side=tk.LEFT, padx=5)
        sl_label = ttk.Label(channel_frame, text="SL")
        sl_label.pack(side=tk.LEFT)

        bp_entry = ttk.Entry(channel_frame)
        bp_entry.pack(side=tk.LEFT, padx=5)
        bp_label = ttk.Label(channel_frame, text="BP")
        bp_label.pack(side=tk.LEFT)

        tp1_entry = ttk.Entry(channel_frame)
        tp1_entry.pack(side=tk.LEFT, padx=5)
        tp1_label = ttk.Label(channel_frame, text="TP1")
        tp1_label.pack(side=tk.LEFT)

        self.channel_widgets[channel_name] = {
            "checkbox": channel_var,
            "sl_entry": sl_entry,
            "bp_entry": bp_entry,
            "tp1_entry": tp1_entry
        }

    def remove_channel(self, channel_name):
        if channel_name in self.channel_widgets:
            self.channel_widgets[channel_name]["checkbox"].set(False)
            del self.channel_widgets[channel_name]

    def get_selected_channels(self):
        selected_channels = [channel for channel, var in self.channel_widgets.items() if var["checkbox"].get()]
        return selected_channels

    def get_sl_bp_tp1(self, channel_name):
        if channel_name in self.channel_widgets:
            sl = self.channel_widgets[channel_name]["sl_entry"].get()
            bp = self.channel_widgets[channel_name]["bp_entry"].get()
            tp1 = self.channel_widgets[channel_name]["tp1_entry"].get()
            return sl, bp, tp1
        return None, None, None

    def start_forwarding(self):
        self.start_button.config(state="disabled")  # Disable start button
        self.stop_button.config(state="normal")     # Enable stop button
        enabled_channels = [channel for channel, var in self.channel_widgets.items() if var["checkbox"].get()]
        if enabled_channels == []:
            self.stop_forwarding()
        else:
            print(self.data)
            start_script()
            pass
        # Do something with selected channels

    def stop_forwarding(self):
        self.stop_button.config(state="disabled")   # Disable stop button
        self.start_button.config(state="normal")    # Enable start button
        # Stop forwarding process
        print("Hello ")
        stop_script()
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    names = ['OPTIONS TRADING ', 'STOCK/INDEX', 'STOCK EXPERT', 'ACCURATE TRADING','MY']
    
    gui = GUIHandler(width=800, height=600)
    for i in names:
        gui.add_channel(i)

    gui.run()
