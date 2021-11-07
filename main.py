import os
import discord
import requests
import json
import random

bot_token = os.environ['BOT_TOKEN']

client = discord.Client()


anxiety = ["anxiety", "anxious", "worried", "fear", "fearful"]
depression = ["depression", "depressed","sad", "down"]
greetings = ["hi", "hello","how are you", "what's up", "whats up" ]
goodbye = ["bye", "see you later", "goodbye", "thank you", "see you", "see ya"]

anxiety_response = [
  "I understand and your feelings are valid. "
  
]
depression_response = [

]
greetings_response = [
  "Hi there, I'm doing well! My name is Evelyn, what can I do for you?",
  "Hey there, my name's Evelyn, your mental health friend. How can I help you today?"]
goodbye_response = [
  "See you later! Take care!",
  "Have a lovely day! Take care and stay safe!",
  "Take care of yourself! I'm always here to support you! Feel free to come back at any time!"]
invalid_response = [
 "I’m sorry, I do not understand. Can you repeat that?",
 "Can you please rephrase your request? I do not understand."

]

def get_quote(): 
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return (quote)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  msg = message.content
  if message.author == client.user:
    return

  if msg.startswith('$hello'):
    await message.channel.send('Hello!')

  elif msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  elif any(word in msg.lower() for word in anxiety):
    await message.channel.send(random.choice(anxiety_response))
  
  elif any(word in msg.lower() for word in depression):
    await message.channel.send(random.choice(depression_response))

  elif any(word in msg.lower() for word in greetings):
    await message.channel.send(random.choice(greetings_response))

  elif any(word in msg.lower() for word in goodbye):
    await message.channel.send(random.choice(goodbye_response))
    
  else: await message.channel.send(random.choice(invalid_response))

  
client.run(bot_token)






