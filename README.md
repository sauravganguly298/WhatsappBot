# WhatsappBot
This is the simple WhatsApp Bot which is made in python using the automation API that is selenium.

This has several function which uses basically selenium API.

Function that it has:-
def search_user(username):-
  This function searches the user and invokes the first matched user by clicking on the first matched user the selection of the search box is performed using the XPATH.
def user_chat(username,message,no_of_times=1):-
  This function clicks on the message box of the selected user and send the keys to the message box .Then it will click on send this will result in sending of the message to the invoked user by search_user function.
def spam(username,message,no_of_times=1):-
  This function is responsible for the spamming purpose the spamming is done using repetative sending of the message using a loop.
  
  
  
  
  Further Scopes of the project:-
  - Implement the machine learning technique to chat like a bot.
  - Implement the time module to send the message at a particular time by the bot.
