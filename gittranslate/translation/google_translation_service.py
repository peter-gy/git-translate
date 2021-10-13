import os

from google.cloud import translate as gc_translate

import gittranslate.translation.base as trans_base
from gittranslate.translation.base import TranslationOptions


class GoogleTranslationService(trans_base.TranslationService):
    """
    ``TranslationService`` implementation based on the Google Cloud Translation API.
    """

    def __init__(self, *, service_key_path: str, project_id: str):
        """
        Args:
            service_key_path: the path to the Google Cloud Service JSON file that grants access
                              to the Google Cloud Translation API
            project_id: the ID of the Google Cloud Project
        """
        # Authentication to Google Cloud will occur using an environment variable
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = service_key_path
        self._project_id = project_id
        self._client = gc_translate.TranslationServiceClient()

    @property
    def project_id(self) -> str:
        """
        The ID of the Google Cloud Project in which the Google Cloud Translation Service was enabled.
        """
        return self._project_id

    def translate(self, content: str, options: TranslationOptions) -> str:
        location = 'global'
        parent = f'projects/{self._project_id}/locations/{location}'

        response: gc_translate.TranslateTextResponse = self._client.translate_text(
            request={
                "parent": parent,
                "contents": [content],
                "mime_type": options.mime_type,
                "source_language_code": options.source_language_code,
                "target_language_code": options.target_language_code,
            }
        )
        return response.translations[0].translated_text
