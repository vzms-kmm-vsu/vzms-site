from pelican import signals

from .config import MAILGUN_API_KEY, MAILGUN_MAILING_LIST
from .mailgun import Mailgun
from .tools import get_participants_emails

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def update_mailing_list(_):
    emails = get_participants_emails()
    mg = Mailgun(MAILGUN_API_KEY)
    mg.update_mailing_list(MAILGUN_MAILING_LIST, emails)


def register():
    signals.initialized.connect(update_mailing_list)


__all__ = ('register',)
