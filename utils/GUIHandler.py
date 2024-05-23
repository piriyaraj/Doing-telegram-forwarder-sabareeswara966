import tkinter as tk
from tkinter import ttk

class GUIHandler:
    def __init__(self, width=600, height=400):
        self.root = tk.Tk()
        self.root.title("Telegram Message Forwarder")
        self.width = width
        self.height = height
        self.root.geometry(f"{self.width}x{self.height}")

        self.channel_frame = ttk.LabelFrame(self.root, text="Channels")
        self.channel_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.selected_channels = {}
        self.channel_widgets = {}

    def add_channel(self, channel_name):
        channel_var = tk.BooleanVar(value=True)

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

    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
# Example usage:
    gui = GUIHandler(width=800, height=600)
    gui.add_channel("Channel 1")
    gui.add_channel("Channel 2")
    selected_channels = gui.get_selected_channels()
    print("Selected channels:", selected_channels)
    gui.run()
