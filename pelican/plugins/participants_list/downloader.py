import logging

import requests

from .config import PARTICIPANTS_URL

logger = logging.getLogger(__name__)


def download_participants_csv(csv_out: str) -> None:
    try:
        r = requests.get(PARTICIPANTS_URL)
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        logger.error("Couldn't get participants list!")
        raise

    with open(csv_out, 'wb') as f:
        f.write(r.content)
