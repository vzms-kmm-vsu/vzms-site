import json
import logging

import requests

logger = logging.getLogger(__name__)


class Mailgun:
    BASE_URL = 'https://api.mailgun.net/v3'

    def __init__(self, api_key) -> None:
        self.API_KEY = api_key

    def _post(self, url, data):
        r = requests.post(
            url=Mailgun.BASE_URL + url,
            auth=('api', self.API_KEY),
            data=data
        )
        r.raise_for_status()
        return r

    def update_mailing_list(self, mailing_list: str, emails: list):
        data = {
            'upsert': True,
            'members': json.dumps([{'address': e} for e in emails])
        }

        try:
            response = self._post(f'/lists/{mailing_list}/members.json', data)
        except requests.exceptions.HTTPError as e:
            logger.error("Couldn't update Mailgun mailin list!")
            logger.error(f"Mailgun response: {e.response.json()}")
            raise

        logger.info('Mailgun mailing list updated successfully!')
        return response
