import pandas as pd
from datetime import datetime
import os

class ExcelHandler:
    def __init__(self, filename_prefix='Orders_', output_dir='./src/Orders/'):
        self.filename_prefix = filename_prefix
        self.output_dir = output_dir
        os.makedirs("src/Orders", exist_ok=True)
        
    def create_filename(self):
        today = datetime.now()
        return f"{self.filename_prefix}{today.strftime('%d_%m_%Y')}.xlsx"

    def save_to_excel(self, data):
        filename = self.create_filename()
        filepath = f"{self.output_dir}/{filename}"

        if os.path.exists(filepath):
            df = pd.read_excel(filepath)
        else:
            df = pd.DataFrame(columns=['Time', 'Message', 'Source Channel'])

        current_time = datetime.now().strftime('%H:%M:%S')
        new_data = {'Time': current_time, 'Message': data[0], 'Source Channel': data[1]}
        df = df._append(new_data, ignore_index=True)

        df.to_excel(filepath, index=False)
        print(f"Data saved to {filepath}")

# # Example usage:
# handler = ExcelHandler()
# handler.save_to_excel(['Message 3', 'Channel 1'])
