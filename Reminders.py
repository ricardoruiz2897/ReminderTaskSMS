#Twilio api
from twilio.rest import Client

#To get current time.
from time import localtime, strftime

#To setup a timer.
import threading

#Set up

#Locked for github
account_sid = "xxxxxx"
auth_token = "xxxxxxx"

client = Client(account_sid, auth_token)

#Helper functions.
def send_reminder(text, sender_phone, receiver):
    message = client.messages.create(
        to=receiver,
        from_=sender_phone,
        body=text
    )


def get_time():
    time = strftime("%H:%M", localtime())
    return time


def handle_time(reminders,sender, receiver):
    t = get_time()
    print(reminders.keys())
    if t in reminders.keys():
        send_reminder(reminders[t], sender, receiver)
        return t


File = open("twilioapp.txt", "r")

#Get all the reminder into a hashmap, time is key and message is value.
reminders = dict()

lines = []
for line in File:
    lines.append(line)

for line in lines:
    line = line.rstrip()
    line = line.split(",")
    reminders[line[1]] = line[0]

sender_phone = input("Enter sender phone number (+1) (Should be registered in twilio account): ")
receiver = input("Enter phone to receive reminders (+1): ")

#Start timer.
#timer  = threading.Timer(5, handle_time(reminders))
timer  = threading.Timer(30, handle_time(reminders, sender_phone, receiver))
timer.start()



