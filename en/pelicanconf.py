# coding: utf-8

SITENAME = {
    "full": "Voronezh Winter Mathematical School",
    "short": "VWMS",
}
SITEURL = "vzms.kmm-vsu.ru/en"

AUTHOR = "ijustbsd@gmail.com"
DESCRIPTION = "Voronezh Winter Mathematical School by S.G.Krein"
KEYWORDS = "Voronezh Winter Mathematical School, VWMS"
YEAR = "2022"

THEME = "theme"

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["participants_list", "mailing_list"]

SLUGIFY_SOURCE = "basename"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"

PAGE_ORDER_BY = "order"

STATIC_PATHS = ["files"]

# Disable generations some files
ARCHIVES_SAVE_AS = None
AUTHORS_SAVE_AS = None
CATEGORIES_SAVE_AS = None
FEED_ALL_ATOM = None
TAGS_SAVE_AS = None
