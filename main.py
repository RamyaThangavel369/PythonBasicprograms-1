import re
import from long_responses as long
def get_response(user_input):
    split_message=re.split('r\s|[,;"?_]\s*',user_input.lower())
    response=check_all_messages(split_message)
    return response
while True:
    print('Bot: '+ get_response(input('You: ')))

