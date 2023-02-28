#!/usr/bin/env python3
#Hi developer,here is an example bot. You can read this to learn how to write a bot easily.
import hackchat
import time

#This func is used to get messages.
def message_got(message,sender,trip):
    print('{who} says: {msg}'.format(who=sender,msg=message))

#This func is used to get join notifications.
def user_join(nick,trip):
    print("{user} joined.".format(user=nick))

#This func is used to get leave notifications.
def user_leave(nick):
    print("{user} left".format(user=nick))

#This func is used to get whisper.
def whisper_got(message,nick,trip):
    print("{user} whispered to you: {msg}".format(user=nick,msg=message))

#This func is used to get errors.
def kill_errors(info):
    print("An error occured.Details: {}".format(info))

chat=hackchat.hackchat("lounge","TestBot","TestBotPassword") #3 strings are required. The channel,the nick and the password.
chat.message_function+=[message_got]
chat.join_function+=[user_join]
chat.leave_function+=[user_leave]
chat.whisper_function+=[whisper_got]
chat.error_function+=[kill_errors]
time.sleep(1)
chat.send_message("Hello World!")    #Send messages.
time.sleep(1)
#chat.send_to("target nick","message")   #Send whispers.
#chat.change_nick("new nick")  #Change the nick of the bot.
chat.run(False) 
