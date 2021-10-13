from dataclasses import dataclass
from typing import Literal

"""
Language codes as listed at https://cloud.google.com/translate/docs/languages
"""
LanguageCode = Literal[
    'af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb ', 'zh-CN', 'zh', 'zh-TW',
    'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht',
    'ha', 'haw', 'he', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jv', 'kn', 'kk', 'km',
    'rw', 'ko', 'ku', 'ky', 'lo', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne',
    'no', 'ny', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk',
    'sl', 'so', 'es', 'su', 'sw', 'sv', 'tl', 'tg', 'ta', 'tt', 'te', 'th', 'tr', 'tk', 'uk', 'ur', 'ug', 'uz',
    'vi', 'cy', 'xh', 'yi', 'yo', 'zu'
]

MimeType = Literal['text/plain', 'text/html']


@dataclass(init=True, repr=True, kw_only=True, frozen=True)
class TranslationOptions:
    """
    Options to be passed to the ``translate`` call of a ``TranslationService`` object.
    """
    source_language_code: LanguageCode
    target_language_code: LanguageCode
    mime_type: MimeType
