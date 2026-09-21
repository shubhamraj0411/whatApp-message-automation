#twilio client setup


from twilio.rest import Client
from datetime import datetime, timedelta
import time
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
auth_token = os.getenv("ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

client = Client(account_sid, auth_token)

def send_whatsApp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
           from_='whatsapp:+17372508034',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'message sent successfully ! Message SID {message.sid}')
    except Exception as e:
        print('An error occured :')

name = input('Enter the recipent name = ')
recipient_number = input('Enter the recipient whatsApp number with country code (e.g +911234567890)')
message_body = input(f'Enter the message you want to send to the {name}: ')


date_str = input('enter the date to send the message (YYYY-MM-DD)')
time_str = input('enter the time to send the message (HH-MM in 24hour format): ')

schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

#for calculation of time delay
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print('the specified time is in the past. so the message cannot be send. add the future time ')
else:
    print(f'Message schedule to be sent to {name} at {schedule_datetime}.')

    time.sleep(delay_seconds)
    send_whatsApp_message(recipient_number, message_body)
    print("thank you for using this")
    