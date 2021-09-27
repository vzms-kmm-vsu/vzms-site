# coding: utf-8
import csv
from os import listdir, scandir

SITENAME = {
    "full": "Voronezh Winter Mathematical School",
    "short": "VWMS",
}
SITEURL = "vzms.kmm-vsu.ru/en"

AUTHOR = "ijustbsd@gmail.com"
DESCRIPTION = "Voronezh Winter Mathematical School by S.G.Krein"
KEYWORDS = "Voronezh Winter Mathematical School, VWMS"
YEAR = "2020"

THEME = "theme"

SLUGIFY_SOURCE = "basename"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"

PAGE_ORDER_BY = "order"

STATIC_PATHS = ["files", "albums"]

PHOTOS = [
    (x.name, listdir("content/albums/" + x.name))
    for x in scandir("content/albums")
    if x.is_dir()
]

with open("participants.csv", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    PARTICIPANTS = enumerate(tuple(reader), 1)

# Disable generations some files
ARCHIVES_SAVE_AS = None
AUTHORS_SAVE_AS = None
CATEGORIES_SAVE_AS = None
FEED_ALL_ATOM = None
TAGS_SAVE_AS = None
