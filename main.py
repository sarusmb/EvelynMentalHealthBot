import os
import discord
import requests
import json
import random

bot_token = os.environ['BOT_TOKEN']

client = discord.Client()


anxiety = ["anxiety", "anxious", "worried", "fear", "fearful"]
depression = ["depression", "depressed","sad", "down"]
resources = ["resources", "websites", "videos", "links"]
greetings = ["hi", "hello","how are you", "what's up", "whats up" ]
goodbye = ["bye", "see you later", "goodbye", "thank you", "see you", "see ya"]

anxiety_response = [
 """ You are not alone. Here are some tips for coping with anxiety.
  
  Take a time-out. Practice yoga, listen to music, meditate, get a massage, or learn relaxation techniques. Stepping back from the problem helps clear your head.
  
  Get enough sleep. When stressed, your body needs additional sleep and rest.

  Limit alcohol and caffeine, which can aggravate anxiety and trigger panic attacks.
   """,
   """
  I understand how you feel. I recommend the trying out the following....

  Take deep breaths. Inhale and exhale slowly. Count to 10 slowly. Repeat, and count to 20 if necessary.
  
  Accept that you cannot control everything. Put your stress in perspective: Is it really as bad as you think?

  Learn what triggers your anxiety. Is it work, family, school, or something else you can identify? Write in a journal when you’re feeling stressed or anxious, and look for a pattern.

  Talk to someone. Tell friends and family you’re feeling overwhelmed, and let them know how they can help you. Talk to a physician or therapist for professional help.
   """
]

depression_response = [ 
  """
  Your feelings are valid and you are not alone. One of the most insidious aspects of depression is that it tricks you into thinking that nothing will help, or that the relief will be temporary, and it will keep you in a cycle of maladaptive thinking,feeling, and doing (or non-doing). However, there are steps one can take to cope with depression. 

  Seek professional help! There are different medical and mental health professionals who can help treat your depression and get you on the path to feeling better.
  """,
  """
  You are not alone. Here are some tips I have....

  Get active! It is important to get 30 minutes of physical activity daily. This can be anything from yoga, walking, jogging, walking stairs, a stroll around the block, gardening. If this is too daunting, start with 10-15 minutes a day and add 5 minutes to each day. 

  Talk to friends and family. For some, this may mean forging stronger ties with friends or family. Knowing you can count on supportive loved ones to help can go a long way toward improving your depression.
  
  """,
  """
   Depression can tinge recollections with negative emotions. You may find yourself focusing on the one thing that went wrong instead of the many things that went right. Try to stop this overgeneralization. Push yourself to recognize the good. If it helps, write down what was happy about the event or day. Then write down what went wrong. Seeing the weight you’re giving to one thing may help you direct your thoughts away from the whole and to the individual pieces that were positive.
  
  """
]

resources_response = ["""
Anxiety Canada is a great resource to visit to supplement learning about your anxiety. Click the link below
https://www.anxietycanada.com/

"""]
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

  elif any(word in msg.lower() for word in resources):
    await message.channel.send(random.choice(resources_response))
    
  else: await message.channel.send(random.choice(invalid_response))

  
client.run(bot_token)






