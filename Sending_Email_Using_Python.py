import os, smtplib, ssl, getpass, imaplib, email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import *
from tkinter import messagebox

"""Part 2:"""

def assimilator(sender_email, sender_password, receiver_email, Subject, Body, cc_email, bcc_email):
    port = 587                                                                  # Port for google mail
    smtp_server = "smtp.gmail.com"                                              # Server Mail   
    mailPassword = 'icrdvamquacafwdd'
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = Subject
    
    receivers = receiver_email.split()
    if (cc_email != None):
        message["Cc"] = cc_email
        cc = (cc_email.strip()).split()
        receivers.extend(cc)
    if (bcc_email != None):
        #message["Bcc"] = bcc_email
        bcc = (bcc_email.strip()).split()
        receivers.extend(bcc)

    #The body and the attachments for the mail
    message.attach(MIMEText(Body, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_email, sender_password) #login with mail_id and password
    text = message.as_string()


    session.sendmail(sender_email, receivers, text)
    session.quit()
    #print('Mail Sent')

#sender = 'anasalakkadproj1@gmail.com'
#reciever = 'anasalakkadproj2@gmail.com'
#EmailSubject = 'Sending Email Test for the project'
#EmailContent = 'This is a test for sending email.'
# assimilator(sender, reciever, EmailSubject, EmailContent)

"""Part 3,4, and 5 (Send Email from Application):"""

emailGUI = tk.Tk()
emailGUI.title("Emailing App")
emailGUI.geometry('600x600')

sender_email = StringVar()
receiver_email = StringVar()
subject_email = StringVar()
message_email = StringVar()
password_email = StringVar()
cc_email = StringVar()
bcc_email = StringVar()

#Draw GUI

labelTo = Label(emailGUI, text='To:', fg='black', font=('Arial',14))
labelTo.grid(row=0, column=0, padx=5,pady=10)
textboxTo = Entry(emailGUI,textvariable = receiver_email, fg='black', width='40', font=('Arial',14))
textboxTo.grid(row=0, column=1)

labelCc = Label(emailGUI, text='Cc:', fg='black', font=('Arial',14))
labelCc.grid(row=1, column=0, padx=5,pady=10)
textboxCc = Entry(emailGUI,textvariable = cc_email, fg='black', width='40', font=('Arial',14))
textboxCc.grid(row=1, column=1)

labelBcc = Label(emailGUI, text='Bcc:', fg='black', font=('Arial',14))
labelBcc.grid(row=2, column=0, padx=5,pady=10)
textboxBcc = Entry(emailGUI,textvariable = bcc_email, fg='black', width='40', font=('Arial',14))
textboxBcc.grid(row=2, column=1)


labelFrom = Label(emailGUI, text='From:', fg='black', font=('Arial',14))
labelFrom.grid(row=3, column=0, padx=5,pady=10)
textboxFrom = Entry(emailGUI, textvariable = sender_email, fg='black', width='40', font=('Arial',14))
textboxFrom.grid(row=3, column=1)

labelSubject = Label(emailGUI, text='Subject:', fg='black', font=('Arial',14))
labelSubject.grid(row=4, column=0, padx=5,pady=10)
textboxSubject = Entry(emailGUI, textvariable = subject_email, fg='black', width='40', font=('Arial',14))
textboxSubject.grid(row=4, column=1)

labelMessage = Label(emailGUI, text='Message:', fg='black', font=('Arial',14))
labelMessage.grid(row=5, column=0, padx=5,pady=10)
textboxMessage = Text(emailGUI, fg='black', font=('Arial',14))
textboxMessage.place(x=5, y=250, width=575, height=250)

# Define Send Command
def send():
  passwordWindow = Toplevel(emailGUI)
  passwordWindow.title('Enter Password')
  passwordWindow.geometry('650x200')

  # Sender Line
  labelEmail = Label(passwordWindow, text='Email:', fg='black', font=('Arial',14))
  labelEmail.grid(row=0, column=0, padx=5,pady=10)
  labelEmailAddress = Label(passwordWindow, text = sender_email.get(), fg='black', width='40', font=('Arial',14))
  labelEmailAddress.grid(row=0, column=1)

  # Password Line
  labelPassword = Label(passwordWindow, text='Password', fg='black', font=('Arial',14))
  labelPassword.grid(row=1, column=0, padx=5,pady=10)
  textboxPassword = Entry(passwordWindow,textvariable = password_email, fg='black', width='40', font=('Arial',14), show="*")
  textboxPassword.grid(row=1, column=1)

  # Define Sign In Command
  def signIn():
    emailsubject = subject_email.get()
    sender = sender_email.get()
    password = password_email.get()
    receiver = receiver_email.get()
    ccEmail = cc_email.get()
    bccEmail = bcc_email.get()
    emailcontent = textboxMessage.get('1.0',END)

    assimilator(sender, password, receiver, emailsubject, emailcontent, ccEmail, bccEmail)

  #OK button
  buttonOK = Button(passwordWindow, command = signIn, text='Sign In', fg='black', font=('Arial', 14), pady=10)
  buttonOK.grid(row = 2, column = 1, padx = 5, pady = 10)


#Send Button
buttonSend = Button(emailGUI, command = send, text='Send', fg='black', font=('Arial', 14), pady=10)
buttonSend.place(x=275, y=575, width=100)


emailGUI.mainloop()