from abc import ABC, abstractmethod

from gittranslate.translation.base.translation_options import TranslationOptions


class TranslationService(ABC):
    """
    Interface specifying the signature of a translation call
    """

    @abstractmethod
    def translate(self, content: str, options: TranslationOptions) -> str:
        """
        Translates the specified ``content`` based on the supplied ``options`` and returns
        the translated result.

        Args:
            content: the text to be translated
            options: translation configuration

        Returns: the translated text as a ``str``

        """
        raise NotImplementedError('This method needs to be implemented.')
