import smtplib, ssl

class SendNotifications():
    
    def __init__(self, distroList, message):
        self.distroList = distroList
        self.message = message 
    
    def send(self):
        sender = "" # fill with gmail account
        password = "" # email password
        port = 465  # For SSL
        context = ssl.create_default_context()
        
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender, password)
            for member in self.distroList:
                server.sendmail(sender, member, self.message)
