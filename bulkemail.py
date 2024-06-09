#Create a function to Send bulk email using python.
import smtplib

try:
    ob = smtplib.SMTP('smtp.gmail.com', 587)
    ob.ehlo()
    ob.starttls()
    ob.login('officialanurag134@gmail.com', 'bvqs fcuj sbjf grms ')  # Use App Password if 2FA is enabled
    subject = input("enter subject: ")
    body = input("Enter your message: ")
    message = f'Subject: {subject}\n\n{body}'
    ob.sendmail('anurag1342001@gmail.com', 'bhupesh7750@gmail.com', message)
    print("Email sent successfully")
except smtplib.SMTPAuthenticationError as e:
    print("Failed to authenticate:", e)
except Exception as e:
    print("Failed to send email:", e)
finally:
    ob.quit()
