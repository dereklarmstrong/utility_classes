import base64
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class GmailAPI:
    """
    The GmailAPI class provides an interface for sending emails using Gmail API.

    Attributes:
        service: An instance of the Gmail API service object.

    """
    def __init__(self, credentials):
        """
        The constructor takes the credentials required to authenticate the API requests.

        Args:
            credentials: An instance of the credentials object obtained using the Google API Console.

        """
        self.service = build('gmail', 'v1', credentials=credentials)

    def send_email(self, to, subject, body, attachments=None):
        """
        This method sends an email to the specified recipient.

        Args:
            to: The email address of the recipient.
            subject: The subject of the email.
            body: The body of the email.
            attachments: A list of file paths for the attachments. (default is None)

        Returns:
            None

        """
        try:
            message = MIMEMultipart()
            message['to'] = to
            message['subject'] = subject
            message.attach(MIMEText(body))

            if attachments:
                for attachment in attachments:
                    with open(attachment, 'rb') as f:
                        file = MIMEApplication(f.read(), _subtype="pdf")
                        file.add_header('content-disposition', 'attachment', filename=os.path.basename(attachment))
                        message.attach(file)

            create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
            send_message = (self.service.users().messages().send(userId="me", body=create_message).execute())
            print(f'sent message to {to} with email Id: {send_message["id"]}')
        except HttpError as error:
            print(f'An error occurred: {error}')
