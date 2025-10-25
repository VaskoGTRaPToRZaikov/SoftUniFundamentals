class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []

info = input().split()

while info[0] != "Stop":
    sender, receiver, content = info
    email = Email(sender,receiver, content)
    emails.append(email)
    info = input().split()

send_emails = [int(number) for number in input().split(', ')]

for num in send_emails:
    emails[num].send()

for message in emails:
    print(message.get_info())