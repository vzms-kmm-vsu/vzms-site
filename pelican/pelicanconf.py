# coding: utf-8
import csv
from os import listdir

SITENAME = {
    'full': 'Воронежская зимняя математическая школа',
    'short': 'ВЗМШ'
}
SITEURL = 'vzms.kmm-vsu.ru'

AUTHOR = 'ijustbsd@gmail.com'
DESCRIPTION = 'Воронежская зимняя математическая школа C.Г. Крейна'
KEYWORDS = 'Воронежская зимняя математическая школа, ВЗМШ'
YEAR = '2020'

THEME = 'theme'

SLUGIFY_SOURCE = 'basename'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

PAGE_ORDER_BY = 'order'

STATIC_PATHS = ['files', 'albums']

PHOTOS = [(x, listdir('content/albums/' + x))
          for x in listdir('content/albums')]

with open('participants.csv', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    PARTICIPANTS = enumerate(tuple(reader), 1)

# Disable generations some files
ARCHIVES_SAVE_AS = None
AUTHORS_SAVE_AS = None
CATEGORIES_SAVE_AS = None
FEED_ALL_ATOM = None
TAGS_SAVE_AS = None
