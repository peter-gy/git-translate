from abc import ABC

from .supported_formats import InputFormat, OutputFormat


class ConverterService(ABC):
    @staticmethod
    def convert_text(*, source: str, input_format: InputFormat, output_format: OutputFormat) -> str:
        """
        Args:
            source: the source file to be converted, as a ``str``
            input_format: the file format of the source file
            output_format: the desired format for the output text

        Returns: the ``source`` converted into a ``str`` in the specified ``output_format``
        """
        raise NotImplementedError('This method needs to be implemented')
