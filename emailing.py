import dotenv
import os
import smtplib
from email.message import EmailMessage
from PIL import Image
import io


dotenv.load_dotenv()
gmail_password = str( os.getenv( "GMAIL_PASSWORD" ) )
sender_email = str( os.getenv( "SENDER_EMAIL" ) )
recipient_email = str( os.getenv( "RECIPIENT_EMAIL" ) )


def send_email( attachment_image_filename: str, sender: str = sender_email, password: str = gmail_password, recipient: str = recipient_email ) -> None:
    email_message = EmailMessage()
    email_message["Subject"] = "Motion Detected!"
    email_message.set_content( "Motion was just detected" )
    
    with open( attachment_image_filename, "rb" ) as motion_capture:
        motion_capture_image = motion_capture.read()
        
    try:
        with Image.open( io.BytesIO( motion_capture_image ) ) as img:
            image_format = img.format.lower() # type: ignore > catches None type here deliberately
    except IOError:
        image_format = None
    
    email_message.add_attachment( motion_capture_image, maintype = "image", subtype = image_format )
    
    gmail = smtplib.SMTP( host = "smtp.gmail.com", port = 587 )
    gmail.ehlo()
    gmail.starttls()
    gmail.login( sender, password )
    gmail.sendmail( from_addr = sender, to_addrs = recipient, msg = email_message.as_string() )
    gmail.quit()
    
    print( f"Email was sent! with attachment {attachment_image_filename}" )
    

# =========================================================================== #

if __name__ == "__main__":
    send_email( attachment_image_filename = "scratchpad/aligator.png" )
