#sending whatsapp message using python code
import pywhatkit as kit
import time

phone_number = input("Enter the target phone number (with country code, e.g., +1234567890): ")
message = input("Enter the message: ")

print("Sending message. Please make sure you are logged into WhatsApp Web in your default browser.")

try:
    kit.sendwhatmsg_instantly(phone_number, message, wait_time=15, tab_close=True, close_time=2)
    time.sleep(20) 
    print("Message sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
