import os
from abc import ABC

from .supported_formats import InputFormat, OutputFormat


class ConverterService(ABC):
    @staticmethod
    def convert_text(*, input_text: str, input_format: InputFormat, output_format: OutputFormat) -> str:
        """
        Args:
            input_text: the input text to be converted
            input_format: the file format of the input
            output_format: the desired format for the output text

        Returns: the ``input_text`` converted into a ``str`` in the specified ``output_format``
        """
        raise NotImplementedError('This method needs to be implemented')

    @staticmethod
    def convert_file(*,
                     input_file: os.PathLike[str],
                     input_format: InputFormat,
                     output_file: os.PathLike[str],
                     output_format: OutputFormat) -> None:
        """
        Args:
            input_file: path to the input file
            input_format: the file format of the input file
            output_file: path to the output file
            output_format: the desired format for the output file

        Returns: ``None``
        """
        raise NotImplementedError('This method needs to be implemented')
