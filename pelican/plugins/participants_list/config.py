import os

from dotenv import load_dotenv

load_dotenv()

PARTICIPANTS_RAW_CSV = os.getenv('PARTICIPANTS_RAW_CSV')
PARTICIPANTS_CSV = os.getenv('PARTICIPANTS_CSV')

GDRIVE_DOCUMENT_ID = os.getenv('GDRIVE_DOCUMENT_ID')
GDRIVE_SHEET_ID = os.getenv('GDRIVE_SHEET_ID')

PARTICIPANTS_URL = (
    'https://docs.google.com/spreadsheets/d/'
    f'{GDRIVE_DOCUMENT_ID}/export?format=csv&gid={GDRIVE_SHEET_ID}'
)
