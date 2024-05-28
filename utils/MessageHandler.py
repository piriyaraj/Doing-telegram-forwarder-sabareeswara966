import os
import re

class MessageHandler:
    @staticmethod
    def format_options_trading(message):
        # Updated pattern to match the specified formats, handling various characters and formatting
        pattern = r'(\b\w{1,10}\b)\s+(\d{1,5})\s+(CE|PE)\s+above\s+(\d{1,5})'
        match = re.search(pattern, message)
        if match:
            formatted_message = f"{match.group(1)} {match.group(2)} {match.group(3)} BUY ABOVE {match.group(4)}"
            return formatted_message
        return None

    # done
    @staticmethod
    def format_stock_index(message):
        # Updated pattern with capture groups
        pattern = r'^\s*([A-Z ]+) ([0-9]+) CE BUY ABOVE ([0-9]+(\.[0-9]+)?)\s*(?:\nTGT ([0-9,]+))?\s*$'
        match = re.match(pattern, message)
        if match:
            # Construct the formatted message using the captured groups
            formatted_message = f"{match.group(1)} {match.group(2)} CE BUY ABOVE {match.group(3)}"
            return formatted_message
        return None

    # Done
    @staticmethod
    def format_stock_expert(message):
        # Format: XXXX YYYY ZZ  at AA
        pattern = r'(\b\w{1,10}\b)\s+(\d{1,5})\s+(CE|PE)\s+AT\s+₹(\d{1,5})'
        match = re.search(pattern, message)
        if match:
            formatted_message = f"{match.group(1)} {match.group(2)} {match.group(3)} BUY ABOVE {match.group(4)}"
            return formatted_message
        return None
    # Done
    @staticmethod
    def format_accurate_trading(message):
        # Updated pattern to match the specified formats
        pattern = r'^\s*buy\s+([A-Z0-9 ]+)\s+(CE|PE)\s*[\r\n]*abv\s+([0-9]+(\.[0-9]+)?)🍀\s*$'
        match = re.search(pattern, message, re.IGNORECASE)
        if match:
            formatted_message = f"{match.group(1).strip()} {match.group(2)} {match.group(3)} BUY ABOVE {match.group(3)}"
            return formatted_message
        return None

    def check_message(self,message):
        result = self.format_options_trading(message)
        if result != None:
            return True, result
        result = self.format_stock_index(message)
        if result != None:
            return True, result
        result = self.format_stock_expert(message)
        if result != None:
            return True, result
        result = self.format_accurate_trading(message)
        if result != None:
            return True, result
        
        return False, message
    
def read_text_files_and_process(directory):
    message_handler = MessageHandler()
    
    for root, dirs, files in os.walk(directory):
        print(root)
        for file in files:

            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    message = f.read()
                    formatted_message = message_handler.check_message(message=message)
                    print("   >>>",formatted_message)
if __name__ == '__main__':
    read_text_files_and_process('examples')
