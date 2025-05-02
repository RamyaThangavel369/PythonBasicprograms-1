import random

jokes = ["Alright! I took the quiz and it turns out I do put career over men.",
       "Yes, on a scale of one to 10, 10 being the dumbest a person can look, you are definitely 19",
       "I'm not great at advice. Can I interest you with a sarcastic comment?",
       "Ok, you have to stop the Q-tip when there's resistance!",
        "What do you know? You're a door. You only like knock knock jokes.",
         "Until I was 25, I thought that the only response to 'I love you' was 'Oh, crap!'"]
def getReply(message):
   message=message.lower()

   if 'who' in message and 'you' in message:
      reply="Hello,I  am Ramya"
   elif 'jokes' in message:
      reply = random.choice(jokes)
   elif 'how are you' in message:
       reply="I am doing good"
   elif 'jokes' in message:
       reply=random.choice(jokes)
   elif 'age' in message:
       reply="I am 33 years old"
   else:
       reply ="i am good!"
       print('Bot:',reply)
message=''
While: 'bye' not in message
message = input('human:')
getReply(message)


