import os

import pypandoc

from . import ConverterService, InputFormat, OutputFormat


class PandocConverterService(ConverterService):

    @staticmethod
    def convert_text(*, input_text: str, input_format: InputFormat, output_format: OutputFormat) -> str:
        return pypandoc.convert_text(source=input_text, format=input_format, to=output_format)

    @staticmethod
    def convert_file(*,
                     input_file: os.PathLike[str],
                     input_format: InputFormat,
                     output_file: os.PathLike[str],
                     output_format: OutputFormat) -> None:
        pypandoc.convert_file(source_file=str(input_file),
                              format=input_format,
                              outputfile=str(output_file),
                              to=output_format)
