import re

def format_options_trading(message):
    # Updated pattern to match the specified formats, handling various characters and formatting
    pattern = r'(\b\w{1,10}\b)\s+(\d{1,5})\s+(CE|PE)\s+above\s+(\d{1,5})'
    match = re.search(pattern, message)
    if match:
        formatted_message = f"{match.group(1)} {match.group(2)} {match.group(3)} above {match.group(4)}"
        return formatted_message
    return "Message does not match the format."

# Test case
message = """
📊 BANKNIFTY 49200 CE above 350 

#INDEX_OPTIONS
"""

result = format_options_trading(message)
print(f"Result: {result}")
