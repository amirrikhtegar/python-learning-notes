from pprint import pprint

class Email:

    def __init__(self, sender:str, recipient:str, subject:str, body:str) -> None:
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = str(body)

    def send_email(self) -> str:
        print(f"***{self.sender}***")
        print(f"**{self.recipient}**")
        print(f"*{self.subject}*")
        print(f"body: {self.body}")


em1 = Email("amir", "ali", "leasing", "in english we how not ")

pprint(em1.send_email())