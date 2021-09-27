import csv
import logging

from pelican import signals

from .config import PARTICIPANTS_CSV, PARTICIPANTS_RAW_CSV
from .downloader import download_participants_csv
from .formatter import format_csv

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def create_participants_list(_):
    download_participants_csv(PARTICIPANTS_RAW_CSV)
    format_csv(PARTICIPANTS_RAW_CSV, PARTICIPANTS_CSV)
    logger.info('Participant list formatted successfully!')


def add_participants_to_context(generator):
    with open(PARTICIPANTS_CSV, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        generator.context['PARTICIPANTS'] = enumerate(tuple(reader), 1)
    logger.info('Participant list added to generator context!')


def register():
    signals.initialized.connect(create_participants_list)
    signals.generator_init.connect(add_participants_to_context)


__all__ = ('register',)
