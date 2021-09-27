import os

from dotenv import load_dotenv

load_dotenv()

MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_MAILING_LIST = os.getenv("MAILGUN_MAILING_LIST")

PARTICIPANTS_RAW_CSV = os.getenv("PARTICIPANTS_RAW_CSV")
