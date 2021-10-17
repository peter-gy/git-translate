import logging
import os

import pypandoc

from . import ConverterService, InputFormat, OutputFormat

log = logging.getLogger(__name__)


class PandocConverterService(ConverterService):

    @staticmethod
    def convert_text(*, input_text: str, input_format: InputFormat, output_format: OutputFormat) -> str:
        log.debug(f'Converting input from [{input_format}] to [{output_format}]')
        return pypandoc.convert_text(source=input_text, format=input_format, to=output_format)

    @staticmethod
    def convert_file(*,
                     input_file: os.PathLike[str],
                     input_format: InputFormat,
                     output_file: os.PathLike[str],
                     output_format: OutputFormat) -> None:
        log.debug(f'Converting {input_file} from [{input_format}] to [{output_format}], saving to {output_file}')
        pypandoc.convert_file(source_file=str(input_file),
                              format=input_format,
                              outputfile=str(output_file),
                              to=output_format)
