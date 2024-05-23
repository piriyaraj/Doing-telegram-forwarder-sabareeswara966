import re

class MessageHandler:
    @staticmethod
    def format_options_trading(message):
        # Format: XXXX YYYY ZZ above AA
        pattern = r'(\w{2,8})\s+(\d{1,5})\s+(CE|PE)\s+above\s+(\d{1,5})'
        match = re.search(pattern, message)
        if match:
            formatted_message = f"{match.group(1)} {match.group(2)} {match.group(3)} above {match.group(4)}"
            return formatted_message
        return None

    @staticmethod
    def format_stock_index(message):
        # Format: XXXX YYYY ZZ BUY above AA
        pattern = r'(\w{2,8})\s+(\d{1,5})\s+(CE|PE)\s+BUY\s+above\s+(\d{1,5})'
        match = re.search(pattern, message)
        if match:
            formatted_message = f"{match.group(1)} {match.group(2)} {match.group(3)} BUY above {match.group(4)}"
            return formatted_message
        return None

    @staticmethod
    def format_stock_expert(message):
        # Format: XXXX YYYY ZZ  at AA
        pattern = r'(\w{2,8})\s+(\d{1,5})\s+(CE|PE)\s+AT\s+₹(\d{1,5})'
        match = re.search(pattern, message)
        if match:
            formatted_message = f"{match.group(1)} {match.group(2)} {match.group(3)} at ₹{match.group(4)}"
            return formatted_message
        return None

    @staticmethod
    def format_accurate_trading(message):
        # Format: XXXX YYYY ZZ PPPP above AA
        pattern = r'BUY\s+(\w{2,8})\s+(\d{1,5})\s+(CE|PE)\s+ABV\s+(\d{1,5})'
        match = re.search(pattern, message.replace('\n', ' ').replace('\r', ' '))
        if match:
            formatted_message = f"{match.group(1)} {match.group(2)} {match.group(3)} ABV {match.group(4)}"
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
    BUY EXIDEIND 460 PE



    ABV 17.00
    """
    formatted_message = MessageHandler.format_accurate_trading(message)
    if formatted_message:
        print("Formatted message:", formatted_message)
    else:
        print("Message does not match the format.")
