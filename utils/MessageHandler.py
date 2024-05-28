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
        pattern = r'^([A-Z ]+) ([0-9]+) CE BUY ABOVE ([0-9]+(\.[0-9]+)?)$'
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
if __name__ == '__main__':
    # Example usage:
    message = """
HEROMOTOCO 5100 PE AT ₹55

STOPLOSS AT ₹48

TARGET ₹68_₹77+🚀
    """
    formatted_message = MessageHandler().check_message(message=message)
    if formatted_message:
        print("Formatted message:", formatted_message)
    else:
        print("Message does not match the format.")
